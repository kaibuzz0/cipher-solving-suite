# Current Repository State

Last reconciled: 2026-09-14 19:20 UTC
Default branch: `main`
Reconciled default-branch head: `5d78a1dd81176ec0a1f4cca705e130065b94dea0`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot. A branch/PR containing this file may have a newer commit by definition; compare material repository facts rather than treating that self-reference difference as drift.

## Verified health

- Current `main` is `5d78a1dd81176ec0a1f4cca705e130065b94dea0`, the merge of PR #175 (`Research: preserve Sep 14 OATS source-health lead`).
- Exact-main Core validation `34820583429` succeeded on `5d78a1dd81176ec0a1f4cca705e130065b94dea0` across Python 3.11, 3.12 and 3.13.
- The Core matrix successfully ran the test suite, Python compilation, intelligence source-registry/history/report validation, intelligence-feed validation, artifact inventory, 310 migration/reproduction verification, dashboard-data generation, maintenance diagnostics, and the final validation gate.
- Later Daily Repository Maintenance `34865045068` and Intelligence Source Report `34869246753` also succeeded on the same exact main commit.
- PR #175 changed only `intelligence/feeds/2026-09-14-source-health.json`. The Pages workflow does not trigger for `intelligence/**`-only changes, so no new Pages deployment was expected from that merge; the previously deployed site remains the release surface until a Pages-triggering canonical/data/docs/ops change lands.
- No standalone open GitHub issue currently blocks the chronological replay lane.
- `main` remains unprotected and required status-check enforcement is disabled.

## Canonical source / integration state

- Canonical source history remains at 78 checks through Aug. 29 afternoon, `2026-08-29T19:40:52Z`.
- PR #148 remains the canonical Aug. 29 morning replay: five records at `2026-08-29T07:38:35Z` for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`.
- PR #171 adds exactly one later canonical record for `ethglobal-events` at `2026-08-29T19:40:52Z`, fingerprint `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179`, predecessor `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`, `change_state=changed`.
- `docs/WORK_QUEUE.md` and `data/integration_queue.json` agree that Aug. 30 morning is the next chronological replay gate; the Aug. 30 morning/afternoon contribution remains `needs-integration`, with morning first.
- The Aug. 29 raw snapshots and all later contributed research snapshots remain preserved unchanged.

## Aug. 30 morning independent readiness check

- `intelligence/feeds/2026-08-30-source-health.json` is the next eligible snapshot at `2026-08-30T07:38:20Z`.
- Repo Integrity previously recomputed all five preserved observation SHA-256 fingerprints and they exactly match the contributed values:
  - `challenge-gov`: `0570aab0fa0e07a2a97db33360d99e65c1a97260df3b71eb88dd753bd3885a75`
  - `ctftime-upcoming`: `1867c7ba3ec559aac232f71474198bd8eef43eb9b5ce0a71689930794044510e`
  - `sherlock-bounties`: `f691382d715d50fcf471cb70e074abbbd1d00b0335a3fa4046ed2b99dbe1b986`
  - `arxiv-cryptography`: `708237551c62ad0e0e7e1b9a823dff2c946745a99c6d279ba894aaf284c00a99`
  - `ethglobal-events`: `06a6fd437851f24e1b0513421f1389620ee201851f396b5220ac04031a06310a`
- Latest canonical predecessors are, respectively, `9e063815d1081f098c97ab5981f71b4c2e94d00edba6ca61198d1d9b2e762045`, `33b5c83409f9f2704f19483a69440ce82525b23c05a7f5ef2d401ac816c0f2ce`, `6aaa4c2de88200e0be6144cb024734167d513c9c79a1b11d6f283958bbd2b19f`, `246032d40532baab6948400a0678b2421b6342024d13ae16258ac80583bb26c3`, and the Aug. 29 afternoon ETHGlobal fingerprint `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179`.
- No Aug. 30 canonical write has been made by this integrity pass. The replay scope remains exactly five history additions at `2026-08-30T07:38:20Z` and five matching registry timestamp advances, with no later-snapshot replay mixed in.

## Sep. 14 contributed research review

- PR #175 merged the single raw snapshot `intelligence/feeds/2026-09-14-source-health.json` from exact prior main `a7b1f685e212d0302e546f5b915fa03433f18ac8`; it did not change canonical source history, registry freshness, intelligence, opportunities, cases, tools/toolsets, integration queues, or Pages HTML.
- The snapshot preserves four observations: `arxiv-cryptography`, `github-search`, `ctftime-upcoming`, and `challenge-gov`. It explicitly labels OATS benchmark/runtime measurements as author-reported and unreproduced and does not treat public security/event/challenge listings as testing authorization.
- Repo Integrity independently reopened arXiv:2609.12001 and confirmed the paper title and its reported 66,192-version measurement, 100-sample audit with 92% detector precision, live-agent sandbox study, and 64-case obfuscation benchmark. Those results remain external author claims, not repository-verified capability.
- The public `pheo-ai/open-agent-trust-system` repository exists. No external code was imported or executed by this pass. Any future integration must pin an exact external revision and reproduce benign validator/reference-runtime behavior locally before capability promotion.
- This Sep. 14 evidence must not leapfrog Aug. 30 morning/afternoon or intervening overlapping snapshots in canonical source chronology.

## Concurrent / stale contribution state

- PR #174 remains open from pre-PR175 main (`e61b39d26aaaf46459ac1d45a7621a5d3a1854d9`) and contributes Sep. 13 afternoon raw research only. It must reconcile current `main` before integration and must preserve its already-expired ETHOnline/PwnSec timing as historical evidence rather than current actionability.
- PR #161 and PR #163 remain stale-base research contributions and require current-main reconciliation before merge.
- Older open research PRs #152, #154 and #157 remain contributed evidence lanes and must be reconciled only when chronology/source-overlap order permits.
- No open research PR may leapfrog the Aug. 30 morning replay gate merely because its external facts are newer.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; normal tools/toolsets/cases/intelligence/evidence must surface through canonical registries/manifests/site-data builders rather than bespoke `site/index.html` edits.
- Core validation confirms dashboard-data generation and the repository's normal discovery/visibility contracts remain healthy on current `main`.
- Structured active cases remain authorization-bounded. Repository evidence must not be interpreted as an external puzzle solve, private key, payout, registration, team/faction state, or permission to test a public target.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- Current exact-main maintenance and validation are green; this does not substitute for a comprehensive secrets/static-analysis audit.
- GitHub Actions still use major-version action tags such as `actions/checkout@v4` and `actions/setup-python@v5` rather than immutable commit SHAs, and CI installs broad dependency ranges rather than a lockfile. Supply-chain drift remains hardening debt.
- `main` remains unprotected with required status-check enforcement disabled; release discipline depends on workflow verification and review practice.
- Legacy root truthfulness debt remains in `QUICK_START_REAL_MONEY.sh` and `TOOLS_AUDIT.md`; preserve history and reconcile those claims separately.

## Coordination state

- `docs/WORK_QUEUE.md` and `data/integration_queue.json` remain mutually consistent on the next replay gate: Aug. 30 morning.
- `docs/AGENT_HANDOFF.md` remains append-only and its latest entry predates PR #173/#175. The available contents write operation replaces the whole file, while retrieval of the large journal is truncated; this integrity pass does not risk reconstructing or truncating historical provenance. The complete handoff for this pass is therefore carried in the coordination PR description until an append-safe/full-file path is available.
- No queue rewrite is required solely for PR #175 because it is preserved raw research and the chronological integration inbox already identifies Aug. 30 morning/afternoon as the active gate. Later research remains noncanonical until chronology reaches it.

## Current operating priorities

1. Stage only the Aug. 30 morning native replay from `intelligence/feeds/2026-08-30-source-health.json`; do not mix Aug. 30 afternoon or later Sep. research.
2. Require deterministic replay/readiness assertions for all five hashes, exact latest predecessors, five-record/five-registry scope, idempotence, and registry non-rewind behavior.
3. Require source-history/registry validation, Core matrix, Intelligence Source Report, Daily Maintenance, Agent Operations/site-data compatibility, semantic diff review, and no unresolved review threads before merge.
4. Require post-merge exact-main Core and Pages success before advancing to Aug. 30 afternoon.
5. Reconcile PR #174 and other later research only from current `main`, preserving contributed evidence and expired/current-state distinctions.
6. Evaluate OATS only as a later research lead: pin exact revision, run benign local tests, and compare against existing authorization/provenance contracts before proposing integration.
7. Continue supply-chain/action pinning and legacy root truthfulness cleanup only as separate bounded objectives that preserve evidence.

## Next handoff

Current `main` is `5d78a1dd81176ec0a1f4cca705e130065b94dea0`, the merge of research-only PR #175. Exact-main Core `34820583429`, Daily Maintenance `34865045068`, and Intelligence Source Report `34869246753` are green. PR #175 preserved Sep. 14 OATS/source-health research without changing canonical freshness; the material OATS paper facts were independently reopened but its implementation and benchmarks remain unreproduced. Canonical source history remains through Aug. 29 afternoon, and Aug. 30 morning remains the exact next action: stage only the five-record/five-registry native replay, validate exact head, merge only if clean and non-stale, then require exact-main Core and Pages before considering Aug. 30 afternoon.
