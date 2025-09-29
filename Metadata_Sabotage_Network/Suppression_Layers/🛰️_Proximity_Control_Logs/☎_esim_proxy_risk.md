# ☎ eSIM / SIM-Proxy Risk Node — Detection & Mitigation  
**First created:** 2025-09-20 | **Last updated:** 2025-09-29  
*Forensic indicators of SIM-level proxying/provisioning abuse and defensive steps.*

---

## Indicators  
- Duplicate sessions emerging from different devices.  
- Unexplained provisioning or porting events.  
- OTP / SMS anomalies.  
- IMEI or device ID changes.  
- Roaming or geo-location mismatches.  
- Temporal clustering aligned with spoofed activity.  

---

## Preservation  
- **Carrier level** — collect CDRs, provisioning logs, IMSI collisions, porting events.  
- **Method** — export in native format, apply cryptographic hash, maintain full chain-of-custody.  

---

## Mitigations  
- **Organisations** — avoid SMS as a security channel; use hardware tokens or app-based MFA.  
- **Individuals** — disable SMS-based account recovery.  
- **Policy / Governance** — preservation SLAs, forensic gating for telco-level evidence.  

---

## 🏮 Footer  

*eSIM / SIM-Proxy Risk Node* is a living node of the Polaris Protocol.  

> 📡 Cross-references:  
> - [Event Linkage Node](../Metadata_Sabotage_Network/Event_Linkage.md)  
> - [Forensic Checklist](../Metadata_Sabotage_Network/Forensic_Checklist.md)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-09-29_
