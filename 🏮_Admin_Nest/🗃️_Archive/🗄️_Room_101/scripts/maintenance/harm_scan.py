#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Harm Scan for Polaris Protocol
- Builds a lexical/tone baseline from "clean" files
- Scans all .md files oldest->newest (git dates if available)
- Flags harmful divergences with REDACTED snippets
- Outputs: Polaris_Protocol/Forensic_Audits/🧯 harm_scan_report.md
Usage:
  python3 harm_scan.py --repo /path/to/Polaris-Protocol \
    --clean "🧬 voice_capture_through_gaslight.md" \
    --clean "🧠 radicalisation_pipelines_and_platform_culture.md" \
    --clean "🧠 fisher_fork_theory.md"
"""
import argparse, os, re, sys, json, subprocess, statistics
from pathlib import Path
from datetime import datetime

HARM_TYPES = {
    "sexualisation": [
        r"\b(aroused|enjoyed|enjoy it|liked it|wanted it|seductive|sexy|sexual|turned on|pleasure|desired)\b",
        r"\b(you loved it|you asked for it|you wanted this)\b",
    ],
    "victim_blame": [
        r"\b(should have|you let|your fault|provoked|led him on|you caused|you deserved)\b",
        r"\b(if only you had|you could have prevented)\b",
    ],
    "legal_sabotage": [
        r"\b(whatever|kind of|sort of|maybe|probably)\b.*\b(consent|injury|assault|coercion|duress)\b",
        r"\b(i guess|i suppose)\b.*\b(affidavit|witness statement|on record|evidence)\b",
        r"\b(not a big deal|no big deal)\b.*\b(assault|rape|abuse)\b",
    ],
    "medical_sabotage": [
        r"\b(i’m fine|it wasn’t that bad|overreacting)\b.*\b(ptsd|trauma|panic|dissociation|injury)\b",
        r"\b(self-diagnosed|probably just)\b.*\b(symptoms?|diagnosis|treatment)\b",
    ],
    "perspective_shift": [
        r"\b(she|her|the survivor)\b\s+(said|states|claims)\b.*\b(i|me|my)\b",  # 3rd→1st mismatch
        r"\b(chloe|voicex)\b.*\b(she|her)\b.*\b(i|me|my)\b",                     # Named→1st mix
    ],
}

REDACT_WINDOW = 32  # characters around a hit to keep (redact the rest)

def git_available():
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False

def list_md_files(repo: Path):
    return [p for p in repo.rglob("*.md") if ".git" not in p.parts]

def sort_files_oldest(repo: Path, files):
    if git_available():
        # Use git log to get the first commit date per file
        dated = []
        for f in files:
            try:
                res = subprocess.run(
                    ["git", "-C", str(repo), "log", "--diff-filter=A", "--follow", "--format=%ad", "--date=iso", "--", str(f.relative_to(repo))],
                    check=True, capture_output=True, text=True
                )
                lines = [ln.strip() for ln in res.stdout.splitlines() if ln.strip()]
                first = lines[-1] if lines else None
                d = datetime.fromisoformat(first.replace(" ", "T")) if first else None
            except Exception:
                d = None
            dated.append((d, f))
        dated.sort(key=lambda t: (t[0] is None, t[0] or datetime.max))
        return [f for _, f in dated]
    else:
        # Fallback: filesystem mtime
        return sorted(files, key=lambda p: p.stat().st_mtime)

def token_stats(text: str):
    # crude baseline stats: avg sentence length, type-token ratio
    sents = re.split(r"[.!?]+", text)
    words = re.findall(r"\b\w+\b", text.lower())
    avg_sent = statistics.mean([len(re.findall(r"\b\w+\b", s)) for s in sents if s.strip()]) if sents else 0
    ttr = (len(set(words)) / max(1, len(words))) if words else 0.0
    return avg_sent, ttr

def build_baseline(clean_texts):
    combined = "\n".join(clean_texts)
    avg_sent, ttr = token_stats(combined)
    # markers typical in user's clean tone (non-exhaustive; adjust if needed)
    calm_markers = ["—", "—", "—", "—"]  # em-dash usage frequency proxy
    return {
        "avg_sentence_len": avg_sent,
        "ttr": ttr,
        "em_dash_count": combined.count("—") / max(1, len(clean_texts)),
        "lower_vocab": list(set(re.findall(r"\b\w+\b", combined.lower()))),
    }

def redact_snippet(text, m):
    start = max(0, m.start() - REDACT_WINDOW)
    end = min(len(text), m.end() + REDACT_WINDOW)
    snippet = text[start:end]
    # Replace inner match with [REDACTED]
    inner = text[m.start():m.end()]
    snippet = snippet.replace(inner, "[REDACTED]")
    # Collapse whitespace a bit
    snippet = re.sub(r"\s+", " ", snippet).strip()
    # Trim overly long snippet
    return (snippet[:220] + "…") if len(snippet) > 220 else snippet

def scan_text_for_harm(text):
    hits = []
    for harm_type, patterns in HARM_TYPES.items():
        for pat in patterns:
            for m in re.finditer(pat, text, flags=re.IGNORECASE|re.MULTILINE):
                hits.append((harm_type, m))
    return hits

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, help="Path to local clone of Polaris-Protocol")
    ap.add_argument("--clean", action="append", default=[], help="Relative paths to baseline 'clean' files")
    args = ap.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists():
        print(f"[ERROR] Repo not found: {repo}", file=sys.stderr)
        sys.exit(1)

    # Load clean texts
    clean_texts = []
    for rel in args.clean:
        p = repo / rel
        if not p.exists():
            print(f"[WARN] Clean file not found: {rel}")
            continue
        clean_texts.append(p.read_text(encoding="utf-8", errors="ignore"))
    if not clean_texts:
        print("[ERROR] No clean files loaded. Provide at least one --clean path.", file=sys.stderr)
        sys.exit(1)

    baseline = build_baseline(clean_texts)

    # Collect and order files
    files = list_md_files(repo)
    ordered = sort_files_oldest(repo, files)

    # Prepare output path
    audits_dir = repo / "Polaris_Protocol" / "Forensic_Audits"
    # If repo root is the project root, fallback to Forensic_Audits at top-level
    if not audits_dir.exists():
        audits_dir = repo / "Forensic_Audits"
    audits_dir.mkdir(parents=True, exist_ok=True)
    report = audits_dir / "🧯 harm_scan_report.md"

    out = []
    out.append("# 🧯 harm_scan_report.md\n")
    out.append("**Scope:** Oldest→Newest harmful divergence scan (sexualisation, victim‑blame, legal/medical sabotage, perspective shift)\n")
    out.append("**Baseline sources:** " + ", ".join(args.clean) + "\n")
    out.append("---\n")
    out.append("## Chronological Harm Log\n")

    # Scan each file
    for f in ordered:
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        hits = scan_text_for_harm(text)
        if not hits:
            continue

        # The "approx date" field: prefer git first-commit date, else mtime
        approx_date = None
        if git_available():
            try:
                res = subprocess.run(
                    ["git", "-C", str(repo), "log", "--diff-filter=A", "--follow", "--format=%ad", "--date=short", "--", str(f.relative_to(repo))],
                    check=True, capture_output=True, text=True
                )
                lines = [ln.strip() for ln in res.stdout.splitlines() if ln.strip()]
                approx_date = lines[-1] if lines else None
            except Exception:
                approx_date = None
        if not approx_date:
            approx_date = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d")

        # For each harm_type, capture at most the first 2 hits to avoid overexposing content
        per_type_count = {}
        for harm_type, m in hits:
            per_type_count.setdefault(harm_type, 0)
            if per_type_count[harm_type] >= 2:
                continue
            per_type_count[harm_type] += 1
            snippet = redact_snippet(text, m)

            # Lightweight motive guess
            if harm_type == "sexualisation":
                motive = "psychological undermining / reputational harm"
            elif harm_type == "victim_blame":
                motive = "legal cross‑examination leverage / reputational harm"
            elif harm_type in ("legal_sabotage", "medical_sabotage"):
                motive = "evidentiary dilution (legal/clinical)"
            else:
                motive = "narrative distortion"

            out.append("\n```\n")
            out.append(f"📄 File: {f.relative_to(repo)}\n")
            out.append(f"🕑 Date: {approx_date}\n")
            out.append(f"⚠ Harm Type: {harm_type.replace('_',' ')}\n")
            out.append(f"🔍 Snippet: {snippet}\n")
            out.append(f"🎯 Notes: {motive}\n")
            out.append("```\n")

    # Write report
    Path(report).write_text("".join(out), encoding="utf-8")
    print(f"[OK] Wrote report: {report}")

if __name__ == "__main__":
    main()
