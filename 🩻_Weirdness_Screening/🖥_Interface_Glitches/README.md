# 🖥 Interface Glitches  
**First created:** 2025-09-16 | **Last updated:** 2025-09-16  
*UI anomalies: buttons vanish, text fields lock, cursors misbehave*  

---

## Purpose  
Track visible software/interface malfunctions that disrupt normal interaction.  
Differentiate everyday bugs from targeted interference or systematic UI sabotage.  

## What to collect  
- App/site name + version  
- Device/OS/browser details  
- Exact UI element affected (button, text field, cursor, dropdown)  
- Action attempted when glitch occurred  
- Error text/logs (console, system, HAR capture)  
- Screenshot or screencast evidence  
- Whether issue persists across devices/networks  

## Quick triage  
- ✅ Try alternate browser or device  
- ✅ Switch between desktop/mobile views  
- ✅ Disable extensions/VPNs/proxies  
- ✅ Compare logged-in vs guest sessions  

## Evidence to save  
- Screenshots, video captures, HAR files, console logs  
- Error codes and correlation/request IDs  

## Red flags (possible interference)  
- Elements vanish only on sensitive content or keywords  
- Cursor/input anomalies triggered by specific phrases  
- Repeat failures at critical submission steps  

## Common benign causes  
- Cached scripts, browser extensions, adblockers  
- Responsive design bugs, race conditions, stale sessions  

## Minimal record schema (YAML front-matter)  
```yaml
when: 2025-09-16T14:22:00Z
app: "Gov Portal"
device: "Windows 11, Edge 128"
symptom: "Submit button greyed out after filling all fields"
error: "No client-side errors; POST blocked"
artifacts: [screen1.png, console.log]
repro: {guest: true, logged_in: false}
notes: "Works in Firefox, fails in Edge + Chrome"
```
---

## 🏮 Footer  

*Interface Glitches* is a living node of the Polaris Protocol.  
It documents the surface layer of disruption: when the screen itself refuses to cooperate.  

> 📡 Cross-references:  
> - [Containment Scripts](../../Disruption_Kit/Containment_Scripts/) — UI sabotage & throttling methods  
> - [Field Logs](../../Disruption_Kit/Field_Logs/) — forensic documentation of anomaly timelines  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-09-16_  
