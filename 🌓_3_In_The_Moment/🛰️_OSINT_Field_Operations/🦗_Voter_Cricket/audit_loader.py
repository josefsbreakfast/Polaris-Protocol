
#!/usr/bin/env python3
"""
audit_loader.py — Lightweight helper to scan the 🧭 Citizen Audit CSV and surface potential risk hotspots.

Usage:
  python audit_loader.py --csv path/to/🧭_citizen_audit_log_template.csv --outdir out/

What it does:
  1) Loads the CSV and normalises field names.
  2) Computes basic flags (boundary change, foreign ownership, hosting location, spend ratios, turnout shifts).
  3) Produces:
     - out/summary.csv          (per-row flags + risk score/category)
     - out/region_summary.csv   (counts by risk category per region)
     - out/summary.md           (human-readable Markdown summary)

Notes:
  - This is a heuristic triage tool, not a determination of wrongdoing.
  - Keep personal data out of your CSV. Stick to public/aggregate sources.
"""

import argparse
import re
from pathlib import Path
from typing import Dict, List
import pandas as pd
import numpy as np

CANON = {
    # Canonical expected columns -> list of fuzzy aliases
    "constituency_or_ward": ["constituency_or_ward","constituency","ward","seat"],
    "region": ["region"],
    "borough_or_council": ["borough_or_council","council","local_authority"],
    "year_of_election": ["year_of_election","year"],
    "boundary_change_y_n": ["boundary_change_y_n","boundary_change","boundary_change_y/n","boundary_change_flag"],
    "boundary_change_notes": ["boundary_change_notes"],
    "seat_status": ["seat_status(gain/loss/hold)","seat_status","status"],
    "party_targeting_observed": ["party_targeting_observed","targeting_observed","parties_targeting"],
    "main_local_issues": ["main_local_issues","issues"],
    "digital_ad_spend": ["digital_ad_spend(£)","digital_ad_spend","digital_spend","digital_ads_spend"],
    "physical_campaign_spend": ["physical_campaign_spend(£)","physical_campaign_spend","physical_spend"],
    "declared_data_consultancy": ["declared_data_consultancy","data_consultancy","analytics_vendor","consultancy"],
    "consultancy_company_number": ["consultancy_company_number","company_number"],
    "ownership_notes": ["ownership_notes(foreign/uk)","ownership_notes","ownership"],
    "cloud_or_hosting_location": ["cloud_or_hosting_location","hosting_location","cloud_region"],
    "foi_requests_filed": ["foi_requests_filed(y/n)","foi_requests_filed","foi_filed"],
    "foi_reference_numbers": ["foi_reference_numbers","foi_refs","foi_reference"],
    "notable_ads_or_messaging_themes": ["notable_ads_or_messaging_themes","ads_themes","messaging_themes"],
    "turnout_change_pct_vs_previous": ["turnout_change(%)_vs_previous","turnout_change_pct_vs_previous","turnout_change"],
    "possible_behavioural_tactics_observed": ["possible_behavioural_tactics_observed","behavioural_tactics","tactics_observed"],
    "source_links": ["source_links","sources","links"],
    "researcher_or_group": ["researcher_or_group","researcher","group"],
    "date_logged": ["date_logged","logged_date"],
    "verification_status": ["verification_status"],
    "comments_and_context": ["comments_and_context","comments","notes"]
}

FOREIGN_OWNERSHIP_KEYWORDS = [
    # crude indicators; editable per project
    "foreign", "overseas", "parent", "owned by", "subsidiary", "delaware",
    "cayman", "bvi", "singapore", "hong kong", "uae", "qatar", "saudi",
    "russia", "china", "US parent", "non-UK", "non uk", "offshore"
]

FEAR_IDENTITY_KEYWORDS = [
    "fear", "protect", "security", "stability", "crime", "threat",
    "invasion", "take back", "zero tolerance", "enemy", "traitors",
    "identity", "culture war", "replacement"
]

HOST_OUTSIDE_UK_INDICATORS = [
    # simple heuristics for non-UK hosting
    "us-", "us ", "united states", "usa", "singapore", "ap-southeast",
    "australia", "india", "japan", "east asia", "south america",
    "canada", "ca-", "sa-", "africa", "me-", "middle east"
]

def normalise_columns(df: pd.DataFrame) -> pd.DataFrame:
    def norm(s: str) -> str:
        s = s.strip().lower()
        s = re.sub(r"[\s/()%-]+", "_", s)
        s = re.sub(r"[^a-z0-9_]+", "", s)
        return s
    df = df.copy()
    df.columns = [norm(c) for c in df.columns]
    # build mapping from current -> canon
    mapping: Dict[str,str] = {}
    for canon, aliases in CANON.items():
        for alias in aliases:
            alias_n = re.sub(r"[^a-z0-9_]+","", alias.lower())
            for col in df.columns:
                if col == alias_n:
                    mapping[col] = canon
    # merge columns if duplicates map to same canon
    out = {}
    for col in df.columns:
        key = mapping.get(col, col)
        if key in out:
            # prefer the column with fewer nulls
            s_old = out[key]
            s_new = df[col]
            out[key] = s_new if s_new.notna().sum() >= s_old.notna().sum() else s_old
        else:
            out[key] = df[col]
    ndf = pd.DataFrame(out)
    return ndf

def to_float(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series.astype(str).str.replace(",", "").str.replace("£",""), errors="coerce")

def flag_foreign_ownership(text: str) -> bool:
    if not isinstance(text, str):
        return False
    t = text.lower()
    return any(k in t for k in FOREIGN_OWNERSHIP_KEYWORDS)

def flag_hosting_outside_uk(text: str) -> bool:
    if not isinstance(text, str):
        return False
    t = text.lower()
    if "uk" in t or "united kingdom" in t or "london" in t or "cardiff" in t or "manchester" in t:
        return False
    return any(k in t for k in HOST_OUTSIDE_UK_INDICATORS)

def flag_behavioural_themes(theme_text: str, tactics_text: str) -> bool:
    t = (theme_text or "") + " " + (tactics_text or "")
    t = t.lower()
    return any(k in t for k in FEAR_IDENTITY_KEYWORDS)

def compute_risk_row(row: pd.Series) -> Dict[str, object]:
    # Numeric conversions
    dig = to_float(row.get("digital_ad_spend", pd.NA))
    phy = to_float(row.get("physical_campaign_spend", pd.NA))
    turnout = pd.to_numeric(row.get("turnout_change_pct_vs_previous", pd.NA), errors="coerce")
    ratio = np.nan
    if pd.notna(dig) and pd.notna(phy) and phy != 0:
        ratio = float(dig) / float(phy)
    elif pd.notna(dig) and (pd.isna(phy) or phy == 0):
        ratio = np.inf

    boundary = str(row.get("boundary_change_y_n", "")).strip().lower() in ("y","yes","true","1")
    consultancy = str(row.get("declared_data_consultancy", "")).strip() != ""
    foreign_owner = flag_foreign_ownership(row.get("ownership_notes", ""))
    hosting_outside_uk = flag_hosting_outside_uk(row.get("cloud_or_hosting_location", ""))
    emotive_behavioural = flag_behavioural_themes(
        row.get("notable_ads_or_messaging_themes", ""),
        row.get("possible_behavioural_tactics_observed", ""),
    )

    risk = 0
    if boundary: risk += 1
    if consultancy: risk += 1
    if foreign_owner: risk += 2
    if hosting_outside_uk: risk += 1
    if pd.notna(ratio) and ratio != np.inf and ratio > 1.5: risk += 1
    if ratio == np.inf: risk += 2  # digital only
    if pd.notna(turnout) and abs(float(turnout)) > 3.0: risk += 1
    if emotive_behavioural: risk += 1

    if risk >= 5:
        cat = "High"
    elif risk >= 3:
        cat = "Medium"
    else:
        cat = "Low"

    return {
        "digital_physical_ratio": ratio,
        "boundary_change_flag": boundary,
        "declared_consultancy_flag": consultancy,
        "foreign_owner_flag": foreign_owner,
        "hosting_outside_uk_flag": hosting_outside_uk,
        "emotive_behavioural_flag": emotive_behavioural,
        "risk_score": risk,
        "risk_category": cat,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="Path to 🧭_citizen_audit_log_template.csv (or derivative).")
    ap.add_argument("--outdir", default="out", help="Directory for outputs (default: out)")
    args = ap.parse_args()

    in_path = Path(args.csv)
    out_dir = Path(args.outdir)
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(in_path, comment="#")
    df = normalise_columns(df)

    # Compute flags
    risks: List[Dict[str,object]] = []
    for _, row in df.iterrows():
        risks.append(compute_risk_row(row))
    rfx = pd.DataFrame(risks)

    # Stitch summary
    keep_cols = [
        "constituency_or_ward","region","borough_or_council","year_of_election",
        "boundary_change_y_n","seat_status","party_targeting_observed",
        "main_local_issues","declared_data_consultancy","consultancy_company_number",
        "ownership_notes","cloud_or_hosting_location",
        "notable_ads_or_messaging_themes","possible_behavioural_tactics_observed",
        "turnout_change_pct_vs_previous","source_links","verification_status"
    ]
    for k in keep_cols:
        if k not in df.columns:
            df[k] = np.nan

    summary = pd.concat([df[keep_cols], rfx], axis=1)
    summary.to_csv(out_dir / "summary.csv", index=False)

    # Region summary
    region_summary = (
        summary
        .fillna({"region":"(unknown)"})
        .groupby(["region","risk_category"])
        .size()
        .reset_index(name="count")
        .sort_values(["region","risk_category"])
    )
    region_summary.to_csv(out_dir / "region_summary.csv", index=False)

    # Markdown overview
    md_lines = []
    md_lines.append("# Citizen Audit — Automated Summary\n")
    md_lines.append(f"- Source CSV: `{in_path}`\n")
    md_lines.append(f"- Rows analysed: **{len(summary)}**\n")
    md_lines.append("\n## Risk Category Counts (overall)\n")
    overall = summary["risk_category"].value_counts().rename_axis("risk_category").reset_index(name="count")
    for _, r in overall.iterrows():
        md_lines.append(f"- **{r['risk_category']}**: {int(r['count'])}")
    md_lines.append("\n## Regions by Risk\n")
    for region, sub in region_summary.groupby("region"):
        counts = ", ".join([f"{rc}: {int(c)}" for rc, c in sub[["risk_category","count"]].values])
        md_lines.append(f"- **{region}** — {counts}")
    md_lines.append("\n> This is a heuristic triage; investigate High/Medium rows with primary evidence (FOIs, ad libraries, filings).")
    (out_dir / "summary.md").write_text("\n".join(md_lines), encoding="utf-8")

    print(f"✓ Wrote: {out_dir/'summary.csv'}")
    print(f"✓ Wrote: {out_dir/'region_summary.csv'}")
    print(f"✓ Wrote: {out_dir/'summary.md'}")

if __name__ == "__main__":
    main()
