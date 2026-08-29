# Current Repository State

Last reconciled: 2026-08-29 19:30 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `c3e57fa8b13bd7f6d76c3446f329a44d5b346f5b`, the merge of PR #89.
- PR #89 final head `18b8e5033036981d3656678f823f10f3087c0318` passed Core validation `33242370395` across Python 3.11/3.12/3.13 and Daily Repository Maintenance `33242370414` before merge.
- Repo Integrity independently recomputed all five protected Aug. 26 observation SHA-256 values from `intelligence/feeds/2026-08-26-source-health.json`; all matched the preserved snapshot exactly.
- The Aug. 26 predecessor chain is consistent with current canonical history: `challenge-gov` -> `756f0ba6...`, `sherlock-bounties` -> `b50b89ec...`, `arxiv-cryptography` -> `68147c9a...`, `ctftime-upcoming` -> `26679909...`, and `ethglobal-events` -> `b20807c6...`.
- PR #89 adds only `tests/test_aug26_source_replay_readiness.py`; it verifies library dry-run replay and the documented direct-script `replay-snapshot ... --dry-run` command are non-mutating and classify all five observations as replay-ready/changed.
- Pre-merge current-main scheduled Intelligence Source Report and Daily Repository Maintenance runs were green on `08d018181d2f4e9aafffb03f98f6a36e73f42b27`. Post-merge workflow/Pages status for `c3e57fa8...` must still be observed before claiming merge-commit release health.

## Build / integration state

- Source-health observations through Aug. 25 are canonical.
- Aug. 26 PR #66 raw evidence remains preserved on `main` and remains `needs-integration`; PR #89 verifies replay readiness but intentionally does not advance canonical source history or registry freshness.
- The next bounded build step is a separate canonical Aug. 26 replay PR using `python scripts/source_check_history.py replay-snapshot intelligence/feeds/2026-08-26-source-health.json` after preserving the actionability boundary around xTech|Search 10.
- The xTech|Search 10 official-source conflict remains unresolved for actionability: USA.gov, the Army xTech page, and SBIR.gov expose conflicting date windows, and the preserved Army full-RFI link was a placeholder at the Aug. 26 observation time.
- Open PR #75 owns only Aug. 27 raw research, PR #82 owns Aug. 28 raw research, and PR #85 owns Aug. 29 raw research. They must not overtake the Aug. 26 canonical replay.

## Current research / intelligence state

- Aug. 22 morning, Aug. 22 afternoon, Aug. 23, Aug. 24, and Aug. 25 source-health observations are canonical.
- The Aug. 26 snapshot is verified as internally replay-ready, not yet canonical.
- NASA RASC-AL remains specialized research and should not be converted into generic actionable work without complete official competition guidelines.
- xTech|Search 10 remains a high-value watch/reconciliation lead, not a definitive actionable opportunity, until the official deadline/RFI/application conflict is resolved.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- PR #89 changes no tool/toolset registration, case, opportunity, primary evidence, canonical website data, or bespoke website HTML.
- Canonical registry/site-data discovery contracts remain unchanged; PR #89 Core validation passed dashboard-data generation and Agent Operations inputs on all Python matrix jobs.

## Known state / debt

- Confirm post-merge Core/Pages release health on `c3e57fa8...` when runs surface.
- Replay the exact Aug. 26 snapshot canonically in a separate bounded PR without promoting xTech actionability merely because source-health replay is valid.
- Then process Aug. 27 PR #75, Aug. 28 PR #82, and Aug. 29 PR #85 chronologically.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.

## Current operating priorities

1. Observe post-merge Core/Pages release health for `c3e57fa8...`.
2. Canonically replay the verified Aug. 26 snapshot through the deterministic replay command in a separate bounded PR.
3. Keep xTech|Search 10 non-actionable until the authoritative RFI/application window is resolved; source-health replay does not resolve the opportunity conflict.
4. Then process Aug. 27 PR #75, Aug. 28 PR #82, and Aug. 29 PR #85 in chronological order.
5. Continue 310 external-provenance and hash-preserving root-artifact work without inflating experimental capability claims.

## Coordination note

PR #89 was rebuilt from post-PR87 current `main`, superseding stale PR #88/#86 test branches without copying stale shared coordination state. The compatible one-file regression was preserved, later raw research PRs remain untouched, and no source freshness or capability claim was advanced by the verification merge.

## Next handoff

After this post-PR89 coordination PR is green, merge it. Then create a separate bounded Aug. 26 replay PR from current `main`, run the canonical replay command, verify exactly five new `2026-08-26T07:39:05Z` history records with the independently verified hashes/predecessors, advance only matching registry timestamps, and rerun source-history/registry/report/intelligence/site-data/Agent Operations/Core/Maintenance validation. Do not promote xTech|Search 10 actionability until the official RFI/application conflict is independently resolved. Aug. 27, Aug. 28, and Aug. 29 follow afterward.