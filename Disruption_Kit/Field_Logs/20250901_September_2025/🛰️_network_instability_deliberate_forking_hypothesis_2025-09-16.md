# 🛰️ Network Instability & Deliberate Forking Hypothesis — Field Log  
**First created:** 2025-09-16 | **Last updated:** 2025-09-27  
*Field log capturing app crashes, lag, and VPN-based mitigation; testing whether instability is engineered rather than incidental.*  

---

## 🔎 Observations  
- Multiple inference failures across app sessions.  
- Significant lag; repeated crashes.  
- No improvement when switching **Wi-Fi ⇄ 5G**.  
- **VPN use restored stability.**  
- Suggests mid-path shaping or interference rather than local fault.  

---

## 🧠 Hypotheses  
1. **ISP throttling / shaping** — targeted degradation of specific ports or ASNs.  
2. **Middlebox DPI** — packet resets via deep inspection.  
3. **Transit routing fault** — VPN bypass makes this less likely.  
4. **Service-side throttling** — possible, but cross-device consistency points network.  
5. **Deliberate disruption** — forked reliability as a suppression technique.  

---

## 🧪 Suggested Tests  
- `ping` + `mtr` baseline vs VPN.  
- `traceroute` with and without VPN.  
- DNS comparison (ISP vs 1.1.1.1 / 8.8.8.8).  
- Collect `tcpdump` for RST floods or resets.  
- Log timestamps, devices, OS versions.  

---

## ✦ Stardust — Related Tags & Signals  
- network instability, deliberate forking  
- VPN restores stability  
- ISP shaping, middlebox DPI  
- throttling tests, tcpdump, traceroute  
- platform suppression, interference pattern  

---

## 📡 Cross-Links  
- [🛰️ Throttling Chokepoints (2025-08-26)](./🛰️_throttling_chokepoints_2025-08-26.md)  
- [🧱 Loft Packet Dump Theory (2025-08-06)](./🧱_loft_packet_dump_theory_2025-08-06.md)  
- [🛰️ Direct Interference on Clarity (2025-09-11)](./🛰️_direct_interference_on_clarity_2025-09-11.md)  

---

## 🏮 Footer  
*Network Instability & Deliberate Forking Hypothesis — Field Log* is a living node of the Polaris Protocol.  
It tracks whether instability in inference is accidental load or engineered fork.  

Not assessed as officially sanctioned state behaviour; pattern more consistent with outsourced enforcement, commercial shaping, or structural neglect — interference by incentive, not by decree.  

> 📡 Cross-references:  
> - [Field Logs](../Disruption_Kit/Field_Logs/) — forensic capture of anomalies  
> - [Containment Scripts](../Disruption_Kit/Containment_Scripts/) — platform-level suppression logs  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-09-27_  
