---
name: Security signal
about: Report anomalous/suspicious outputs or potential API/exploit behavior
title: '[security-signal] brief description'
labels: security-signal
body:
  - type: textarea
    id: repro
    attributes:
      label: Minimal repro (please do not include PII)
      description: Describe the minimal steps to observe the anomalous behavior. Include model, sampling params, and any prompt snippets (redact personal data).
  - type: input
    id: impact
    attributes:
      label: Impact summary
      description: Short note on why this is risky (editorial, legal, safety)
  - type: textarea
    id: mitigation
    attributes:
      label: Suggested containment
      description: Quick suggestions for removal, redaction, or test cases to block this behavior
