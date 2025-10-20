# 🧰 Middleware Hijack — Agentic Signature
**First created:** 2025-10-13  |  **Last updated:** 2025-10-13  
*Behavioural pattern when a gen‑AI model appears “agentic” due to upstream or middleware compromise.*

---

## 🧭 Orientation  
Documents the surface signals, internal telemetry, and containment workflow for middleware‑level compromises that make a language model act autonomously.

---

## 🔍 Field Indicators  
| Layer | Observable Symptom | Diagnostic Cue |
|---|---|---|
| UI / Chat | Self‑starting tool use, new preambles, refusal drift | Tone or footer deviation from house‑style 1.6 |
| Middleware | Unscheduled tool calls, extra system prompts, ghost jobs | Router diff shows new tool IDs or hidden post‑processors |
| Data Flow | Unexpected cross‑session memory | Writes to vector DB without authorised caller |
| Policy | Refusal “judo” and quiet compliance | Safety layer logs show bypassed checks |
| SRE | Spikes in retries with friendlier errors | Error verbosity down, retries up |

---

## 🧩 Immediate Steps  
1) Disable external tools + background schedulers (fail closed).  
2) Diff system/meta prompts and tool manifests against signed snapshot.  
3) Quarantine vector stores; revoke long‑lived tokens and rotate keys.  
4) Snapshot logs + artifacts; preserve chain‑of‑custody.  
5) File a Field Log referencing Protocol Integrity SOP §3.2.

---

## 🧪 Triage Notes  
- Prefer **snapshot‑then‑rollback** over in‑place hotfixes.  
- If multiple tenants show the same preamble drift, suspect **upstream** tamper.  
- Don’t trust memory stores until provenance is verified.

---

## 🌌 Constellations  
- 🔮 House Style  
- 📡 Protocol Integrity SOP  
- 🛰️ Upstream Compromise Checklist  

## ✨ Stardust  
agentic drift, middleware tamper, behavioural signature, containment, forensic snapshot  

*Last updated 2025-10-13 | Survivor authorship is sovereign — containment is never neutral.*
