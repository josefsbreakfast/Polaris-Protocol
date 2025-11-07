# 🗣️ How to Detect if Your Voice Has Been Used in a Dataset  
**First created:** 2025-11-07 | **Last updated:** 2025-11-07  
*Practical guidance for identifying, evidencing, and documenting potential misuse of your voice in text-to-speech or R&D datasets.*

---

## 🧭 Orientation  

When your voice appears in synthetic speech or datasets without consent, proof is rarely straightforward.  
This node offers forensic, legal, and procedural paths to **detect, evidence, and log** possible misuse — even when datasets are proprietary, distributed, or automated.  
It is part of the *Cloneproof* constellation within the Survivor Tools cluster.

---

## 🧩 Key Features  

- Practical steps to detect voice cloning or dataset reuse.  
- Forensic + legal approaches (technical and administrative).  
- Template Subject Access Request (SAR) language.  
- Evidence logging sheet for survivor-led verification.  

---

## 🔍 Analysis  

### 1. **Forensic Detection (Technical Route)**  

| Method | What it Does | What You Need | Limits |
|--------|---------------|---------------|--------|
| **Spectral / fingerprint comparison** | Compares voiceprint patterns (formants, pitch, rhythm) with suspect samples. | Access to the audio you suspect + clean reference recordings of your own voice. | Needs forensic linguist or ML tools (e.g., ECAPA-TDNN, ASVSpoof). |
| **Embedding similarity tests** | Quantifies how close two voices are in ML space. | An analyst who can extract embeddings. | Only indicative — not court proof alone. |
| **Watermark search** | Detects inaudible markers in synthetic voices. | Specialist tools. | Few datasets actually watermark. |

If you believe a synthetic voice resembles yours, keep **the output audio, transcript, and URL or API record** as evidence.  
You do *not* need to prove intent — only that data similarity exists.

---

### 2. **Legal Rights (UK + EU Context)**  

Your voice counts as **biometric data** under the *UK GDPR* and *Data Protection Act 2018* when used for identification or modelling.  
You may therefore:

#### 🔎 Make a Subject Access Request (SAR)
Send to any organisation that may hold your data (universities, AI firms, insurers, contractors).  
Request confirmation of:

- whether they process *audio, biometric, or voice data* relating to you;  
- the **source** of any such data;  
- whether it has been used for *training, testing, or synthesis*;  
- the **recipients** of that data; and  
- any **automated decision-making** involving your voice.

#### 🗑️ Request Erasure or Restriction
If processing lacks lawful basis or explicit consent, request deletion or restriction of your voice data.  
Refusals (e.g., “research exemption”) should be logged as evidence of probable reuse.

#### 🧾 Example SAR Language

> **Subject Access Request: Audio / Biometric Data**  
> I am making a Subject Access Request under Article 15 UK GDPR.  
> Please confirm whether you process any audio, speech, or biometric data relating to me, and if so:  
> - The source of that data,  
> - The purpose and lawful basis for processing,  
> - Whether it has been used for text-to-speech, voice synthesis, or R&D model training,  
> - The recipients or categories of recipients of that data,  
> - Whether any automated decision-making has been performed using it, and  
> - The retention period or deletion schedule.  
> Please supply copies of any data, metadata, and processing records under the Right of Access.

---

### 3. **Indirect Indicators**

- A synthetic voice reproduces your accent, cadence, or habitual phrases.  
- Dataset indices, model cards, or research papers list your **institution, region, or recording context**.  
- You once participated in research, telehealth, or customer-service calls linked to dataset suppliers.  
- Your **metadata or transcripts** appear in public repositories (e.g., “Common Voice”, “AudioSet”, or sub-licensed academic corpora).  
- You notice **matching artefacts** (microphone hiss, room echo) identical to recordings you made.

None of these prove direct inclusion, but together they justify formal enquiries.

---

### 4. **Evidence-Logging Template**

| Date | Source / Event | Type (Audio, Transcript, Metadata) | Retained Proof | Notes |
|------|-----------------|------------------------------------|----------------|-------|
| YYYY-MM-DD | e.g. Website demo voice | Audio sample (MP3) | Saved file, screenshot | Spectral similarity to my voice |

Keep this log in encrypted storage; use hashes or timestamps to preserve integrity.  
If evidence escalates, consult a digital forensics expert or solicitor specialising in data rights.

---

## 🌌 Constellations  

🧿 🧬 ⚖️ 🛰️ — Survivor tools; biometric autonomy; legal recourse; digital forensics.

---

## ✨ Stardust  

voice cloning, text-to-speech, SAR template, biometric data, forensic linguistics, data rights, dataset reuse, evidence logging, survivor tools, AI accountability  

---

## 🏮 Footer  

*🗣️ How to Detect if Your Voice Has Been Used in a Dataset* is a living node of the Polaris Protocol.  
It provides survivor-led technical and legal methods to verify potential voice misuse in AI training or R&D contexts.  

> 📡 Cross-references:  
> - [🧬 Cloneproof](../Survivor_Tools/🧬_cloneproof.md) — countermeasures against likeness and behavioural cloning  
> - [⚖️ Containment Contract Trace](../Big_Picture_Protocols/⚖️_containment_contract_trace.md) — how layered contracts obscure accountability  
> - [🎛️ Polaris Drafting Rules — Survivor Voice Fidelity](../Admin_Kit/🎛️_polaris_drafting_rules_survivor_voice_fidelity.md) — undertone and forensic clarity in testimony  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-11-07_
