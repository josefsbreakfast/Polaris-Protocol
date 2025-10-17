import sys, re, csv, pathlib
from datetime import date

# Usage: python parse_usna_removed_books.py input.pdf output.csv
inp = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])

# Dependences: pip install pdfplumber
import pdfplumber

SOURCE_URL = "https://media.defense.gov/2025/Apr/04/2003683009/-1/-1/0/250404-LIST%20OF%20REMOVED%20BOOKS%20FROM%20NIMITZ%20LIBRARY.PDF"
SOURCE_DATE = "2025-04-04"

rows = []
with pdfplumber.open(str(inp)) as pdf:
    for page in pdf.pages:
        # Try reading tabular data first
        tables = page.extract_tables()
        if tables:
            for table in tables:
                for r in table:
                    if not r or len(r) < 3: 
                        continue
                    # Heuristic: header row starts with 'Title'
                    if str(r[0]).strip().lower().startswith("title"):
                        continue
                    title = (r[0] or "").strip()
                    pub = (r[1] or "").strip()
                    subjects = (r[2] or "").strip()
                    if title:
                        rows.append([title, pub, subjects, SOURCE_URL, SOURCE_DATE])
        else:
            # Fallback: parse text lines (if table extraction fails on some pages)
            text = page.extract_text() or ""
            # Find lines that look like: "<Title>  [YYYY]  <subjects...>"
            # We'll capture generously and clean later.
            for line in text.splitlines():
                line = line.strip()
                if not line or line.lower().startswith(("list of removed books", "released:", "title", "publication date", "subjects")):
                    continue
                # Split using two or more spaces or a tab
                parts = re.split(r"\s{2,}|\t", line)
                if len(parts) >= 3:
                    title, pub, subjects = parts[0].strip(), parts[1].strip(), " ".join(p.strip() for p in parts[2:])
                    if title:
                        rows.append([title, pub, subjects, SOURCE_URL, SOURCE_DATE])

# Deduplicate while preserving order
seen = set()
deduped = []
for r in rows:
    key = tuple(r[:3])
    if key not in seen:
        seen.add(key)
        deduped.append(r)

with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title","PublicationDate","Subjects","SourceURL","SourceDate"])
    writer.writerows(deduped)

print(f"Wrote {len(deduped)} rows to {out}")
