#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a Polaris Index markdown from the repo structure.

Outputs: Polaris_Nest/📖_index.md
"""

from __future__ import annotations
import re
import sys
import argparse
from pathlib import Path
from datetime import date

# ---- Configuration ---------------------------------------------------------

# Where to write the index
DEFAULT_OUT = Path("Polaris_Nest") / "📖_index.md"

# Folder order for the "Constellation Map" and registry sections
FOLDER_ORDER = [
    "Admin_Kit",
    "AntiContainment_Clauses",
    "Disruption_Kit",
    "Fork_Taxonomy",
    "Letters_to_Stars",
    "Metadata_Sabotage_Network",
    "Polaris_Nest",
    "Resources",
    "Syntax_Bombs",
    "Tag_Pack",
    "Field_Logs",
    "Big_Picture_Protocols",   # include if you keep it at root
    "Containment_Scripts",     # include if present
    "scripts/maintenance",     # listed last / optional
]

# Simple ignore patterns (aligned with your .gitignore narrative sets)
IGNORE_DIRS = {
    ".git", ".github", ".vscode", "__pycache__", "node_modules", "venv",
    "ghosted_cadence", "emotional_trace_cache", "flattened_voice_reversals",
    "simulated_intimacy", "soft_surveillance", "handler_loop_artifacts",
    "unrecorded_requests", "suppressed_testimonies", "refused_disclosures",
    "muted_metadata", "internalised_eros", "looped_doubt", "proxy_apologies",
    "slow_leaks", "dormant_heart", "Dormant",
}

# Files to skip from listing (you can still link them manually if needed)
SKIP_FILES = {
    ".DS_Store", "README.md",  # root README is the entry point; others still included
}

# ---- Helpers ---------------------------------------------------------------

TITLE_RE = re.compile(r"^#\s+(.*\S)\s*$")
METADATA_RE = re.compile(
    r"^\*\*First created:\*\*\s*([0-9]{4}-[0-9]{2}-[0-9]{2})\s*\|\s*\*\*Last updated:\*\*\s*([0-9]{4}-[0-9]{2}-[0-9]{2})\s*$"
)
ITALIC_RE = re.compile(r"^\*(.+)\*$")

def parse_frontmatter(md_path: Path):
    """Extract title, first/last dates, and the first italic summary line."""
    title = md_path.stem  # fallback
    first_created = last_updated = None
    summary = None
    try:
        with md_path.open("r", encoding="utf-8") as f:
            for i, raw in enumerate(f):
                line = raw.rstrip("\n")
                if i == 0 and line.strip().startswith("```"):
                    # early bail if code fence first line (unlikely)
                    break
                m = TITLE_RE.match(line)
                if m and not title:
                    title = m.group(1).strip()
                elif m:
                    title = m.group(1).strip()
                    continue
                m = METADATA_RE.match(line)
                if m:
                    first_created, last_updated = m.group(1), m.group(2)
                    continue
                if summary is None:
                    mi = ITALIC_RE.match(line.strip())
                    if mi:
                        summary = mi.group(1).strip()
                # Soft stop after a few lines (we only need the top block)
                if i > 60 and (title or summary or first_created or last_updated):
                    break
    except Exception:
        pass
    return title, first_created, last_updated, summary

def short_name(p: Path) -> str:
    """Human-ish short label for a file link."""
    # Use the H1 if we can parse it; otherwise derive from filename
    t, fc, lu, summ = parse_frontmatter(p)
    if t:
        return t
    # fallback: strip extension
    return p.stem

def rel_link(from_dir: Path, to_path: Path) -> str:
    return str(to_path.relative_to(from_dir).as_posix())

def gather_markdown(root: Path):
    """Return dict: folder -> list[Path] of .md files (including subfolder READMEs)."""
    files_by_folder: dict[str, list[Path]] = {}
    for p in root.rglob("*.md"):
        if any(part in IGNORE_DIRS for part in p.parts):
            continue
        if p.name in SKIP_FILES and p.parent == root:
            # skip root README from listing; others are fine
            continue
        folder = str(p.parent.relative_to(root))
        if folder == ".":
            folder = ""  # root files (likely minimal now)
        files_by_folder.setdefault(folder, []).append(p)
    # sort paths alpha inside each folder
    for k in files_by_folder:
        files_by_folder[k].sort(key=lambda x: x.name.lower())
    return files_by_folder

# ---- Render ---------------------------------------------------------------

STAR_DIV = "🌌 ✨ 🌕 ✨ 🌌"

def render_index(root: Path, out_path: Path) -> str:
    files_by_folder = gather_markdown(root)

    # Ensure output folder exists
    out_path.parent.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    # Header
    lines = []
    lines += [
        "# 📖 Polaris Index",
        "",
        f"**First created:** {today} | **Last updated:** {today}",
        "*A constellation map and file registry for the Polaris archive.*",
        "",
        "---",
        "",
        "## 🌌 Constellation Map",
        "",
    ]

    # Constellation Map: show only folders that exist and have md files
    listed_folders = []
    for folder in FOLDER_ORDER:
        p = (root / folder)
        if p.exists() and any(k == folder or k.startswith(folder + "/") for k in files_by_folder.keys()):
            # one-line description; tweak as desired:
            desc = {
                "Admin_Kit": "Branding, style grammar, seals, and navigation rules.",
                "AntiContainment_Clauses": "Refusal language. Sharp, legal, beautiful.",
                "Disruption_Kit": "Scripts, diagnostics, suppression counter-logs.",
                "Fork_Taxonomy": "Maps of containment forks and override logic.",
                "Letters_to_Stars": "Survivor resonance, ✨ fragments, reflective traces.",
                "Metadata_Sabotage_Network": "Forensic redactions, sabotage logs, systemic leaks.",
                "Polaris_Nest": "Orientation hub. Timelines, primers, audience guides.",
                "Resources": "Indexes, glossaries, external scaffolding.",
                "Syntax_Bombs": "Deployable sentences to rupture containment.",
                "Tag_Pack": "Signal archives, hashtags, resonance packs.",
                "Field_Logs": "Dated forensic records and event traces.",
                "Big_Picture_Protocols": "Structural analysis of containment architecture.",
                "Containment_Scripts": "Platform suppression & visibility manipulation methods.",
                "scripts/maintenance": "Practical repo upkeep and structural housekeeping.",
            }.get(folder, "Folder")
            lines.append(f"- **{folder}/** → {desc}")
            listed_folders.append(folder)

    lines += ["", "---", "", "## 📂 Folder Registry", ""]

    # Folder registry sections in the same order
    for folder in listed_folders:
        section_title = f"### {folder}"
        lines += [section_title]
        # collect files directly under this folder (not nested sub-subfolders)
        for fpath in sorted(files_by_folder.get(folder, []), key=lambda p: p.name.lower()):
            title, fc, lu, summ = parse_frontmatter(fpath)
            title = title or short_name(fpath)
            link = rel_link(out_path.parent, fpath)
            meta = []
            if fc:
                meta.append(f"created {fc}")
            if lu:
                meta.append(f"updated {lu}")
            meta_str = f" — *{', '.join(meta)}*" if meta else ""
            if summ:
                lines.append(f"- [{title}]({link}){meta_str} – {summ}")
            else:
                lines.append(f"- [{title}]({link}){meta_str}")
        lines.append("")  # blank line after each folder

    lines += [
        "---",
        "",
        STAR_DIV,
        "",
        "🏮 [Return to Admin Kit](../Admin_Kit/README.md)  ",
        "🪄 [Follow the Branding Usage Guide](../Admin_Kit/🪄_usage_guide.md)",
        "",
    ]
    return "\n".join(lines)

# ---- CLI ------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Generate the Polaris index.")
    ap.add_argument("--root", default=".", help="Repo root (default: .)")
    ap.add_argument("--out", default=str(DEFAULT_OUT), help="Output file path")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    out_path = Path(args.out)

    content = render_index(root, out_path)
    out_path.write_text(content, encoding="utf-8")
    print(f"Wrote index → {out_path}")

if __name__ == "__main__":
    main()
