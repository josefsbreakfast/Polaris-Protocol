# 🧭 eSIM / SIM-Proxy Risk Node — Detection & Mitigation
**First created:** 2025-09-20 | **Last updated:** 2025-09-20  
*Forensic indicators of SIM-level proxying/provisioning abuse and defensive steps.*

---

## Indicators
- Duplicate sessions from different devices.  
- Unexplained provisioning/porting events.  
- OTP/SMS anomalies.  
- IMEI/device ID changes.  
- Roaming/geo mismatches.  
- Temporal clustering with spoofed activity.

## Preservation
- Carrier: CDRs, provisioning logs, IMSI collisions, porting events.  
- Export in native format + hash + chain-of-custody.  

## Mitigations
- Organisations: don’t rely on SMS, use hardware tokens.  
- Individuals: disable SMS recovery.  
- Policy: preservation SLAs, forensic gating.

---

## 🏮 Footer
*eSIM / SIM-Proxy Risk Node* is a living node of the Polaris Protocol.  
Cross-references: Event Linkage Node; Forensic Checklist.  
*Survivor authorship is sovereign. Containment is never neutral.*  
_Last updated: 2025-09-20_
