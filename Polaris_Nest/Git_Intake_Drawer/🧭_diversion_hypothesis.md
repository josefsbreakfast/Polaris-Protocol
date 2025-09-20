# 🧭 Diversion Hypothesis Node — “Why we get steered away”  
**First created:** 2025-09-20 | **Last updated:** 2025-09-20  
*Neutral hypothesis inventory: why inquiries or signals may be diverted from a materially pertinent locus, and how to test for diversion without allegation.*

---

## 1. Phenomenon (concise)
The subject observes repeated procedural or informational friction that appears to steer attention away from a potentially pertinent locus (event, venue, dataset, or institutional process). This node records the hypothesis space (mechanisms of diversion) and an evidence-first checklist to test whether diversion occurred.

---

## 2. Plausible diversion mechanisms (neutral list)
1. **Procedural friction** — departments place FOI/SARs into long “review” queues or apply vague exemptions to delay disclosure.  
2. **Information siloing** — relevant logs/data held in a different team or vendor, producing delays or “not held” replies.  
3. **Record exhaustion** — institutions claim records absent due to retention policy, or claim logs purged under standard practice.  
4. **Recharacterisation** — complaints or incidents are re-categorised under unrelated frameworks (e.g., “HR” rather than “security”) to limit technical triage.  
5. **Scope migration** — investigators focus on peripheral symptoms rather than root causes (a political or bureaucratic redirection).  
6. **Civil-society overload** — NGOs/journalists overloaded and unable to take up recurring small anomalies; patterns fade.  
7. **Deliberate obfuscation** — bad actors bury or remix evidence via spoofing / cloned identifiers so inquiries chase false leads (note: this is a hypothesis to be tested with forensics).  
8. **Resource asymmetry** — those who notice (litmus-test class) lack capacity to escalate, so departments face low risk in delaying.

---

## 3. Red flags consistent with diversion (observable signals)
- Repeated “under review” responses with no substantive explanation.  
- Multiple FOI refusals citing different exemptions for the same request.  
- Vendor replies: “not our logs” despite vendor being confirmed venue provider.  
- Time-lag pattern: where the same requester repeatedly gets longer, vaguer replies.  
- Inconsistent record retention statements across similar events.  
- Evidence of rapid purging (logs timestamped as deleted shortly after request).  
- Focus-shift in investigation reports (detailed on peripheral actors, vague on central systems).

---

## 4. Evidence checklist — what to collect & where to ask (ordered by impact)
**A. Immediate preservation & procurement**
- Preserve original FOI/SAR requests & all replies (email headers, timestamps).  
- Ask the body to acknowledge and preserve all logs with an explicit preservation request (template below).  
- Preserve venue/vendor contracts showing who ran Wi-Fi / badge / registration systems for the event(s).

**B. Technical logs & forensics**
- DHCP/RADIUS/AP association logs for event windows.  
- Email gateway (MIME + headers) for any related spoofed messages.  
- Vendor admin access logs (who accessed attendee DBs and when).  
- Carrier provisioning logs if SIM/SMS signals are involved.  
- CCTV / access-control timestamps (where lawful).

**C. Administrative & process records**
- Document retention policies in force at the time (ask for the policy documents).  
- Internal review logs / meeting minutes referencing the FOI/SAR (ask for internal review notes via FOI).  
- Escalation logs: who handled the FOI / complaint and any change-of-handler notes.  
- External correspondence with NGOs / journalists (if any).

**D. Public-source & reputational checks**
- Parliamentary correspondence (committee letters, Ministerial replies) around the same time window.  
- Local press, social media posts, and LinkedIn profiles of key witnesses / respondents (public, non-sensational check).  
- NGO or union casework logs (published anonymised instances).

---

## 5. Triage tests to run (quick, cheap, evidence-light)
1. **Consistency test:** submit the same FOI request to the named vendor and to the venue — compare responses and time to preserve.  
2. **Redaction pattern test:** request a small, specific item (e.g., “RADIUS logs for AP ID X for yyyy-mm-dd hh:mm–hh:mm”) — narrow asks are harder to stonewall.  
3. **Parallel request:** have two different people from different addresses submit identical requests — see if responses differ (detects discriminatory treatment).  
4. **Retention/Policy check:** request the record retention policy and the last purge/export action for the relevant systems.  
5. **Chain-of-custody ask:** request chain-of-custody for any logs that are cited as evidence in complaints/investigations.

---

## 6. FOI/SAR preservation & escalation templates (short)
**A. Preservation request (send to venue/vendor/department):**  
> Subject: Preservation request — logs and records for [Event] on [date]  
> Please acknowledge and preserve all original logs, exports, and backups relating to [event], including RADIUS/DHCP/AP logs, registration DB, badge-scan records, and vendor admin access logs for the period [date time window]. Please do not purge or alter these records and provide a confirmation of preservation and an estimate of when an export can be provided. — [name/contact]

**B. Internal review request (to department FOI/Complaints):**  
> Please provide the internal review notes, handler changes, and any meeting minutes or emails that reference my FOI/SAR [ref] (specifically explaining legal grounds for refusal). I request a named contact who is handling the review and a timescale for resolution.

---

## 7. Public checks to run (low-risk investigators)
- Pull Hansard/committee letters for the date range and cross-check whether the issue was discussed.  
- Search national/local press archives for unexplained “review” or “investigation” stories tied to the dept/venue.  
- Check LinkedIn / public bios for sudden career changes of key staff (resignations, moves) — this can be a signal of internal review but is not proof.

---

## 8. Next-step decision map (what you can do now)
- **If you want proof-of-diversion:** run triage tests (narrow FOI, preservation requests, parallel requests) and gather log exports.  
- **If you want to build public pressure:** compile the pattern (multiple “under review/stonewall” instances) into a short briefing and send to a friendly journalist or oversight NGO with preserved artifacts (avoid sharing sensitive originals).  
- **If you want internal correction:** use the preservation & internal review templates, then request ICO intervention if preservation/refusal looks abusive.

---

## 9. Ethics & safety note
- This node contains only neutral investigatory steps and public-source checks. It **does not** suggest harm or targeting of individuals. Where carrier/venue logs are involved, lawful process is required to obtain third-party data.

---

## 🏮 Footer
*Diversion Hypothesis Node* is a living diagnostic node in the Polaris Protocol. Use it to test whether procedural or deliberate diversion explains the repeated “guardrails” you observe.  
Cross-references: Transparency Floor Node; Event Linkage Node; Forensic Checklist.  
_Last updated: 2025-09-20_
