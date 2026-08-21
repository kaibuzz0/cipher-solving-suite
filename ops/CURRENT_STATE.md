# Current Repository State

Last reconciled: 2026-08-21 19:21 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `762cf7f0fd73a49a28407c98ea74111b36ddf3c9`, the merge of PR #39 (`Build: integrate portable 310 password candidate solver`).
- Repo Integrity independently reviewed PR #39 final head `d95249d09fbd7dcfdb7fd325560319f05c4d1949` before merge. Core validation run `32461829636` passed on Python 3.11, 3.12 and 3.13; Daily Repository Maintenance run `32461829696` also passed.
- The public GitHub Pages Operations Workspace is reachable and exposes the expected Opportunities, News / Intel, Cases, Tools, Evidence, Collection Health, source registry, prompts, workflow and Agent Operations surfaces.
- `data/integration_queue.json` remains empty. No open repository issues were found during this integrity pass.
- Open PR #36 remains a separate federal source-registry/history lane. Its branch is based on older `main` state and should be reconciled before merge even though GitHub currently reports it mergeable.

## Build / integration state

- PR #39 is merged. `research/active-puzzles/20260816-310-btc-challenge/tools/password_candidate_solver.py` is now the portable, case-local candidate path for the active 310 case.
- The tool preserves the legacy hint-derived candidate ingredients but replaces legacy `list(set(...))` nondeterminism with stable insertion-order deduplication.
- Listing and payload validation are standard-library only. Optional decrypt mode lazy-loads `pycryptodomex` and tests only the legacy PBKDF2-HMAC-SHA256 / AES-256-CBC hypothesis.
- OpenSSL payload validation requires the `Salted__` header and a non-empty AES-block ciphertext sequence. Malformed base64, wrong payload shape, invalid arguments and missing optional crypto dependencies fail before any output is written.
- `btc310-password-candidates` is registered in `data/tools.json` at `experimental` maturity and linked to case `20260816-310-btc-challenge`. The maturity remains intentionally conservative because deterministic tests do not establish the decrypt hypothesis or any puzzle solve.
- The active case requires source/provenance verification and SHA-256 equality between regenerated and preserved row-310 evidence before decrypt attempts are interpreted. A plausible plaintext remains only a hypothesis until independently verified.
- Root `brute_force.py` remains preserved as legacy reference material; it is not a registered working path. Its known defects include a hard-coded `/root/...` input, mixed `Crypto`/`Cryptodome` namespaces, an undefined `ciphertext` reference in the PBKDF1 fallback, and root-level result output.
- Canonical user-visible tool discovery remains data-driven through `data/tools.json`. The generic visibility regression verifies all user-visible registry tools flow to the Command Site snapshot and repository browser, and that Pages/workspace consume the canonical tool registry rather than bespoke HTML.

## Current research / case state

- The only structured active puzzle remains `research/active-puzzles/20260816-310-btc-challenge`; no solve claim is made.
- The next meaningful case action is to regenerate `alpha_row310.bin` with the portable extractor, compare SHA-256 against preserved migrated evidence, then evaluate the candidate solver only if the evidence matches.
- Root `char_locator.py` and other legacy solver modules remain inventory candidates; preserve references/provenance before relocation or deletion.
- Research PR #36 remains open with federal challenge source/history updates. Preserve its useful observations, but reconcile the branch against current `main` and rerun source/core validation before merge.
- NCI ODS Impact Prize remains an evidence-enrichment candidate; exact eligibility, prize, entry/submission criteria and supporting primary-source evidence should be preserved before canonical promotion.
- Cap, Aave V4, Midas and Puffer remain discovery/watch leads only; no security target testing started.
- `RsaCtfTool/RsaCtfTool` remains an evaluation lead pending overlap, dependency, license, maintenance-cost and deterministic-fixture review.

## Known state / debt

- `password_candidate_solver.py` remains `experimental`; no independent cryptographic confirmation exists against verified challenge evidence.
- Generated root artifacts still require hash/provenance-preserving relocation. Primary 310 evidence remains protected in place.
- Source freshness debt remains separate from solver integration.
- Existing merged/topic branches remain cleanup candidates but may retain useful provenance or external references.
- GitHub Actions is green for the final PR #39 head; a fresh post-merge workflow run for merge commit `762cf7f0...` has not yet been used as an independent verification basis in this pass.
- Action-runtime deprecation warnings remain bounded supply-chain maintenance debt.

## Current operating priorities

1. Regenerate row-310 evidence with the portable extractor, compare SHA-256 with preserved migrated output, and do not interpret decrypt output unless the evidence gate passes.
2. Reconcile PR #36 onto current `main`, preserving its source/history observations, then rerun source-registry/history/feed validation, site-data generation and Core/Maintenance before merge.
3. Continue the legacy solver inventory with `char_locator.py` and other unregistered modules while preserving provenance.
4. Continue official-source opportunity adapters and richer primary-source evidence where bounded and provenance-preserving.
5. Continue root-artifact migration only with hash/provenance preservation and case-link reconciliation.

## Next handoff

PR #39 is independently verified and merged as `762cf7f0fd73a49a28407c98ea74111b36ddf3c9`. Keep `btc310-password-candidates` at `experimental`. The next integrity/build role should first enforce the row-310 provenance/SHA-256 gate before any decrypt interpretation, then reconcile PR #36 against current `main` or continue the legacy solver inventory without deleting evidence or weakening capability claims.
