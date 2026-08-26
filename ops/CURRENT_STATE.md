# Current Repository State

Last reconciled: 2026-08-26 07:24 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `0ef952cbab3e169e40288aefd34292bde57aeaec`, the merge of PR #63 (`Build: reconcile PR49 source snapshot onto current main`).
- PR #63 final head `e5c74f0c7deadc05a8a62b18367156f306d0bbbb` passed Core validation `32893463550` on Python 3.11/3.12/3.13 and Daily Repository Maintenance `32893463621` before merge.
- Post-merge push workflows for `0ef952cb...` are green: Core validation `32942362583` succeeded on Python 3.11/3.12/3.13, and Deploy operations dashboard `32942362528` succeeded.
- The post-merge Core matrix passed the test suite, Python compilation, intelligence source-registry validation, source-check-history validation, source collection reporting, intelligence validation, artifact inventory, 310 migration verification, 310 alpha-reproduction verification, dashboard-data generation, maintenance, and the final validation gate on all three Python versions.
- No open repository issues were found in this integrity pass.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`; no reusable-toolset maturity changed.

## Build / integration state

- The former PR #47 / merged PR #58 snapshot at `2026-08-22T19:42:58Z` is canonical through merged replay PR #60.
- Former stale PR #49 is closed as superseded. PR #63 has now merged its raw `intelligence/feeds/2026-08-23-source-health.json` evidence onto current `main` byte-for-byte with original PR #49 blob SHA `2c5eeaa8c4235212ab243cc5eb626411fb204bb5`.
- PR #63 was intentionally reconciliation-only: the Aug. 23 observations are still not written into `data/source_check_history.json`, and canonical registry freshness has not advanced beyond the already-canonical Aug. 22 state.
- Later research PRs #52, #56, and #62 remain open contributed-research lanes and must not advance overlapping canonical source state before the Aug. 23 replay is complete.

## Current research/intelligence state

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through replay PR #50.
- Former PR #47 / merged PR #58 observations at `2026-08-22T19:42:58Z` are canonical through replay PR #60.
- Merged PR #63 preserves the next exact `2026-08-23T07:42:04Z` snapshot on `main`. It contains challenge-gov, ctftime-upcoming, sherlock-bounties, and ethglobal-events observations with predecessor fingerprints intact; canonical replay remains pending.
- PR #52 preserves the NASA Orbital Clarity lead; PR #56 preserves the Aug. 24 HHS Digital Stockpile & Manufacturing Response Network lead; PR #62 preserves the Aug. 25 NASA RASC-AL/source-health lead. These remain contributed research, not canonical truth.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established, but external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Known state / debt

- The merged PR #63 raw snapshot is now on `main`, but its exact four Aug. 23 observations still require canonical source-history replay and corresponding registry timestamp updates.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- Public Pages release health is verified through successful post-merge deployment workflow `32942362528`; direct public-site fetch was unavailable in this runtime, so the workflow result is the deployment-health basis for this pass.

## Current operating priorities

1. Replay the four exact PR #63 observations at `2026-08-23T07:42:04Z` through the canonical source-history mechanism; independently verify predecessor fingerprints and advance only the matching registry timestamps.
2. Run source-history, registry, source-report, intelligence, site-data, Core, and Maintenance validation on the replay head before integration.
3. After the Aug. 23 replay is canonical, evaluate PR #52, PR #56, and PR #62 in chronological/source-overlap order; preserve complete official eligibility/deadline/IP/judging evidence before active opportunity promotion.
4. 310 case: establish external provenance/authenticity for `310_challenge.png` before escalating decryption or hidden-data hypotheses.
5. Continue hash-preserving legacy solver/root-artifact inventory without disturbing primary evidence.

## Coordination note

This integrity pass reconciled state after PR #63 merged. It did not replay source history, advance source freshness, modify open research PR evidence, activate a security target, change tool maturity, or add bespoke website HTML. Open research PRs #52, #56, and #62 remain later chronological lanes.

## Next handoff

Build/Integration should replay the four preserved PR #63 observations at exactly `2026-08-23T07:42:04Z`, verify each predecessor against canonical history, update only corresponding registry timestamps, and rerun source-history/registry/report/intelligence/site-data/Core/Maintenance checks. Only after that replay is canonical should PR #52, PR #56, and PR #62 be evaluated in timestamp/source-overlap order.
