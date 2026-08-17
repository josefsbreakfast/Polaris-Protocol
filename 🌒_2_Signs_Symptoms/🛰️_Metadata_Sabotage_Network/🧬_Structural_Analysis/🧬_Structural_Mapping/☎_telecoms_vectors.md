# 📡 Telecoms Vectors — Index  
**Folder:** Metadata_Sabotage_Network/📡_telecoms_vectors/  
**Purpose:** a living index for telco-level forensic vectors, provisioning abuse, and SIM/IMEI/CDR threats.

---

## About this folder
This folder collects forensic nodes, mitigation notes, and investigative playbooks related to telecommunication-level metadata exploitation: SIM/eSIM abuse, IMSI-catchers, CDR manipulation, signalling layer (SS7/SIGTRAN) attacks, lawful-intercept backdoors, and associated forensic artefacts. Use this index to find existing nodes and to sketch future work.

**Keep in mind:** many of these nodes may intersect with legal or libel-sensitive material. Flag anything naming organisations or individuals for legal review before public release.

---

## Current contents
- 🧭 _esim_proxy_risk.md — eSIM / SIM-Proxy Risk Node — Detection & Mitigation (forensic indicators + preservation + mitigations)

---

## Suggested future nodes (titles + short description)
Use these as prompts or placeholders when you want to create a new node.

1. **SS7_SIGTRAN_Exploits.md** — catalogue of known signalling-layer attacks, indicators in carrier logs, and forensic traces to request from telcos.  
2. **IMSI_Catcher_Detection.md** — field-detection checklist (RF signatures, temporal clustering, device-side heuristics) and safe-evidence capture.  
3. **CDR_Manipulation_Fingerprint.md** — how to spot altered call-detail records, timestamps/sequence anomalies, and chain-of-custody patterns.  
4. **IMEI_Spoofing_and_Device_Abuse.md** — patterns of IMEI collisions, provisioning anomalies, and device-identification laundering.  
5. **Lawful_Intercept_Backdoors.md** — taxonomy of intercept mechanisms (legal vs covert), governance red flags, and evidence preservation steps.  
6. **Porting_and_Provisioning_Abuse.md** — forensic timeline for SIM port-outs, emergency porting abuse, and telco responses.  
7. **Carrier_Forensics_Request_Templates.md** — pre-built templates (what to ask for: CDRs, provisioning logs, IMSI history, HLRS/MSC traces) and legal language for preservation.  
8. **OTA_Provisioning_Abuse.md** — over-the-air provisioning (eSIM/OTA) attack patterns, indicators in MNO logs, rollback/provision states.  
9. **SS7_Sigtran_Mitigation_Best_Practices.md** — recommended telco-level mitigations, attestations, and monitoring telemetry.  
10. **Proxying_and_Session_Anomaly_Alerts.md** — SIEM-ready rules and heuristics for detecting duplicate session/proxy behaviours.  

---

## Filing and tagging conventions (recommended)
- Filename prefix: emoji tag for quick scanning (📡 for telecoms).  
- Frontmatter (optional) for each node:

```
title: “Short Title”
created: 2025-09-26
last_updated: 2025-09-26
tags: [telecoms, forensic, esim, ss7, imei]
classification: internal
```

- Add cross-reference links to other Metadata_Sabotage_Network nodes and to Disruption_Kit/Forensic_Checklist where relevant.

---

## How to add a new node (copy/paste template)
```markdown
# <Emoji> Short Title  
**First created:** YYYY-MM-DD | **Last updated:** YYYY-MM-DD  
*One-line summary of the node.*

---

## Indicators
- ...

## Preservation
- ...

## Mitigations / Investigative steps
- ...

```

---

## 🏮 Footer
*This node is a living part of the Polaris Protocol.*  
> 📡 Cross-references:  
> - ../Forensic_Checklist.md  
> - ../Event_Linkage.md

_Last updated: YYYY-MM-DD_
