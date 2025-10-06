# 📋 Diagnostic Checklist — ToS Non-Compliance as Stealthing
**First created:** 2025-10-06 | **Last updated:** 2025-10-06

Use this quick triage when you suspect a platform is breaching its own ToS or policy promises.

## 0) Case meta
- Platform / App / Host: `___`
- Jurisdiction(s): `___`
- Date range: `___`
- Reporter(s): `___`
- Risk level: `Low / Med / High`

## 1) Signals (tick ✓ / cross ✗ / unsure ?)
- [ ] Sudden change in **defaults** (privacy, discovery, sharing) with low-salience notice  
- [ ] **Selective enforcement** visible (critics penalised; partners unaffected)  
- [ ] Evidence of **secret flags/lists/whitelists** affecting reach or moderation  
- [ ] **Retroactive policy edits** following user complaints  
- [ ] **Appeal loops** or template-only replies within SLA windows  
- [ ] **Undeclared telemetry** or SDK calls to partners not named in ToS/Privacy  
- [ ] **Ranking/visibility anomalies** clustering around specific topics or accounts

## 2) Minimal evidence to collect
- [ ] Before/after screenshots (settings, policy pages) with timestamps  
- [ ] Network traces (headers, endpoints) showing data sinks  
- [ ] Ticket IDs + response timing + content of replies  
- [ ] Reach metrics vs. matched controls (A/B style)  
- [ ] Partner policies contradicting platform statements

## 3) Clause mapping
- ToS/Privacy clause(s) **allegedly breached**:  
  - `Clause ID / excerpt → Observed behaviour`
- Materiality (why it matters to a reasonable user): `___`

## 4) Decision gates
- **Proceed to Repro Tests** if ≥2 strong signals **and** at least one clause mapped.  
- **Escalate** if there is personal risk or retaliation patterns.

