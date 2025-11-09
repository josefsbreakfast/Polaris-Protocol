# 🔊 Signal Integrity Quick Protocol  
**Purpose:** Protect and verify authentic human voice recordings against cloning, remix, or metadata sabotage.  
**Source Node:** [🔊 Signal Integrity Protocols — Protecting the Sound of the Voice](./🔊_signal_integrity_protocols_protecting_the_sound_of_the_voice.md)

---

## 1️⃣ Capture Safely  
- Record in a private, verified space.  
- Immediately **hash** the file (`shasum -a 256 <file>`).  
- Note date, device, and context in a short YAML or text manifest.  
→ *Goal:* fix the moment of authorship before edits or uploads occur.

---

## 2️⃣ Embed an Acoustic Trace  
- Use **Audiowmark** or equivalent to add a hidden watermark.  
- Keep the private key offline; share only verification outputs.  
→ *Goal:* your voice can later prove itself genuine without revealing extra data.

---

## 3️⃣ Register a Voiceprint Hash  
- Derive a **non-reversible spectral hash** (formant + pitch signature).  
- Store this hash, not the audio, in a secure ledger.  
→ *Goal:* clones can be disproven by mismatch without exposing content.

---

## 4️⃣ Maintain an Integrity Chain  
| Step | Action | Tool |
|------|---------|------|
| 1 | Capture → hash → timestamp | `ffmpeg`, `openssl` |
| 2 | Encrypt → store → verify | `gpg`, `git lfs` |
| 3 | Publish with manifest | signed `.yaml` or `.csv` |

→ *Goal:* any later deviation exposes tampering or re-encoding.

---

## 5️⃣ Detect Sabotage  
Watch for:  
- Timestamp drift / timezone mismatch  
- Codec or bit-depth changes  
- Smoothed or “cleaned” spectrograms  
- Odd silences or truncated breaths  
→ *Goal:* map the anomaly pattern, not just the clip.

---

## 6️⃣ Verify & Respond  
When a suspect clip appears:  
1. Compare its hash to your ledger.  
2. Check for missing watermark or spectral mismatch.  
3. Log findings in your evidence index.  
4. Publish a short signed statement confirming or refuting authenticity.  
→ *Goal:* control the narrative before misinformation settles.

---

## 🧾 Minimal Manifest Example  

```yaml
voice_id: V-2025-0013
file_name: testimony.wav
hash_sha256: "<checksum>"
recorded_at: "2025-11-09T14:30:00Z"
authored_by: "Witness A"
consent_scope: "public excerpt only"
signature: "<PGP signature>"
notes: "Watermark verified; no anomalies."
```

---

## 🪞 Quick Ethic  
Authenticity ≠ exposure.  
Proof of voice should never require surrender of privacy.  
Verification is an act of **sovereignty**, not compliance.

---

_Last updated: 2025-11-09_
