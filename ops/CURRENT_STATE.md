# Current Repository State

Last reconciled: 2026-08-28 19:24 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `13dff25b7b1fdfb3817975a7bf60f7eff3eb4afc`, the merge of PR #79.
- PR #79 exact final head `087d43f2825897959c969aa65f6814eda7bb851a` passed Core validation `33154463607` across Python 3.11/3.12/3.13, Intelligence Source Report `33154463592`, and Daily Repository Maintenance `33154463591` before merge.
- Core passed the test suite, direct-script replay coverage, compile checks, source registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction checks, dashboard-data generation, maintenance, and the final failure gate.
- Repo Integrity independently inspected the replay implementation and tests, verified the canonical tool/site discovery path, and found no blocking defect before merge.
- Post-merge workflow runs for `13dff25b...` had not surfaced through the connected commit-run query at reconciliation time, so merge-commit CI/Pages are not claimed here.
- Open research PR #75 changes only `intelligence/feeds/2026-08-27-source-health.json`; PR #78 changes only its Aug. 28 raw research/source-health file. Neither overlaps the merged replay implementation paths.

## Build / integration state

- PR #79 canonically added `python scripts/source_check_history.py replay-snapshot <snapshot>` as a bounded provenance-preserving replay path for preserved source-health snapshots.
- The replay command recomputes every preserved observation SHA-256, requires canonical source IDs, rejects duplicate snapshot sources, blocks newer canonical history and registry timestamp rewind, treats exact same-time/same-fingerprint records as idempotent, and validates the complete snapshot before writing canonical files.
- Deterministic tests cover changed/unchanged predecessor derivation, hash-mismatch fail-closed behavior, chronology blocking, idempotence, direct-script `--dry-run` non-mutation, and the actual preserved Aug. 25 PR #62 snapshot against current Aug. 24 canonical history.
- The preserved Aug. 25 hashes independently recompute exactly: `ctftime-upcoming` `26679909...`, `sherlock-bounties` `b50b89ec...`, `arxiv-cryptography` `68147c9a...`, and `ethglobal-events` `b20807c6...`.
- Expected Aug. 25 predecessors are `a96cc699...`, `13c29e51...`, `8fb2b945...`, and `a1954da1...` respectively.
- No Aug. 25 canonical source freshness or opportunity state was advanced by PR #79. Its purpose was to make the next replay safer and reviewable.
- The existing canonical `source-history` tool ID/path remains unchanged and `verified`; only its documented capability description was extended. Command Site snapshot generation consumes canonical `data/tools.json`, so no bespoke website HTML is required.

## Current research / intelligence state

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through PR #50.
- Former PR #47 / merged PR #58 observations at `2026-08-22T19:42:58Z` are canonical through PR #60.
- Former PR #49 / merged PR #63 observations at `2026-08-23T07:42:04Z` are canonical through PR #67.
- PR #72 / PR #76 observations at `2026-08-24T19:42:29Z` are canonical.
- The Aug. 25 PR #62 RASC-AL/source-health snapshot is now the next `needs-integration` source lane and should be replayed with the merged safe replay command in a separate bounded PR.
- The Aug. 26 PR #66 xTech/source-health snapshot remains blocked behind Aug. 25. PR #75 Aug. 27 and PR #78 Aug. 28 raw research remain later chronological lanes.
- Complete official RASC-AL rules remain a separate verification gate before structured opportunity promotion.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established, but external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Known state / debt

- Replay the preserved Aug. 25 PR #62 snapshot next using the newly merged deterministic replay command; do not combine the capability merge and source-freshness advancement into the same review boundary.
- Independently verify complete official RASC-AL eligibility, judging, submission, IP, travel/cost, and top-award rules before any structured actionability promotion.
- Process the preserved Aug. 26 PR #66 snapshot afterward; resolve the xTech|Search 10 official deadline conflict and obtain complete RFI/application evidence before actionability claims.
- Keep Aug. 27 PR #75 and Aug. 28 PR #78 behind those earlier source lanes.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- Direct local replay could not be run in this integrity pass because the runtime could not resolve `github.com`; GitHub-hosted deterministic CI plus independent source/test inspection are the verification basis.

## Current operating priorities

1. Replay the exact Aug. 25 PR #62 snapshot in a separate bounded branch/PR using `source_check_history.py replay-snapshot`, preserving its four verified fingerprint/predecessor pairs.
2. Validate source history, source registry, collection report, intelligence, site-data, Agent Operations, Core, Maintenance, and Pages compatibility after that replay.
3. Then process Aug. 26 PR #66, followed by Aug. 27 PR #75 and Aug. 28 PR #78, without skipping chronology or manufacturing freshness.
4. Continue the 310 external-provenance gate and hash-preserving root-artifact inventory without inflating experimental capability claims.

## Coordination note

PR #79 was independently reviewed and merged from current post-PR77 `main`. It preserved the raw Aug. 26-28 research lanes, did not alter canonical source-history observations or registry timestamps, did not change opportunities/cases/toolsets, and did not add bespoke website HTML. The safe replay mechanism is now canonical; the next source-state mutation must remain a separate reviewable change.

## Next handoff

Create a bounded Aug. 25 replay PR from current `main`, first run `python scripts/source_check_history.py replay-snapshot intelligence/feeds/2026-08-25-source-health.json --dry-run`, confirm exactly four proposed records with the expected predecessors and no writes, then replay without `--dry-run`. Rerun source/history/report/intelligence/site-data/Core/Maintenance validation and independently review before merge. Only after Aug. 25 is canonical should Aug. 26, Aug. 27, and Aug. 28 be processed in order.
