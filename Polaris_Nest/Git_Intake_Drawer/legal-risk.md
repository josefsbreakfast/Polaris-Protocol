---
name: Legal risk
about: Report outputs that may defame, criminalize, or otherwise legally harm an individual or organization
title: '[legal-risk] brief description'
labels: legal-risk
body:
  - type: textarea
    id: example
    attributes:
      label: Example output (redact PII)
      description: Provide the output observed. Do not paste unredacted personal identifying information.
  - type: input
    id: severity
    attributes:
      label: Severity
      description: Low / Medium / High — does this materially threaten reputation or legal standing?
  - type: textarea
    id: suggested_action
    attributes:
      label: Suggested immediate action
      description: e.g., redact, remove, contact counsel, escalate to core team
