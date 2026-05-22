#!/usr/bin/env bash
# PRIVATE_LOCAL
# Polaris Protocol — Folder Consistency Pass
# Default: SCAN ONLY (no changes). Use --apply to perform safe renames/moves.
set -Eeuo pipefail

APPLY=false
if [[ "${1:-}" == "--apply" ]]; then
  APPLY=true
fi

# Ensure we run from repo root
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$REPO_ROOT" ]]; then
  echo "❌ Not inside a Git repo. Aborting."
  exit 2
fi
cd "$REPO_ROOT"

# Paths
OUTDIR="scripts/maintenance/reports"
mkdir -p "$OUTDIR"
TS="$(date -u +"%Y-%m-%dT%H%M%SZ")"
REPORT="$OUTDIR/folder_consistency_report_${TS}.md"

# Accumulators
issues_found=0

# Helpers
print_section () {
  {
    echo
    echo "## $1"
    echo
  } >> "$REPORT"
}

note_issue () {
  issues_found=$((issues_found+1))
}

echo "# Folder Consistency Report" > "$REPORT"
echo "**Timestamp (UTC):** ${TS}" >> "$REPORT"
echo "**Mode:** $([[ "$APPLY" == true ]] && echo "APPLY (will fix simple issues)" || echo "SCAN (no changes)")" >> "$REPORT"
echo >> "$REPORT"
echo "---" >> "$REPORT"

###############################
# 1) Known split folder check #
###############################
print_section "SCP-VoiceX casefiles folder split"

BAD_DIR="Polaris_Nest/SCP-VoiceX _Casefiles"
GOOD_DIR="Polaris_Nest/SCP-VoiceX_Casefiles"

if [[ -d "$BAD_DIR" ]]; then
  note_issue
  echo "- Found stray folder: \`$BAD_DIR\`" >> "$REPORT"
  echo "- Canonical target: \`$GOOD_DIR\`" >> "$REPORT"
  echo "- Contents queued to move:" >> "$REPORT"
  { find "$BAD_DIR" -mindepth 1 -maxdepth 1 -print | sed 's/^/  - /'; } >> "$REPORT"

  if [[ "$APPLY" == true ]]; then
    mkdir -p "$GOOD_DIR"
    # Move top-level entries only (files/dirs)
    while IFS= read -r -d '' p; do
      git mv "$p" "$GOOD_DIR/"
    done < <(find "$BAD_DIR" -mindepth 1 -maxdepth 1 -print0)
    rmdir "$BAD_DIR" 2>/dev/null || true
    echo "- ✅ Applied: moved contents to \`$GOOD_DIR\` and removed stray folder." >> "$REPORT"
  else
    echo "- ➜ Run with \`--apply\` to fix." >> "$REPORT"
  fi
else
  echo "- No split casefiles folder detected." >> "$REPORT"
fi

#############################################
# 2) Directories with ' <underscore>' typos #
#############################################
print_section "Directories with ' <underscore>' typo (space before underscore)"

mapfile -t BAD_DIRS < <(git ls-files -z | xargs -0 -n1 dirname | sort -u | grep " _" || true)
if ((${#BAD_DIRS[@]})); then
  note_issue
  for d in "${BAD_DIRS[@]}"; do
    canon="$(sed 's/ \_/_/g' <<<"$d")"
    echo "- \`$d\` ➜ \`$canon\`" >> "$REPORT"
    if [[ "$APPLY" == true ]]; then
      mkdir -p "$canon"
      git mv "$d" "$canon"
      echo "  - ✅ Applied rename" >> "$REPORT"
    fi
  done
  [[ "$APPLY" == false ]] && echo "- ➜ Run with \`--apply\` to rename above directories." >> "$REPORT"
else
  echo "- No directory names with the ' _' typo found." >> "$REPORT"
fi

##########################################
# 3) Filenames containing backticks `    #
##########################################
print_section "Filenames containing backticks (\\`)"

mapfile -t TICK_FILES < <(git ls-files | grep '\`' || true)
if ((${#TICK_FILES[@]})); then
  note_issue
  for f in "${TICK_FILES[@]}"; do
    clean="${f//\`/}"
    echo "- \`$f\` ➜ \`$clean\`" >> "$REPORT"
    if [[ "$APPLY" == true ]]; then
      dir="$(dirname "$clean")"
      base="$(basename "$clean")"
      mkdir -p "$dir"
      git mv "$f" "$dir/$base"
      echo "  - ✅ Applied rename" >> "$REPORT"
    fi
  done
  [[ "$APPLY" == false ]] && echo "- ➜ Run with \`--apply\` to strip backticks from filenames." >> "$REPORT"
else
  echo "- No filenames with backticks found." >> "$REPORT"
fi

##########################################################
# 4) Specific icc_tag_thread_containment stray backtick  #
##########################################################
print_section "Specific check: stray-backtick ICC file (defensive)"

ICC_BAD="Polaris_Nest/SCP-VoiceX_Casefiles/🧷 \`icc_tag_thread_containment.md"
ICC_GOOD="Polaris_Nest/SCP-VoiceX_Casefiles/🧷 icc_tag_thread_containment.md"
if [[ -f "$ICC_BAD" ]]; then
  note_issue
  echo "- Found: \`$ICC_BAD\` ➜ should be \`$ICC_GOOD\`" >> "$REPORT"
  if [[ "$APPLY" == true ]]; then
    git mv "$ICC_BAD" "$ICC_GOOD"
    echo "  - ✅ Applied rename" >> "$REPORT"
  else
    echo "- ➜ Run with \`--apply\` to fix." >> "$REPORT"
  fi
else
  echo "- No stray-backtick ICC file detected." >> "$REPORT"
fi

##############################################
# 5) Duplicate basenames across the repo     #
##############################################
print_section "Duplicate basenames (same filename in multiple paths)"

# Build a list of basenames and count duplicates
TMP_BN="$(mktemp)"
git ls-files | awk '{print $0"\t"gensub(".*/","",1)}' > "$TMP_BN"
# shellcheck disable=SC2002
dups=$(cut -f2 "$TMP_BN" | sort | uniq -d || true)
if [[ -n "${dups}" ]]; then
  note_issue
  while IFS= read -r bn; do
    [[ -z "$bn" ]] && continue
    echo "- **$bn**" >> "$REPORT"
    grep -F "$bn" "$TMP_BN" | cut -f1 | sed 's/^/  - /' >> "$REPORT"
  done <<< "$dups"
  echo >> "$REPORT"
  echo "> Note: Duplicates are not auto-fixed. Use your reorg map to validate which are intentional (e.g., conceptual vs case-log pairs) and which should be archived." >> "$REPORT"
else
  echo "- No duplicate basenames found." >> "$REPORT"
fi
rm -f "$TMP_BN"

##############################################
# 6) Governance toolkit presence check       #
##############################################
print_section "Governance toolkit presence"

need_flag=false
if [[ ! -f "scripts/maintenance/polaris_file_index_2025-08-10.md" ]]; then
  note_issue; need_flag=true
  echo "- Missing: \`scripts/maintenance/polaris_file_index_2025-08-10.md\`" >> "$REPORT"
fi
if [[ ! -f "scripts/maintenance/polaris_file_reorg_map.md" ]]; then
  note_issue; need_flag=true
  echo "- Missing: \`scripts/maintenance/polaris_file_reorg_map.md\`" >> "$REPORT"
fi
if [[ "$need_flag" == false ]]; then
  echo "- Snapshot + reorg map are present." >> "$REPORT"
fi

echo >> "$REPORT"
echo "---" >> "$REPORT"
echo "**Summary:** $issues_found issue group(s) detected." >> "$REPORT"
[[ "$APPLY" == true ]] && echo "**Applied automatic fixes where safe.**" >> "$REPORT" || true

# Exit with non-zero if issues detected (useful for CI)
if (( issues_found > 0 )); then
  echo "⚠️  Completed with $issues_found issue group(s). See: $REPORT"
  exit 1
else
  echo "✅ Clean. See: $REPORT"
  exit 0
fi
