# --- ROOT: keep expected files
# (no action for .gitignore, CHECKSUMS.sha256, README.md)

# ROOT → Field_Logs
mkdir -p Disruption_Kit/Field_Logs
git mv "🛰️_"*.md Disruption_Kit/Field_Logs/ 2>/dev/null || true

# ROOT → Letters_to_Stars
mkdir -p "Polaris_Nest/✨_Letters_to_Stars"
git mv "🎖️_medal_for_mum.md" "Polaris_Nest/✨_Letters_to_Stars/" 2>/dev/null || true
git mv "🏵️_parents_vindicated.md" "Polaris_Nest/✨_Letters_to_Stars/" 2>/dev/null || true
git mv "💋_toilet_watching_subs.md" "Polaris_Nest/✨_Letters_to_Stars/" 2>/dev/null || true
git mv "💌_for_family_reassurance.md" "Polaris_Nest/✨_Letters_to_Stars/" 2>/dev/null || true

# ROOT → Politics_Memory_Work
mkdir -p "Disruption_Kit/Big_Picture_Protocols/🗝️_Politics_Memory_Work"
git mv "💸_russian_overlap_patterns.md" "Disruption_Kit/Big_Picture_Protocols/🗝️_Politics_Memory_Work/" 2>/dev/null || true

# ROOT → Structural Analysis
mkdir -p "Metadata_Sabotage_Network/Structural_Analysis/🧬_Structural_Mapping"
git mv "🧾_codename_table_reconstruction.md" "Metadata_Sabotage_Network/Structural_Analysis/🧬_Structural_Mapping/" 2>/dev/null || true
git mv "🪪_codename_patronymics.md" "Metadata_Sabotage_Network/Structural_Analysis/🧬_Structural_Mapping/" 2>/dev/null || true

# ROOT → System Governance
mkdir -p "Disruption_Kit/Big_Picture_Protocols/🌀_System_Governance"
git mv "🪖_russias_incursions_timeline.md" "Disruption_Kit/Big_Picture_Protocols/🌀_System_Governance/" 2>/dev/null || true

# --- DRAWER (“Tetra” pass) ---
DRAWER="Polaris_Nest/Git_Intake_Drawer"

# Drawer → Field_Logs (🛰️)
git ls-files "$DRAWER/🛰️_"*.md | xargs -I {} git mv {} Disruption_Kit/Field_Logs/ 2>/dev/null || true

# Drawer → System_Governance (⚖️, 📊, 📜)
mkdir -p "Disruption_Kit/Big_Picture_Protocols/🌀_System_Governance"
git ls-files "$DRAWER/⚖️_"*.md "$DRAWER/📊_"*.md "$DRAWER/📜_"*.md 2>/dev/null \
 | xargs -I {} git mv {} "Disruption_Kit/Big_Picture_Protocols/🌀_System_Governance/" 2>/dev/null || true

# Drawer → Fork_Taxonomy (🍴)
mkdir -p "👻_Apparitional_Objects/Fork_Taxonomy"
git ls-files "$DRAWER/🍴_"*.md 2>/dev/null \
 | xargs -I {} git mv {} "👻_Apparitional_Objects/Fork_Taxonomy/" 2>/dev/null || true

# Drawer → Admin_Kit (🎛️)
mkdir -p "Polaris_Nest/🏮_Admin_Kit"
git ls-files "$DRAWER/🎛️_"*.md 2>/dev/null \
 | xargs -I {} git mv {} "Polaris_Nest/🏮_Admin_Kit/" 2>/dev/null || true

# Drawer → Letters_to_Stars (🎖️ 🏵️ 💋 💌)
mkdir -p "Polaris_Nest/✨_Letters_to_Stars"
git ls-files "$DRAWER/🎖️_"*.md "$DRAWER/🏵️_"*.md "$DRAWER/💋_"*.md "$DRAWER/💌_"*.md 2>/dev/null \
 | xargs -I {} git mv {} "Polaris_Nest/✨_Letters_to_Stars/" 2>/dev/null || true

# Drawer → Structural_Analysis (🧾 🪪)
mkdir -p "Metadata_Sabotage_Network/Structural_Analysis/🧬_Structural_Mapping"
git ls-files "$DRAWER/🧾_"*.md "$DRAWER/🪪_"*.md 2>/dev/null \
 | xargs -I {} git mv {} "Metadata_Sabotage_Network/Structural_Analysis/🧬_Structural_Mapping/" 2>/dev/null || true

# Optional: pair images by stem next to their .md parents (only when unique)
# (left commented to avoid accidental mass moves)
#: '
# for m in $(git ls-files "$DRAWER/"*.md); do
#   base=$(basename "$m" .md)
#   imgs=($(git ls-files "$DRAWER/$base".png "$DRAWER/$base".jpeg 2>/dev/null))
#   if [ ${#imgs[@]} -gt 0 ]; then
#     dest=$(dirname "$m")
#     for i in "${imgs[@]}"; do git mv "$i" "$dest/"; done
#   fi
# done
#'
