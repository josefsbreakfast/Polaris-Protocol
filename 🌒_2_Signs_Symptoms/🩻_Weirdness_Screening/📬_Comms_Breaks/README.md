# 📬 Comms Breaks  
**First created:** 2025-09-16 | **Last updated:** 2026-05-19  
*Messages delayed, attachments lost, calls/messages dropped mid-conversation.*  

---

## 🌱 Purpose  

Capture **breakdowns in communication channels** — email, chat apps, calls, or messaging platforms — and distinguish routine outages from *patterned suppression*.  
A single failed message may be trivial; repetition across time or topic becomes a signature.  

---

## 🧩 Why These Breaks Matter  

Containment often doesn’t look like censorship.  
It looks like silence arriving *just in time*.  

Communication failures can act as **soft disconnections**: the system seems intact, but specific exchanges vanish, delay, or distort at pivotal moments.  
Unlike overt censorship, comms breaks maintain *plausible deniability* — both sender and recipient believe it was just a glitch.  

### Common contexts  

- **Escalation or exposure points:** messages containing evidence, whistleblowing, or survivor coordination drop mid-thread.  
- **Critical timing:** attachments “fail to send” precisely when events go public or legal filings are due.  
- **Containment by fatigue:** repeated breaks make users internalise failure, self-silencing before the system even intervenes.  

Tracking these patterns allows us to see **disruption as choreography** — not a malfunction, but a method.  

### Frequency  

Comms breaks are among the most frequently reported weirdness phenomena in the Polaris field logs.  
They appear across multiple apps and devices, often clustering around **sensitive content or contacts**.  
On their own, they read as technical faults; in aggregate, they trace the outline of suppression infrastructure.  

### Representation  

There are several “species” of comms break:  

| Type | Signature | Typical Cover | Underlying Logic |
|------|------------|---------------|------------------|
| **Silent Drop** | Message shows as delivered but never received | Server lag or device cache | Selective filtering by content or metadata match |
| **Attachment Strip** | File removed while message text remains | Size limit, corruption | Active sanitisation by platform scanning or proxy |
| **Mid-Call Cut** | Call ends abruptly, usually after key phrase | “Poor connection” | Keyword or packet-level trigger |
| **Loopback Lag** | Replies delayed or re-ordered | Network congestion | Queue manipulation to break conversational flow |
| **Phantom Receipt** | You see “read” or “played” status that user denies | Sync bug | False confirmation masking interception |

---

## 📝 What to Collect  

- **Channel/service:** Gmail, Signal, WhatsApp, Zoom, etc.  
- **Device/OS + app version**  
- **Message/call type:** text, voice, video, attachment  
- **Timestamp sent vs received vs observed**  
- **Delivery receipts / status codes**  
- **Screenshots of missing or stripped content**  
- **Cross-check with sender/recipient logs**  
- **Correlated context:** what the message was about, what else was happening at that time  

---

## 🔍 Quick Triage  

- ✅ Confirm sender actually sent the file/message.  
- ✅ Test alternate network or device.  
- ✅ Re-send via different channel (e.g., email → Signal).  
- ✅ Compare timestamps vs server logs.  

If the break repeats around similar topics or contacts, treat it as **patterned suppression**, not coincidence.  

---

## 📦 Evidence to Save  

- Screenshots, email headers, chat exports, voicemail files  
- Delivery failure notifications or bounce codes  
- Any local logs from apps (JSON, XML, or CSV formats)  
- Cross-device screenshots showing divergent histories  

---

## 🚩 Red Flags (Possible Interference)  

- Attachments consistently stripped when related to sensitive topics.  
- Calls/messages cut off during key phrases or events.  
- “Delivered” or “Read” status shown but recipient never receives.  
- One-way ghosting — your messages vanish from your outbox but remain cached in server backups.  

---

## ⚙️ Common Benign Causes  

- Email size limits, mobile carrier congestion  
- App update incompatibility, corrupted cache  
- Outdated certificates or expired login sessions  

(Still record them — repeated benign failures can mask targeted ones.)  

---

## 🧾 Minimal Record Schema (YAML front-matter)  

```yaml
when: 2025-09-16T15:42:00Z
service: "WhatsApp"
device: "iPhone 14, iOS 17.5"
symptom: "Voice note shows 'delivered' but never arrives"
error: null
artifacts: [screenshot.png, chat_export.zip]
repro: {wifi: true, mobile_data: true}
notes: "Attachment arrives if resent via Signal"
```

## 🗂 Planned Nodes  

| Node | Scope | Notes |
|------|-------|-------|
| `📞_cut_signal_casebook.md` | Voice + video | Catalogue of mid-call drops and cut-phrase timing. |
| `📎_attachment_strip_registry.md` | Messaging | Logs of missing or corrupted attachments by platform. |
| `📡_phantom_receipt_index.md` | Verification layer | Tracks false delivery/read receipts. |
| `🪩_cross_device_divergence.md` | Sync drift | Compare message histories across linked devices. |
| `🧰_triage_kit_comms_breaks.md` | Survivor tool | Standard scripts + checklists for testing interference. |

Together, these nodes transform isolated silences into a **coherent diagnostic language** — making the invisible choreography visible.  

---

## 🌌 Constellations  

🩻 📬 🛰️ 🔮 — This node sits in the interference and containment constellation, where communication failure becomes an evidentiary signal.

---

## ✨ Stardust  

communication failure, message loss, attachment stripping, selective silence, interference logging, metadata anomalies, suppression evidence, digital containment  

---

## 🏮 Footer  

*📬 Comms Breaks* is a living node of the Polaris Protocol.  
It records interruptions in digital conversation flows — where the connection appears whole but content quietly fails.  

> 📡 Cross-references:  
> - [🌐 Connection Hiccups](../🌐_Connection_Hiccups/) — network-level dropouts  
> - [📂 Data Shifts](../📂_Data_Shifts/) — record-level drift and disappearance  
> - [🎛 Systematic Patterns](../🎛_Systematic_Patterns/) — scheduled or repeated anomalies  
> - [Field Logs](../../Disruption_Kit/Field_Logs/) — forensic documentation of anomaly timelines  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2026-05-19_
