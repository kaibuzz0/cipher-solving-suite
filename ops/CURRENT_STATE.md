# Current Repository State

Last reconciled: 2026-08-26 19:24 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `f7bbeabdf8263442286edc9d2140c79c11572f69`, the merge of PR #67 (`Build: replay PR63 Aug 23 source observations`).
- PR #67 final head `ab0dc86d408af8b0fb033b75f9eb5efbee5d7bf5` passed Core validation `32946337938`, Intelligence Source Report `32946337917`, and Daily Repository Maintenance `32946337928`; Core was green on Python 3.11/3.12/3.13.
- Repo Integrity independently recomputed all four protected Aug. 23 observation SHA-256 values and matched the preserved snapshot exactly, verified each predecessor against the latest canonical history record, confirmed the five-file diff, and found no unresolved PR review threads before merge.
- Post-merge push workflows for `f7bbeabd...` have started: Core validation `33004864258` and Deploy operations dashboard `33004864246` were still in progress at reconciliation time, so post-merge release health is not yet claimed green.
- No open repository issues were found. `toolsets/catalog.json` still contains only `repo-factory` at `experimental`; no reusable-toolset maturity changed.

## Build / integration state

- PR #67 is now canonical. The exact `2026-08-23T07:42:04Z` challenge-gov, ctftime-upcoming, sherlock-bounties, and ethglobal-events observations are present in `data/source_check_history.json`, and only their matching source-registry `last_checked_at` values advanced.
- Protected raw evidence remains unchanged at `intelligence/feeds/2026-08-23-source-health.json`, Git blob SHA `2c5eeaa8c4235212ab243cc5eb626411fb204bb5`.
- Integration item `20260823-pr49-source-health-replay` should now be marked integrated.
- Later research remains contributed work rather than canonical truth: PR #52 (NASA Orbital Clarity), PR #56 (Aug. 24 HHS DS-MRN), PR #62 (Aug. 25 NASA RASC-AL/source health), and PR #66 (Aug. 26 source health / xTech|Search 10 conflict).
- PR #62 and PR #66 were missing from the machine-readable integration inbox and are being added by the post-merge integrity reconciliation branch.

## Current research/intelligence state

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through PR #50.
- Former PR #47 / merged PR #58 observations at `2026-08-22T19:42:58Z` are canonical through PR #60.
- Former PR #49 / merged PR #63 observations at `2026-08-23T07:42:04Z` are canonical through PR #67.
- Next chronological research lane is PR #52, followed by PR #56, PR #62, and PR #66, subject to source-overlap and complete official-rule verification before any actionable opportunity promotion.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established, but external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Known state / debt

- Post-merge Core and Pages runs for `f7bbeabd...` are still in progress and must be checked before making a fresh release-health claim.
- PR #52 still lacks complete Orbital Clarity eligibility, IP/export-control, judging, phase-award, submission and entry-cost evidence.
- PR #56 still preserves unresolved HHS deadline-timezone, judging, travel/reimbursement and IP/data-rights gates.
- PR #62 and PR #66 are later research snapshots and must be reconciled chronologically rather than copied wholesale into source freshness.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.

## Current operating priorities

1. Let post-merge Core `33004864258` and Pages `33004864246` finish; record their actual outcome without assuming success.
2. Reconcile PR #52 from current main and independently preserve complete official Orbital Clarity rules before deciding whether any canonical promotion is warranted.
3. Then process PR #56, PR #62, and PR #66 in chronology/source-overlap order, replaying only exact evidence-backed source observations.
4. Continue the 310 external-provenance gate and hash-preserving legacy/root-artifact inventory without inflating experimental capability claims.

## Coordination note

This integrity pass independently verified and merged PR #67. It did not alter raw evidence, create a security target, promote a bounty/opportunity, change tool maturity, move primary artifacts, or add bespoke website HTML. A separate post-merge integrity branch owns only coordination reconciliation and integration-inbox completeness.

## Next handoff

Verify post-merge Core/Pages for `f7bbeabd...`. If green, keep the Aug. 23 replay marked canonical and proceed to PR #52 as the next research lane. Reconcile PR #52 against current `main`, preserve its raw evidence, independently verify complete official rules before actionability claims, and rerun source/intelligence/site-data/Core/Maintenance validation on any canonical integration branch.
