# 🧪 Repro Tests Playbook — ToS Non-Compliance as Stealthing
**First created:** 2025-10-06 | **Last updated:** 2025-10-06

Design small, safe experiments to surface non-compliance. Prefer **observational parity tests** over risky confrontations.

## A. Visibility / Reach Tests
**Goal:** Detect covert throttling or ranking suppression.

**Method:**
1. Create **matched posts** (same content, timing, tags).  
2. Publish from **control** and **suspect** accounts (or syndicate via two routes).  
3. Log **impressions, click-through, reshares**, and **time-to-first-interaction**.  
4. Repeat across **3–5 time windows** to smooth noise.

**Evidence:** Divergence beyond expected variance; correlation with flagged topics or prior appeals.

## B. Policy Edit Diffing
**Goal:** Catch retrograde edits.

**Method:**  
- Snapshot ToS and Help pages (HTML/pdf) weekly; compute **diffs**.  
- Flag edits where behaviour **changed before text**.

## C. Data Path Tracing
**Goal:** Discover undeclared partners/processing.

**Method:**  
- Capture **network traffic** during key actions (upload, DM, live).  
- Compare endpoints/vendors to the platform’s declared processors list.

## D. Appeals Latency Probe
**Goal:** Test whether appeals are theatre.

**Method:**  
- File **structured appeals** on matched cases.  
- Measure **latency**, **substance** (template vs. bespoke), and **resolution rate**.

## E. “Pilot Exception” Hunt
**Goal:** Identify secret flags/whitelists.

**Method:**  
- Compare treatment of **partner/advertiser accounts** vs. ordinary users on identical violations.  
- Look for **undocumented exemptions**.

> **Safety:** Do not publish raw PII. Aggregate where possible. Prioritise minimising retaliation risk.

