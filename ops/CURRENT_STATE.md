# Current Repository State

Last reconciled: 2026-09-04 08:00 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `d581d4d11fac14ead7444481650f270344b74717`, the merge of PR #132 (`Build: replay reconciled Aug 28 afternoon source health`).
- PR #132 final head `5c4b6d99e0f6a0ec698694fb5d08af18d4cb8760` passed Core validation `33850817356`, Intelligence Source Report `33850817358`, and Daily Repository Maintenance `33850817510` before merge.
- Exact-merge Core validation `33850953467` and Deploy operations dashboard `33850953537` both succeeded on `d581d4d11fac14ead7444481650f270344b74717`. The Core matrix passed Python 3.11, 3.12, and 3.13; the Python 3.12 job completed tests, compilation, source-registry/history/report validation, intelligence validation, artifact inventory, both 310 verification stages, site-data generation, maintenance, and the final validation gate.
- No open repository issue currently blocks the chronological source-replay lane.
- A direct public Pages render was not independently fetched in this pass; release-health claims are limited to the observed successful deployment workflow plus successful site-data generation in Core.

## Build / integration state

- Canonical source history now extends through Aug. 28 afternoon at `2026-08-28T19:37:39Z`.
- PR #132 canonically added exactly two provenance-safe records from `intelligence/feeds/2026-08-28-afternoon-source-health-reconciled.json`:
  - `ctftime-upcoming`: `8ab1541b75153d193963da65855a7c07f99bf9a26bf701b45b1fbc754272a19b`, predecessor `ab0660900275cf3767cd9b2f49f4bd08c2c0e2f68fa6f074ae1f2f55e66b380f`.
  - `github-search`: `db0ecb913bc55b1de3b637f97325c14ac439c4531e7494144a8db792c457622b`, predecessor `993f3601dafc2f452f9267c79a861f1e4de5e33e0065e7be100191cdd95dcca9`.
- Only the matching `ctftime-upcoming` and `github-search` registry timestamps advanced; the regression now requires exact provenance preservation plus canonical uniqueness/idempotence.
- The original invalid-hash Aug. 28 afternoon raw snapshot remains preserved unchanged. `RsaCracker` remains an evaluation lead and was not registered or promoted as a repository capability.
- The next chronological raw evidence on `main` is `intelligence/feeds/2026-08-29-source-health.json`, followed by `2026-08-29-afternoon-source-health.json`, then Aug. 30 morning/afternoon. These must be independently verified against the new Aug. 28 afternoon canonical predecessors before any replay.

## Current research / intelligence state

- Later research remains contributed/noncanonical evidence until chronology reaches it. Open research lanes include PR #103/#106 (Aug. 31), PR #109/#112 (Sep. 1), PR #116/#120 (Sep. 2), PR #123/#125 (Sep. 3), and PR #131 (Sep. 4).
- PR #131 was opened from the pre-#132 current main and contains only a Sep. 4 raw research contribution. Its ETHOnline/prize and hook-supply-chain observations are not canonical truth and must be reconciled at their chronology point after Aug. 29-Aug. 30 and the later open research lanes.
- Careers in Your Community remains specialized school/team opportunity intelligence, not generic individual work.
- xTech|Search 10 remains non-actionable until authoritative Army/RFI/application evidence resolves conflicting official date/state surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, payout, or puzzle solve.
- Root legacy/generated artifacts remain preservation debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Canonical tools, toolsets, cases, source health, repository data, and Agent Operations continue to flow through registries/manifests/site-data builders rather than bespoke HTML.
- Core validation confirms dashboard/site-data generation continues to succeed on the exact merge commit.

## Security / maintenance state

- Bounded default-branch searches found no indexed `shell=True` or `os.system(` use. Known `subprocess.run` use in regression coverage uses a fixed argument vector with no shell invocation; this is a targeted check, not a complete security audit.
- The latest verified artifact inventory remains 40 items, 10 duplicate groups, 11 orphaned items, 12 generated outputs, 7 items needing case links, 1 protected primary-evidence item, and 0 unknown-provenance items.
- Known root-generated 310 artifacts remain warnings and were left untouched.
- Workflow dependencies remain bounded but not fully immutable: Actions workflows use major tags such as `actions/checkout@v4`, `actions/setup-python@v5`, and `actions/upload-artifact@v4`, while Python test dependencies use bounded version ranges. Immutable action pinning/runtime migration and lockfile strategy remain supply-chain hardening debt, not a release blocker for the verified replay.
- No primary research artifact was deleted, moved, or rewritten in this pass.

## Known state / debt

- `docs/WORK_QUEUE.md` and `data/integration_queue.json` still describe Aug. 28 afternoon as the next replay/integration step and must be reconciled to mark PR #132 integrated and make Aug. 29 morning the next chronological verification gate.
- `data/integration_queue.json` should also gain a traceable Sep. 4 contributed-research record for PR #131 without rewriting older queue history.
- `docs/AGENT_HANDOFF.md` is append-only and materially behind current state. The available connector performs whole-file replacement rather than atomic append; do not reconstruct or truncate the 51 KB journal from partial output. Preserve the exact intended handoff in the coordination PR until a byte-preserving append can be performed safely.
- Later raw research must be reconciled only when chronology reaches it. External 310 provenance, root-artifact relocation, immutable Actions/dependency hardening, and direct public Pages render verification remain separate debt.

## Current operating priorities

1. Reconcile `docs/WORK_QUEUE.md` and `data/integration_queue.json` so Aug. 28 afternoon is marked integrated and Aug. 29 morning is the next source-health gate; add PR #131 as later contributed research.
2. Independently verify `intelligence/feeds/2026-08-29-source-health.json` from current `main`: recompute every protected fingerprint, compare each source with the exact latest canonical predecessor after PR #132, and preserve the raw snapshot unchanged.
3. If any Aug. 29 stored hash is invalid, create a separate provenance-preserving reconciliation rather than rewriting primary evidence. If hashes/predecessors are valid, stage only evidence-backed canonical replay records and matching registry timestamps.
4. Rerun source-history, registry, collection report, intelligence, site-data/Agent Operations, Core, Intelligence Source Report, and Daily Maintenance validation before merge.
5. Continue Aug. 29 afternoon -> Aug. 30 morning -> Aug. 30 afternoon -> Aug. 31 -> Sep. 1 -> Sep. 2 -> Sep. 3 -> Sep. 4 strictly in timestamp/source-overlap order.

## Coordination note

This pass started from actual `main` `578af9ad05391c94dac0c2959d8c2f30438377ce`, independently revalidated the Aug. 28 afternoon provenance-safe snapshot, staged exactly two canonical records and matching registry timestamps on PR #132, and changed the reconciliation regression to require canonical idempotence. PR #132's exact head passed Core, Source Report, and Daily Maintenance, `main` had not moved, and the PR was merged without stale-state reconciliation. Exact-merge Core and dashboard deployment then passed. No raw evidence, opportunity/case status, security authorization, tool maturity, or bespoke site HTML was changed.

## Next handoff

Repo Integrity / Build Integration should first reconcile the remaining queue surfaces, then inspect `intelligence/feeds/2026-08-29-source-health.json` against canonical Aug. 28 afternoon truth. Do not advance Aug. 29 until all observation fingerprints and predecessor links are independently verified; preserve later PRs as contributed evidence until their chronology point.
