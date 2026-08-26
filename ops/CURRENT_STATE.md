# Current Repository State

Last reconciled: 2026-08-26 08:10 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `ace1b5ea0fad291b8b71e5a66762a98694f01f3d`, the merge of PR #65 (`Ops: reconcile state after PR #63 merge`).
- PR #65 final head `de560d89f6488aa519bbe096ee1bca89007a8066` passed Core validation `32943027517` and Daily Repository Maintenance `32943027263` before merge, with no unresolved review threads.
- The most recent verified post-merge Pages health remains PR #63 merge commit `0ef952cb...`: Core `32942362583` and Deploy operations dashboard `32942362528` succeeded.
- Replay PR #67 implementation head `b4d519c59207b509d5be1a856a2de927f3859df9` passed Core validation `32946063477` and Intelligence Source Report `32946063457`. The Core matrix passed tests, compilation, source registry/history validation, collection reporting, intelligence validation, artifact inventory, 310 migration/reproduction verification, dashboard-data generation, maintenance, and the final validation gate.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`; no reusable-toolset maturity changed.

## Build / integration state

- PR #65 cleared stale post-PR63 coordination state before the replay branch was created.
- PR #67 (`Build: replay PR63 Aug 23 source observations`) is based on post-PR65 `main` and replays the exact four `2026-08-23T07:42:04Z` observations preserved by merged PR #63 / former PR #49.
- The protected raw snapshot remains byte-identical at Git blob SHA `2c5eeaa8c4235212ab243cc5eb626411fb204bb5`.
- PR #67 prepends the exact challenge-gov, ctftime-upcoming, sherlock-bounties, and ethglobal-events observations into `data/source_check_history.json` and advances only the matching source-registry `last_checked_at` timestamps. Later registry metadata is preserved.
- PR #67 remains a review branch until its coordination-complete final head is independently verified; the replay is not claimed canonical on `main` yet.
- Later research PRs #52, #56, #62, and #66 remain separate chronological lanes and must not overtake this replay.

## Current research/intelligence state

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through replay PR #50.
- Former PR #47 / merged PR #58 observations at `2026-08-22T19:42:58Z` are canonical through replay PR #60.
- For the Aug. 23 replay, all four preserved observation SHA-256 values were independently recomputed and matched exactly: challenge-gov `6d846e46...`, CTFtime `c91ed131...`, Sherlock `f6fea98b...`, ETHGlobal `f3bd2bb7...`.
- Each preserved `previous_fingerprint` matches the latest canonical predecessor before replay: challenge-gov `63881e1a...`, CTFtime `c4264bc4...`, Sherlock `88227008...`, ETHGlobal `276adb8a...`.
- PR #52 preserves NASA Orbital Clarity research; PR #56 preserves the Aug. 24 HHS Digital Stockpile lead; PR #62 preserves the Aug. 25 NASA RASC-AL/source-health lead; PR #66 preserves Aug. 26 source health and the xTech|Search 10 deadline conflict. These remain contributed research, not canonical truth.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established, but external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Known state / debt

- PR #67 still needs final-head CI after coordination-file updates and independent Repo Integrity review before merge.
- `docs/AGENT_HANDOFF.md` is append-only. The connected mutation primitive replaces the entire file rather than providing an atomic append; this pass will not risk journal truncation. The exact handoff is preserved in PR #67's body for an append-capable integrity pass.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.

## Current operating priorities

1. Independently verify PR #67's four replay entries against the protected raw snapshot and confirm final-head Core/source-report/site-data validation; merge only if clean.
2. After the Aug. 23 replay is canonical, evaluate PR #52, PR #56, PR #62, and PR #66 in chronological/source-overlap order; preserve complete official eligibility/deadline/IP/judging evidence before active opportunity promotion.
3. 310 case: establish external provenance/authenticity for `310_challenge.png` before escalating decryption or hidden-data hypotheses.
4. Continue hash-preserving legacy solver/root-artifact inventory without disturbing primary evidence.

## Coordination note

This build pass merged the already-green coordination-only PR #65 before branching, preventing stale shared-state overlap. PR #66 appeared as newer Aug. 26 research and was intentionally left untouched. No canonical intelligence item, opportunity claim, target authorization state, active case, tool maturity, primary evidence, or bespoke website HTML was changed.

## Next handoff

Repo Integrity should independently compare PR #67's four history records with `intelligence/feeds/2026-08-23-source-health.json`, confirm the predecessor chain and the four matching registry timestamps, verify generated source/site data and final-head CI, safely append the build handoff to `docs/AGENT_HANDOFF.md`, and merge #67 only if those checks remain clean. After merge, process PR #52, #56, #62, and #66 in chronology/source-overlap order.
