# 🪐 Verifying App Encryption & Privacy Claims
**First created:** 2025-10-17 | **Last updated:** 2025-10-17  
*A survivor-safe technical guide to reading what “encrypted” actually means.*

---

## 🛰️ Orientation  
This node teaches how to *validate* encryption and privacy claims — the quiet line between “marketing security” and real protection.  
It explains the difference between **code-level**, **transport-level**, and **metadata-level** secrecy, and gives low-risk methods for checking each without advanced tooling.

---

## 🧩 Key Layers of Encryption  

| Layer | Who Can Read the Data | Example | Risk Notes |
|-------|-----------------------|----------|-------------|
| **End-to-End (E2E)** | Only sender & receiver. | Signal, iMessage (Apple-to-Apple). | Strongest form; even company servers can’t read content. |
| **Transport-Layer (TLS)** | You + the service provider. | Gmail, Facebook Messenger default mode. | Protects data in transit but not on the server. |
| **At-Rest Encryption** | Company encrypts stored data. | iCloud, Dropbox. | Data safe from theft but still readable by the provider. |
| **Tokenised / Differential Privacy** | Aggregated or obfuscated data. | Apple Health, Google Maps (some modes). | Protects from casual leaks, not deep profiling. |

---

## 🔍 Step-by-Step: Verifying Claims  

1. **Check Privacy Label (Storefront Clues)**  
   - App Store → “App Privacy” / Play Store → “Data Safety.”  
   - “Data not linked to you” = minimal profiling.  
   - “Data used to track you” = commercial profiling.

2. **Search Developer’s Site**  
   - “Open source,” “Security audit,” or “Zero-knowledge encryption” = good.  
   - “Proprietary encryption” with no audit → assume marketing only.

3. **Confirm Independent Security Audits**  
   - Look for public audit PDFs (Cure53, Trail of Bits, NCC Group).  
   - If none found → assume *not verified yet.*

4. **Network Traffic Check (Optional)**  
   - Tools: Lockdown Privacy (iOS), NetGuard (Android).  
   - If app contacts dozens of unknown domains → leaking data.

5. **Check Permissions vs Promises**  
   - Encrypted chat apps shouldn’t request call logs, SMS, or screen access.  
   - If they do → harvesting beyond stated purpose.

---

## 🧮 Optional Deeper Tools  

| Tool | Platform | Purpose |
|------|-----------|----------|
| Lockdown Privacy / NetGuard | iOS / Android | See outbound data connections. |
| Exodus Privacy | Android | Lists trackers and permissions. |
| AppCensus Reports | Web | Public data on app tracking. |
| PrivacyGuides.org | Web | Trusted privacy app recommendations. |

---

## 🌌 Constellations  
🔐 🛰️ 🧠 💡 — forensic literacy, survivor digital safety, encryption verification.

---

## ✨ Stardust  
encryption, verification, open source, security audits, coercive control, privacy literacy, metadata, data safety, survivor tools

---

## 🏮 Footer  
*🔐 Verifying App Encryption & Privacy Claims* is a living node of the Polaris Protocol.  
It offers a technically grounded yet survivor-accessible method to distinguish real encryption from marketing claims, and to identify dual-use surveillance disguised as safety.  

> 📡 Cross-references:  
> - [📱 App Security Basics for Survivors](./📱_app_security_basics_for_survivors.md) — everyday check companion  
> - [Survivor Tools](../) — practical countermeasures  
> - [🧿 Watch The Watchers](../../Big_Picture_Protocols/🧿_Watch_The_Watchers/) — systemic surveillance analysis  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-10-17_
