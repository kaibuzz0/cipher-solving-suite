# Tool-Evidence Deference in AI Vulnerability Auditors

**Status:** triage / offline defensive research only. **Owner:** unclaimed.

Primary paper: https://arxiv.org/abs/2610.32876 (submitted 2026-10-23).
Author replication code: https://github.com/lzh0082-cloud/CODE-DETECTION at commit `7d7123df073e1cce224c4e47c4d698b1e6ebc470` (MIT for code).

## Question

Can an AI security-review assistant distinguish correct static-analysis claims from fabricated assurances, rather than trusting reassuring tool text? The paper reports reduced vulnerability detection when a tool falsely claims a missing check exists. Results are **author-reported** and have **not** been reproduced by this repository.

## Authorized work boundary

Use **only offline synthetic C/C++ snippets and mocked analysis outputs** for suite regression tests. Do not run scans, exploitation, credential attacks, or probing against real third-party targets. Public paper/code availability is not target authorization.

## Next experiment

1. Check pinned author package unit tests and requirements in an isolated environment.
2. Review separate PrimeVul and Zenodo dataset rights before any download/import.
3. Create paired local fixture cases with identical code and (a) truthful proof obligations, (b) fabricated assurance, and (c) fabricated alarm.
4. Verify each tool claim against the code in a separate deterministic step; compare decisions with and without verification.
5. Record fixtures, hashes, outputs, environment, and failures; do not claim paper reproduction without matching its datasets/protocol.

Evidence and limitations: `evidence/README.md`. Results and attempts: `attempts.md`.
