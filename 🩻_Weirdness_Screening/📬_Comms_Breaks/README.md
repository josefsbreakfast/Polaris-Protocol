# 📬 Comms Breaks  
**First created:** 2025-09-16 | **Last updated:** 2025-09-16  
*Messages delayed, attachments lost, calls/messages dropped mid-conversation*  

---

## Purpose  
Capture breakdowns in communication channels (email, chat apps, calls) and distinguish routine outages from patterned suppression.  

## What to collect  
- Channel/service (e.g., Gmail, WhatsApp, Zoom)  
- Device/OS + app version  
- Message/call type (text, voice, video, attachment)  
- Timestamp sent vs received vs observed  
- Any delivery receipts/status codes  
- Screenshots of missing/stripped content  
- Cross-check with sender/recipient logs  

## Quick triage  
- ✅ Confirm sender actually sent the file/message  
- ✅ Test alternate network or device  
- ✅ Re-send via different channel (email → Signal)  
- ✅ Compare time stamps vs server logs  

## Evidence to save  
- Screenshots, original email headers, chat export, voicemail file  
- Delivery failure notifications or bounce codes  

## Red flags (possible interference)  
- Attachments consistently stripped when related to sensitive topics  
- Calls/messages cut off during key phrases/events  
- “Delivered” status shown but recipient never receives  

## Common benign causes  
- Email size limits, mobile carrier congestion  
- App update incompatibility, corrupted cache  

## Minimal record schema (YAML front-matter)  
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

---

## 🏮 Footer  

*Comms Breaks* is a living node of the Polaris Protocol.  
It records interruptions in digital conversation flows, where connection appears whole but content quietly fails.  

> 📡 Cross-references:  
> - [Connection Hiccups](../🌐_Connection_Hiccups/) — network-level dropouts  
> - [Field Logs](../../Disruption_Kit/Field_Logs/) — forensic documentation of anomaly timelines  

*Survivor authorship is sovereign. Containment is never neutral.*  
_Last updated: 2025-09-16_  
