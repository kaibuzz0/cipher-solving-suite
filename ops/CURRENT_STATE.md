# Current Repository State

Last reconciled: 2026-08-28 08:03 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `846eed50b3d586e26f18147b0be15665e80e0521`, the merge of coordination PR #77 after green Core validation `33151353058` and no unresolved review threads.
- PR #76 remains the canonical Aug. 24 source-health replay; its exact head `1ff3a191496508c6b99bd1c54c8a3d40548933e3` passed Core `33111737648`, Intelligence Source Report `33111737656`, and Daily Repository Maintenance `33111737691` before merge.
- Open research PR #75 changes only `intelligence/feeds/2026-08-27-source-health.json`; PR #78 changes only its Aug. 28 raw research/source-health file. Neither owns the Aug. 25 canonical replay paths.

## Build / integration state

- Branch `build/source-history-snapshot-replay-20260828` adds a bounded `source-history replay-snapshot` capability rather than replacing the large provenance-bearing source-history file manually.
- The replay command recomputes every preserved observation SHA-256, checks canonical source IDs, blocks duplicate sources, refuses out-of-order chronology or registry rewind, treats exact repeat records as idempotent, and validates the entire snapshot before writing either canonical file.
- Deterministic tests cover changed/unchanged predecessors, hash mismatch fail-closed behavior, chronology blocking, idempotence, direct-script dry-run behavior, and the actual preserved Aug. 25 PR #62 snapshot against current Aug. 24 canonical history.
- The preserved Aug. 25 hashes independently recompute exactly: `ctftime-upcoming` `26679909...`, `sherlock-bounties` `b50b89ec...`, `arxiv-cryptography` `68147c9a...`, and `ethglobal-events` `b20807c6...`.
- Expected Aug. 25 predecessors are `a96cc699...`, `13c29e51...`, `8fb2b945...`, and `a1954da1...` respectively. No Aug. 25 canonical freshness has been advanced by this branch yet.

## Current research / intelligence state

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through PR #50.
- Former PR #47 / merged PR #58 observations at `2026-08-22T19:42:58Z` are canonical through PR #60.
- Former PR #49 / merged PR #63 observations at `2026-08-23T07:42:04Z` are canonical through PR #67.
- PR #72 / PR #76 observations at `2026-08-24T19:42:29Z` are canonical.
- RASC-AL Aug. 25 and xTech/source-health Aug. 26 raw snapshots are preserved on main and remain the next chronological source lanes.
- PR #75 preserves later Aug. 27 source health and the Education Careers in Your Community challenge; PR #78 preserves later Aug. 28 source health and a CTF provenance preprint lead. Both must remain behind Aug. 25 and Aug. 26 replay.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established, but external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Known state / debt

- The snapshot-replay branch requires green Core/Maintenance/site-data compatibility verification and independent integrity review before merge.
- After that capability is canonical, replay the preserved Aug. 25 PR #62 snapshot using the new command; complete official RASC-AL rules remain a separate gate before structured opportunity promotion.
- Process the preserved Aug. 26 PR #66 snapshot afterward; resolve the xTech|Search 10 official deadline conflict and obtain the complete RFI/application evidence before actionability claims.
- Keep Aug. 27 PR #75 and Aug. 28 PR #78 behind those earlier source lanes.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.

## Current operating priorities

1. Verify and merge the safe snapshot-replay capability without changing source freshness.
2. Use it to replay Aug. 25 PR #62 exactly after independent review of its four hash/predecessor pairs.
3. Then replay Aug. 26 PR #66, followed by Aug. 27 PR #75 and Aug. 28 PR #78, without skipping chronology or manufacturing freshness.
4. Continue the 310 external-provenance gate and hash-preserving root-artifact inventory without inflating experimental capability claims.

## Coordination note

PR #77 cleared the post-PR76 state collision. The active build branch starts from that merge and intentionally does not modify raw Aug. 26-28 research files, canonical source history, registry timestamps, opportunities, cases, or website HTML. Its purpose is to make future chronological replay deterministic and fail-closed instead of requiring large manual provenance-file replacement.

## Next handoff

Repo Integrity should independently run the new snapshot-replay tests and direct-script dry run, confirm the actual Aug. 25 snapshot produces exactly four proposed records with the expected predecessors while writing nothing, and verify the updated `source-history` registry entry reaches generated Tools/Command Site/repository-browser data. Merge only if final CI is green; then replay Aug. 25 in a separate bounded PR.
