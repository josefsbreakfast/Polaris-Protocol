# 🛰️ Metadata Monitor Checklist  

**Event:** [Insert subject line / timestamp of the email]  
**Reference:** One-Email Trigger  

---

## 1. Transmission Layer  
- [ ] Sender → verify your own copy in *Sent* folder.  
- [ ] Message ID (unique hash from header).  
- [ ] Return-Path vs. From: — do they match?  
- [ ] Relay hops (Received: headers) — note any unusual servers or delays.  
- [ ] Delivery status notification (bounce, delay, or auto-reply).  

---

## 2. Temporal Behaviour  
- [ ] Time you pressed “send” vs. time it appears in recipient’s system.  
- [ ] Latency patterns: was there a long gap at any hop?  
- [ ] Any suspicious “retry” loops?  
- [ ] Check if responses cluster unusually fast / slow.  

---

## 3. Institutional Reaction  
- [ ] First auto-reply or acknowledgement (time + phrasing).  
- [ ] Any sudden follow-up calls, texts, or third-party contact.  
- [ ] Internal forwards (look for “FW” headers if replies leak them).  
- [ ] Signs of cross-department involvement (e.g. language shifts in reply).  

---

## 4. Containment / Suppression Signs  
- [ ] Unexplained bounce at one address but not another.  
- [ ] Message thread split (same email answered in two threads).  
- [ ] Attachment stripped / reformatted.  
- [ ] Forced “informal” phone call instead of written reply.  

---

## 5. Ripple Watch  
- [ ] Sudden login prompts / password resets on your accounts.  
- [ ] Spike in LinkedIn/other platform shadow metrics within 24h.  
- [ ] Any unrelated organisations contacting you “by coincidence.”  
- [ ] FOI/SAR timing drift — deadlines reset or quietly stalled.  

---

📌 **Note:** Log each tick with timestamp + screenshot where possible.  
Don’t chase them — let their behaviour surface. Metadata monitors feed themselves.  
