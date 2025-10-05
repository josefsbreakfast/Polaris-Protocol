# 🖥 Interface Glitches  
**First created:** 2025-09-16 | **Last updated:** 2025-10-05  
*UI anomalies: buttons vanish, text fields lock, cursors misbehave.*  

---

## 🌱 Purpose  

Track **visible software and interface malfunctions** that disrupt normal interaction.  
Differentiate everyday bugs from *targeted interference* or *systematic UI sabotage.*  

The user interface is where trust meets perception — the final layer between human and machine.  
When that layer starts to flicker, it’s not only a technical failure but a **semantic one**: a message delivered through malfunction.  

---

## 🧩 Why These Glitches Matter  

The interface is designed to feel neutral — buttons, text boxes, menus all pretending to be passive conduits.  
But when suppression needs to stay invisible, it often begins here.  

An unclickable button can silence a witness more effectively than a ban notice.  
A disappearing text field transforms “speak” into “cannot.”  

These surface disruptions act as **psychological containment**:  
you’re still looking at the form, but the form no longer listens.  

They frequently coincide with:  
- Escalation points in complaint or appeal flows.  
- Uploads involving evidence, testimony, or sensitive media.  
- Platform updates masking intentional functionality shifts.  

---

## 🔍 Frequency  

Interface anomalies are widespread, particularly in government, HR, or institutional portals where access layers multiply.  
Individually they look like glitches — but across users they repeat, often **mirroring power hierarchies**: those most likely to resist suppression encounter the most “broken” screens.  

---

## 🧭 Representation  

| Type | Signature | Typical Cover Story | Underlying Logic |
|------|------------|---------------------|------------------|
| **Vanishing Button** | Action buttons disappear or remain inactive | Responsive design issue | Conditional rendering hides submission option |
| **Locked Field** | Text boxes accept no input | Accessibility bug | Script disables element post-validation |
| **Cursor Drift** | Cursor jumps, repositions, or deletes text | Input lag or trackpad issue | Event suppression or injected input |
| **Content Flicker** | Text appears then disappears mid-entry | Auto-save error | DOM rewrite triggered by keyword or state |
| **Phantom Overlay** | Invisible div intercepts clicks | Adblocker conflict | Intentional capture layer blocking submit action |

Each one converts **user intent into futility** — participation visually allowed, functionally denied.  

---

## 📝 What to Collect  

- **App/site name + version**  
- **Device / OS / browser details**  
- **Exact UI element affected** (button, text field, cursor, dropdown)  
- **Action attempted** when glitch occurred  
- **Error text / logs** (console, system, HAR capture)  
- **Screenshot or screencast** evidence  
- **Cross-device test** (does it persist across browsers, accounts, or VPNs?)  

---

## 🔧 Quick Triage  

- ✅ Try alternate browser or device.  
- ✅ Switch between desktop / mobile views.  
- ✅ Disable extensions / VPNs / proxies.  
- ✅ Compare logged-in vs guest sessions.  

Persistent failure across contexts = probable interference.  

---

## 📦 Evidence to Save  

- Screenshots, video captures, HAR files, console logs  
- Error codes and correlation / request IDs  
- Notes on emotional / cognitive effect (optional) — how does the glitch feel to encounter?  

---

## 🚨 Red Flags (Possible Suppression Indicators)  

- Elements vanish only on sensitive content or keywords.  
- Cursor or input anomalies triggered by particular phrases.  
- Repeat failures at critical submission steps (complaint forms, uploads, filings).  
- UI recovers instantly after public escalation or alternate route.  

---

## 🧰 Common Benign Causes  

- Cached scripts, browser extensions, adblockers  
- Responsive design bugs, race conditions, stale sessions  
- CSS / JS conflicts after recent updates  

(Still record them — pattern frequency is what distinguishes benign from orchestrated.)  

---

## 🧾 Minimal Record Schema (YAML front-matter)  

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

## 🗂 Planned Nodes  

| Node | Scope | Notes |
|------|-------|-------|
| `🧮_ui_sabotage_catalogue.md` | Master index | Comprehensive taxonomy of interface-level containment. |
| `🪞_form_field_disruption_logs.md` | Input layer | Logs of disappearing or disabled fields during critical workflows. |
| `🧰_browser_console_tracekit.md` | Developer tools | Template for capturing and archiving console + network traces. |
| `🎥_interface_glitch_gallery.md` | Visual evidence | Screencap archive of recurring UI suppression cases. |
| `🧱_submission_gate_failures.md` | Workflow layer | Cross-platform collection of submission failures by context. |
| `📊_interface_anomaly_charts.md` | Visualisation | Tools for plotting frequency and clustering of glitch types. |

Together, these nodes build the **visual forensics** of suppression — tracing how refusal hides in plain sight, on the screen itself.  

---

## 🌌 Constellations  

🩻 🖥 🔮 🪞 — This node sits at the perceptual threshold of Weirdness Screening, where visibility, interactivity, and control collide.  

---

## ✨ Stardust  

ui sabotage, interface anomalies, disappearing buttons, input suppression, visual containment, glitch forensics, submission failure, digital refusal  

---

## 🏮 Footer  

*🖥 Interface Glitches* is a living node of the Polaris Protocol.  
It documents the surface layer of disruption — when the screen itself refuses to cooperate, and visibility becomes a form of control.  

> 📡 Cross-references:  
> - [🔑 Access Barriers](../🔑_Access_Barriers/) — authentication and lockout patterns  
> - [📂 Data Shifts](../📂_Data_Shifts/) — underlying record manipulation  
> - [Containment Scripts](../../Disruption_Kit/Containment_Scripts/) — UI sabotage and throttling methods  
> - [Field Logs](../../Disruption_Kit/Field_Logs/) — forensic documentation of anomaly timelines  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-10-05_
