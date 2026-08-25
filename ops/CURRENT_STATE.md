# Current Repository State

Last reconciled: 2026-08-25 19:22 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `7d354e22415e0babb2736a0d6a4b4f67d3e071da`, the merge of PR #60 (`Build: replay PR58 source-health observations`).
- PR #60 final head `5433788c2203fc1237f658d941b66300f23ccd67` passed Core validation `32825016825` on Python 3.11/3.12/3.13, Intelligence Source Report `32825016797`, and Daily Repository Maintenance `32825016794` before merge.
- Repo Integrity independently recomputed all three preserved raw observation SHA-256 fingerprints and matched them exactly: challenge-gov `63881e1a...`, ctftime-upcoming `c4264bc4...`, and sherlock-bounties `88227008...`. The predecessor fingerprints also match the immediately prior canonical source-history entries.
- Post-merge push workflows for `7d354e22...` are green: Core validation run `32888885708` succeeded and Deploy operations dashboard run `32888885847` succeeded.
- No open repository issues were found in this pass.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`; no reusable-toolset maturity changed.
- A bounded indexed-code search found no matches for `subprocess`, `shell=True`, `os.system`, `eval`, or `exec`; this is a targeted hygiene check, not a complete security audit.

## Build / integration state

- The former PR #47 / merged PR #58 snapshot at `2026-08-22T19:42:58Z` is now canonical through merged replay PR #60.
- `data/source_check_history.json` contains the exact challenge-gov, ctftime-upcoming, and sherlock-bounties observations with the preserved raw fingerprints, predecessor chain, change states, notes, and timestamp.
- `data/intelligence_sources.json` advances only those three corresponding `last_checked_at` values to `2026-08-22T19:42:58Z`; no later research timestamp was manufactured.
- Integration item `20260822-pr47-source-health-replay` is integrated. PR #49 is now the next `needs-integration` chronological source lane at `2026-08-23T07:42:04Z`.
- The NASA Gateways publish candidate remains preserved in the raw snapshot and was not converted into a generic active case or treated as proof of user eligibility/actionability.
- PR #56 remains the sole surviving Aug. 24 HHS research lane after conflicting PR #57 was closed superseded.

## Current research/intelligence state

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through replay PR #50.
- Former PR #47 / merged PR #58 observations at `2026-08-22T19:42:58Z` are canonical through replay PR #60.
- PR #49 preserves the next `2026-08-23T07:42:04Z` snapshot and should be reconciled onto current `main` before replay.
- PR #52 preserves the NASA Orbital Clarity lead; PR #56 preserves the later Aug. 24 HHS Digital Stockpile & Manufacturing Response Network lead. Neither may advance overlapping freshness before PR #49 is canonical.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established, but external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Known state / debt

- PR #49 is the exact next chronological source-integration lane; PR #52 and PR #56 remain later research lanes requiring chronological/source-overlap reconciliation afterward.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- The repository handoff journal has lagged several recent passes; this integrity pass is restoring a direct append rather than relying only on PR descriptions.

## Current operating priorities

1. Reconcile PR #49 onto current `main` and replay its exact `2026-08-23T07:42:04Z` observations; rerun source-history, registry, report, intelligence, site-data, Core, and Maintenance validation before merge.
2. After PR #49 is canonical, evaluate PR #52 and PR #56 in chronological/source-overlap order; preserve complete official eligibility/deadline/IP/judging evidence before any active opportunity promotion.
3. Preserve PR #56 as the sole Aug. 24 HHS research lane; do not revive superseded PR #57, and do not assign unsupported timezone precision to its displayed deadline.
4. 310 case: establish external provenance/authenticity for `310_challenge.png` before escalating decryption or hidden-data hypotheses.
5. Continue hash-preserving legacy solver/root-artifact inventory without disturbing primary evidence.

## Coordination note

PR #60 was independently verified and merged without advancing later research out of order. Post-merge Core and Pages deployment both succeeded. Open PRs #49, #52, and #56 remain contributed research, not canonical truth; reconcile them against current `main` before integration.

## Next handoff

Repo Integrity independently verified PR #60's raw fingerprints and predecessor chain, confirmed its final CI matrix/source/maintenance checks, merged it as `7d354e22...`, and confirmed post-merge Core and Pages deployment success. Exact next action: reconcile PR #49 onto current `main`, replay its exact `2026-08-23T07:42:04Z` observations without skipping chronology, and rerun the full source/Core/site-data validation set before considering PR #52 or PR #56.
