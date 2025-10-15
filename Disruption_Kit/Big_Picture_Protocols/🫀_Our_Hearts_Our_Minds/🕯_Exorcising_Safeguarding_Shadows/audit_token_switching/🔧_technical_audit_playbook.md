# 🔧 Technical Audit Playbook: Token Switching  
**First created:** 2025-09-30 | **Last updated:** 2025-10-15  
*For sysadmins, forensic analysts, and SIEM operators.*  

---

## Step 1: Preserve evidence  
- Export identity-provider database (ID → attributes) for the last 30–90 days.  
- Export message-bus, application, and dispatcher logs covering the suspect window.  
- Copy checksums or provenance files (e.g. `CHECKSUMS.sha256`) and lock them.  
- Record chain-of-custody (who exported what, when, from which host).  

---

## Step 2: Run crosswalk checks  

### A. Canonical ID diffs (SQL)  
```sql
SELECT subject_id, COUNT(DISTINCT device_id) AS devices
FROM identity_device_map
GROUP BY subject_id
HAVING COUNT(DISTINCT device_id) > 1;
```

### B. Check for reassignments (grep + jq)  
```bash
zgrep -a '"reassign"' /var/log/*.gz
```

### C. Duplicate telemetry (Splunk/Elastic)  
```text
subject_id:(A OR B) | stats count by device_mac, location, subject_id | where count > 1
```

---

## Step 3: Analyse anomalies  
- One-to-many or many-to-one mappings.  
- Identical telemetry for different IDs.  
- Off-hours privileged changes.  
- Divergent signatures (hash mismatch vs owner).  

---

## Step 4: Report findings  
Use the [📑 Forensic Report Template](./📑_forensic_report_template.md).  
Do not alter source records until the report is complete.  

---

## 🏮 Footer  

*Technical Audit Playbook: Token Switching* is a protocol node of the Polaris Protocol.  
It provides a reproducible process for forensic verification of identity-token manipulation.  

> 📡 Cross-references:
> 
> - [📑 Forensic Report Template](./📑_forensic_report_template.md)  
> - [🧬 Twinning Detection](../🧬_twinning_detection.md)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-10-15_  
