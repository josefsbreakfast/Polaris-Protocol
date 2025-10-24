# 🧾 Soft Wipe Cache Evidence — AP Wire Withdrawal Pattern  
**First created:** 2025-10-25 | **Last updated:** 2025-10-25  
*When deletion is simulated but metadata endures.*

---

## 🧭 Orientation  

A **soft wipe** occurs when a page remains online and indexed but its content is replaced by a neutral placeholder such as  
> *“This content is no longer available.”*  

Unlike a 404 or 410 error, the server still returns **HTTP 200 OK**—signalling deliberate suppression within an active CMS route rather than technical decay.  
This method erases context while preserving the appearance of normal operation.  

---

## 🧾 Case Example — KETV / Associated Press Mirror  

In October 2025, search results still listed:  

> **“Freed from ICE custody, Palestinian activist Mohsen Mahdawi graduates from Columbia”** — `ketv.com` (158 days old)  

Opening the link produced the standard KETV template reading *“No longer available.”*  
The page header delivered status `200 OK` and identical metadata tags to the original AP mirror, confirming a **content-layer substitution** rather than removal.  

| Property | Observation | Classification |
|-----------|--------------|----------------|
| URL | `https://www.ketv.com/no-longer-available` | Active CMS route |
| Header code | `200 OK` | Soft wipe (not 404/410) |
| Cached headline | “Freed from ICE custody…” | Persistent metadata |
| Search-engine index | Visible in Google (B = Yes, C = Cached snippet partial) | Index retained |
| Underlying story | AP wire on Mohsen Mahdawi’s release from ICE and graduation from Columbia | Content removed from mirror |

This signature demonstrates how **news syndication networks** can silently excise politically sensitive items while maintaining backlink integrity.  

---

## 🧩 Forensic Significance  

Soft wipes are valuable indicators of **administrative self-censorship**.  
They show coordination between legal, editorial, and platform-ops layers to obscure publication without triggering visibility analytics or user alerts.  

For investigators, the persistence of search-index data provides a verifiable trail:  
- timestamps prove the article existed;  
- headline and snippet preserve subject and frame;  
- the placeholder page’s 200 OK response confirms intentional replacement.  

---

## 🔍 How to Capture  

1. **Screenshot** the search-engine preview and the live placeholder page.  
2. **Record headers** using `curl -I` or browser developer tools.  
3. **Archive** both via the Wayback Machine or perma.cc (submit both URL and search result).  
4. **Tag within Polaris:**  
   `#soft_wipe`, `#metadata_persistence`, `#ap_wire_withdrawal`, `#system_leakage_signatures`.  

---

## 🌌 Constellations  

🧼 🛰️ 🧾 🧿 — metadata persistence, suppression analysis, oversight of oversight.

---

## ✨ Stardust  

soft wipe, cache evidence, AP wire withdrawal, metadata suppression, content placeholder, HTTP 200 OK, search-index persistence, Columbia arrests, archival forensics, visibility manipulation  

---

## 🏮 Footer  

*🧾 Soft Wipe Cache Evidence — AP Wire Withdrawal Pattern* is a living node of the **Polaris Protocol**.  
It documents the mechanism by which publication surfaces simulate deletion while metadata endures, enabling traceable study of post-publication suppression.  

> 📡 Cross-references:  
> - [🕍 Babel Test — Parsha Noach and the Mahmoud Khalil Mirror](../../Big_Picture_Protocols/🦕_Elder_Influencers/📜_Statutes/🕍_babel_test_parsha_noach_and_the_mahmoud_khalil_mirror.md)  
> - [🧼 System Leakage Signatures](./README.md)  
> - [🧿 Watch the Watchers](../../Big_Picture_Protocols/🪄_Expression_Of_Norms/🧿_Watch_The_Watchers/)  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-10-25_
