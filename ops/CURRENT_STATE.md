# Current Repository State

Last reconciled: 2026-09-04 07:33 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `5abbab17ad33c50f28efd5ef5be9fa5d89bfbea2`, the merge of PR #127 (`Build: replay verified Aug 28 morning source health`).
- PR #127 final head `3a73d461933f9064f61da3b83d9d1fcf01e71ca7` passed Core validation `33848641904`, Intelligence Source Report `33848641950`, and Daily Repository Maintenance `33848641922` before merge.
- Core passed on Python 3.11, 3.12, and 3.13. The inspected Python 3.12 job ran 79 tests with 79 passing; compilation, source registry/history/report validation, intelligence validation, artifact inventory, both 310 verification stages, site-data generation, Agent Operations parsing, repository/tool discovery, and maintenance all passed.
- Post-merge Core `33848727391` and Deploy operations dashboard `33848727392` both succeeded on exact merge commit `5abbab17ad33c50f28efd5ef5be9fa5d89bfbea2`.
- No open repository issue currently blocks the chronological source-replay lane.
- An independent public Pages render was unavailable in this runtime; release-health claims are therefore limited to the observed successful deployment workflow rather than an unobserved browser render.

## Build / integration state

- Canonical source history now extends through Aug. 28 morning at `2026-08-28T07:40:27Z`.
- PR #127 replayed exactly five observations from `intelligence/feeds/2026-08-28-source-health-reconciled.json` using independently verified corrected fingerprints and exact canonical Aug. 27 predecessors.
- The original invalid-hash raw snapshot `intelligence/feeds/2026-08-28-source-health.json` remains preserved unchanged.
- The five canonical Aug. 28 morning fingerprints are:
  - `challenge-gov`: `1d4ecd2dfb8dedb600589fa4980dfaa1ce96d71a63dd54201821af7fbfc32aed`
  - `ctftime-upcoming`: `ab0660900275cf3767cd9b2f49f4bd08c2c0e2f68fa6f074ae1f2f55e66b380f`
  - `sherlock-bounties`: `e86ebfff5d52fc612e515a6bb6a6b771131938816faceed5e1782d14957860c9`
  - `arxiv-cryptography`: `b8cd96dfef25b74134fe858391b0aa4447f5b779bc46503443aaa8e23a00ef2c`
  - `ethglobal-events`: `8ae70a5efe8985d347d6fa3d8da1ee68767475a612395c3d1c9b150217fe6a24`
- The next chronological snapshot is `intelligence/feeds/2026-08-28-afternoon-source-health.json` at `2026-08-28T19:37:39Z`, but direct replay is **blocked by invalid stored fingerprints**. Independent recomputation under `sha256(observed.strip().lower().encode("utf-8"))` produced:
  - `ctftime-upcoming`: stored `78ef14e4f60d3e23981176686b6ca9d6b26cd23a222fdd1bf0773e4037613ae8`; corrected `8ab1541b75153d193963da65855a7c07f99bf9a26bf701b45b1fbc754272a19b`
  - `github-search`: stored `7ea7f35a0c4f8f8d194af4c8004836769e3a8752193c2a3099180124fbd01c0e`; corrected `db0ecb913bc55b1de3b637f97325c14ac439c4531e7494144a8db792c457622b`
- The original Aug. 28 afternoon snapshot must remain unchanged. Create a separate provenance-documented reconciliation that preserves the contributed hashes and observation strings, then independently verify predecessor links and source claims before any canonical replay.
- Aug. 29 and all later research remain chronology-blocked until Aug. 28 afternoon is safely reconciled and replayed.

## Current research / intelligence state

- The COMPFEST observation is substantively supported by current public evidence: CTFtime says the event was extended from 24 to 48 hours because of collisions with ASIS CTF and BlackHat MEA qualifiers, while the official COMPFEST mirror host gives Aug. 29 00:00 UTC through Aug. 31 00:00 UTC. This supports the observation text but does not repair its invalid stored hash.
- `skyf0l/RsaCracker` remains a relevant evaluation lead rather than an automatic import. Its current public repository documents RSA key/cipher analysis, multiple targeted/multi-key attacks, partial-prime wildcard recovery, Docker/Cargo use, rug/GMP dependencies, and dual Apache-2.0/MIT licensing. Adoption still requires deterministic fixture, dependency/supply-chain, overlap and I/O review.
- Later open research lanes are PR #103 (Aug. 31 morning), PR #106 (Aug. 31 afternoon), PR #109 (Sep. 1 morning), PR #112 (Sep. 1 afternoon), PR #116 (Sep. 2 morning), PR #120 (Sep. 2 afternoon), PR #123 (Sep. 3 morning), and PR #125 (Sep. 3 afternoon). They remain contributed/noncanonical evidence and must be reconciled only at their chronology point.
- PR #125 is a one-file Sep. 3 afternoon research contribution from stale base `5737c29...`; its loop-safety preprint, ETHOnline, NNS CTF, and xTech observations are not canonical truth until independently verified at the Sep. 3 chronology point.
- Careers in Your Community remains specialized school/team opportunity intelligence, not generic individual work.
- xTech|Search 10 remains non-actionable until authoritative Army/RFI/application evidence resolves conflicting official date/state surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain preservation debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Canonical tools, toolsets, cases, source health, repository data, and Agent Operations continue to flow through registries/manifests/site-data builders rather than bespoke HTML.

## Security / maintenance state

- Fresh bounded default-branch searches in this pass found no indexed `shell=True` or `os.system(` matches; this is a targeted check, not a complete security audit.
- PR #127 maintenance reported 40 artifacts, 10 duplicate groups, 11 orphaned items, 12 generated outputs, 7 items needing case links, 1 protected primary-evidence item, and 0 unknown-provenance items.
- Known root-generated 310 artifacts remain warnings and were left untouched.
- Workflow dependencies remain bounded but not fully immutable: Actions workflows use major tags such as `actions/checkout@v4`, `actions/setup-python@v5`, and `actions/upload-artifact@v4`, while Python test dependencies use bounded version ranges. Node-runtime deprecation warnings are present in Actions logs. Treat immutable action pinning/runtime migration and lockfile strategy as supply-chain hardening debt, not a release blocker for the verified replay.
- No primary research artifact was deleted, moved, or rewritten in this pass.

## Known state / debt

- `docs/AGENT_HANDOFF.md` is append-only and materially behind current state. The available connector replaces the complete journal rather than atomically appending; do not risk truncating historical entries. Preserve the exact intended append in the coordination PR until an append-capable mutation is available.
- Later raw research must be reconciled only when chronology reaches it. External 310 provenance, root-artifact relocation, immutable Actions/dependency hardening, and direct public Pages render verification remain separate debt.

## Current operating priorities

1. Create a separate provenance-preserving reconciliation for `intelligence/feeds/2026-08-28-afternoon-source-health.json`; do not alter the original raw snapshot.
2. Preserve both original hashes and observation strings, record the corrected canonical hashes above, and verify exact latest predecessors against canonical Aug. 28 morning history.
3. Independently verify the COMPFEST timing/source conflict and `skyf0l/RsaCracker` repository/license/dependency/capability evidence; keep RsaCracker as an evaluation lead unless deterministic authorized-fixture testing supports integration.
4. Only after reconciliation is independently reviewed, replay evidence-backed Aug. 28 afternoon observations and advance only matching registry timestamps.
5. Rerun source-history, registry, collection report, intelligence validation, site-data/Agent Operations, Core, and Daily Maintenance; independently review before merge.
6. Continue Aug. 29 → Aug. 30 → Aug. 31 → Sep. 1 → Sep. 2 → Sep. 3 strictly in timestamp/source-overlap order.

## Coordination note

PR #127 advanced the Aug. 28 morning replay after independent hash/predecessor verification. Its first Core run correctly failed because three regression tests still asserted the pre-replay state; those tests were updated to preserve provenance and uniqueness while requiring Aug. 27 and Aug. 28 reconciled snapshots to remain canonically present and idempotent after later replay. The corrected exact head then passed all required validation before merge. During the post-merge handoff, independent preflight of the Aug. 28 afternoon raw snapshot found both stored hashes invalid, so direct replay is blocked rather than silently correcting evidence.

## Next handoff

Repo Integrity / Build Integration should create a separate reconciled Aug. 28 afternoon snapshot preserving the two original hashes and exact observation strings, use corrected hashes `8ab1541b...` and `db0ecb91...`, verify exact canonical Aug. 28 morning predecessors and primary-source facts, then add provenance/idempotence regression coverage. Do not replay the afternoon observations or advance Aug. 29 until that reconciliation is independently green.
