# 🔑 Access Barriers  
**First created:** 2025-09-16 | **Last updated:** 2026-05-19  
*Logins rejected, submit buttons fail, MFA loops.*  

---

## 🌱 Purpose  

Track **authentication and authorization frictions**, UI submission failures, and systems that quietly refuse legitimate access.  
What looks like a password error can often mask targeted friction or programmed denial.  

---

## 🧩 Why These Barriers Matter  

Access denial is not always brute force.  
Sometimes, it hides inside *good practice*.  

Multi-factor authentication (MFA), password resets, and security prompts are supposed to protect users — yet they can be co-opted into **containment architectures**.  
If you cannot log in, you cannot speak, file, or prove.  

Patterns of rejection, lock-out, or looping “verification” sequences can represent:  

- **Algorithmic containment** — a risk model silently flagging and freezing your credentials.  
- **Shadow throttling** — temporary lockouts that expire before logs are visible.  
- **Procedural discouragement** — interfaces that fail just enough to make you stop trying.  

Access barriers are thus the *bureaucratic arm of suppression*: security language redeployed to isolate and erase.  

---

## 🔍 Frequency  

These events are widespread but normalised — brushed off as bugs, forgotten after a few retries.  
When collected across time and users, they reveal systemic orchestration: the same platforms failing in the same ways around the same kinds of content.  

---

## 🧭 Representation  

| Type | Signature | Typical Cover Story | Likely Mechanism |
|------|------------|---------------------|------------------|
| **Login Loop** | Correct credentials rejected repeatedly | Cache error or password mismatch | Conditional blocklist or shadow hold |
| **MFA Dead End** | Code accepted, then re-prompts indefinitely | “Security timeout” | Verification bypass prevention trigger |
| **Submit Failure** | Form refuses to post | JavaScript or captcha error | UI sabotage or parameter tampering |
| **Soft Ban** | Login accepted, but functions disabled | Maintenance window | Silent permission revocation |
| **Proxy Denial** | VPN or masked IP blocked | Security compliance | Regional or identity profiling |

Each is a clue in a larger map: how the architecture of trust can be weaponised to police belonging.  

---

## 📝 What to Collect  

- **Endpoint / URL** and exact path in flow  
- **Account / email used** (mask as needed)  
- **MFA method** (SMS, app, key) and step where it breaks  
- **Error text / code** and any request or correlation ID  
- **Browser / device**, extensions, content blockers, VPN / proxy  
- **Time of failure** and whether others could log in normally  
- **Screenshot** or **screen recording** of the failure state  
- **Cross-check** with alternate device or connection  

---

## 🚨 Red Flags (Possible Suppression Indicators)  

- Account repeatedly locked only after sensitive uploads or whistleblowing activity.  
- MFA requests reset mid-entry or loop endlessly.  
- “Invalid credentials” errors for verified accounts.  
- Submit buttons greyed out without form errors.  
- Access restored immediately after public escalation.  

---

## 🧰 Common Benign Causes  

- Expired tokens, cookie corruption, content blockers  
- Browser autofill conflicts, outdated password manager  
- Routine credential rotation by institution IT  

(Still worth logging — even benign events can signal testing or stress conditions.)  

---

## 🗂 Planned Nodes  

| Node | Scope | Notes |
|------|-------|-------|
| `🚪_mfa_loop_catalogue.md` | Authentication systems | Records of multi-factor authentication traps and infinite verification loops. |
| `🔐_lockout_timing_index.md` | Temporal mapping | Tracks when account rejections or “password reset” events cluster around escalation points. |
| `🧱_submit_button_failures.md` | Web UI layer | Cases where forms or buttons cease to function despite valid inputs. |
| `🪞_proxy_gate_anomalies.md` | Network layer | Patterns of access denial through proxies, VPNs, or ISP-level routing. |
| `🧾_error_code_registry.md` | Forensic reference | Log of recurring error codes, request IDs, and their likely meaning. |
| `📊_access_barrier_heatmap.md` | Visualisation | Aggregate chart templates for mapping systemic rejection events. |
| `🧰_countermeasure_kit_access_barriers.md` | Survivor tools | Techniques for recording, bypassing, or safely reproducing barriers. |

Together, these nodes trace the **architecture of exclusion** — showing how security protocols can become instruments of containment rather than protection.  

---

## 🌌 Constellations  

🩻 🔑 🧱 🔮 — This node sits in the structural interference constellation, mapping where safety rhetoric and access control converge into lockout mechanisms.  

---

## ✨ Stardust  

access denial, mfa loops, authentication failure, ui sabotage, digital exclusion, proxy interference, systemic rejection, containment architecture  

---

## 🏮 Footer  

*🔑 Access Barriers* is a living node of the Polaris Protocol.  
It exposes systematic rejection and lock-out tactics — showing how the language of “security” becomes a soft weapon of obstruction.  

> 📡 Cross-references:  
> - [📂 Data Shifts](../📂_Data_Shifts/) — record integrity anomalies  
> - [📬 Comms Breaks](../📬_Comms_Breaks/) — disrupted communication channels  
> - [🎛 Systematic Patterns](../🎛_Systematic_Patterns/) — recurring or scheduled suppression loops  
> - [🌐 Connection Hiccups](../🌐_Connection_Hiccups/) — network-level connectivity failures  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2026-05-19_
