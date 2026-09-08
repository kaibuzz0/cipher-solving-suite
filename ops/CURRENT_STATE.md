# Current Repository State

Last reconciled: 2026-09-08 07:21 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `901f481293fec25907f3f06a03069f4583c3028b`, the merge of PR #145 (`Ops: reconcile state after PR #143 merge`).
- Exact-main Core validation run `34157763456` completed successfully on `901f481293fec25907f3f06a03069f4583c3028b`.
- Exact-main Deploy operations dashboard run `34157763396` completed successfully on the same commit.
- No open repository issues currently block the chronological source-replay lane; the current open issue-list entries are pull requests.

## Build / integration state

- Canonical source history ends at Aug. 28 afternoon, `2026-08-28T19:37:39Z`.
- PR #132 canonically replayed exactly two reconciled Aug. 28 afternoon observations and preserved the original contributed/raw evidence unchanged.
- PR #134 (`Build: verify Aug 29 morning source replay readiness`) added deterministic readiness coverage only; it did not replay Aug. 29.
- `tests/test_aug29_source_readiness.py` independently locks the five Aug. 29 morning hashes, exact predecessors, chronology, uniqueness/idempotence, and matching registry timestamp behavior.
- The next canonical source write remains a separate bounded Aug. 29 morning replay: exactly five `2026-08-29T07:38:35Z` source-history records and only the five matching source-registry `last_checked_at` advances.
- Aug. 29 afternoon, Aug. 30 morning/afternoon, and later research remain blocked from canonical source-history advancement until Aug. 29 morning is replayed and independently verified.

## Current research / intelligence state

- Later research remains contributed/noncanonical evidence until chronology reaches it.
- Open research lanes include PR #103/#106 (Aug. 31), PR #109/#112 (Sep. 1), PR #116/#120 (Sep. 2), PR #123/#125 (Sep. 3), PR #131/#136 (Sep. 4), PR #139 (Sep. 5), PR #141 (Sep. 6), PR #144 (Sep. 7 morning), and PR #146 (Sep. 7 afternoon).
- PR #144 (`Research: preserve Sep 7 source health and CONTINUITY lead`) changes only `intelligence/feeds/2026-09-07-source-health.json`, was opened from stale base `a9526e36315ac82ad0d47c38db59c46d12d32e23`, and remains contributed evidence until independently re-verified and reconciled at the correct chronology point.
- PR #146 (`Research: preserve Sep 7 afternoon CTF-Agent integration blockers`) changes only `intelligence/feeds/2026-09-07-afternoon-source-health.json` and was opened from stale base `045bd6241c088f387c9a88ad348c382bb1ba0bbe`. Its CTF-Agent maintenance, license/provenance, authorization-model, scope-guard, and prompt-policy-sanitizer statements remain contributed evidence until independently re-verified at the correct chronology point. Do not import/register external framework code merely because it is public or self-labels platform-domain families as allowed.
- PR #141 and the older research branches likewise predate current `main`; preserve compatible research when reconciling them, but do not let stale branches advance canonical source state.
- Public bounty/program/event listings remain discovery evidence only and are not authorization to test unrelated targets.

## 310 case / artifact state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal extraction reproducibility remains verified; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, payout, or puzzle solve.
- Known artifact migration/orphan/duplicate debt remains preservation work. Do not delete or relocate primary evidence without preserving hashes, provenance, references, and reproducibility.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Exact-main CI validates canonical tool discovery, repository-browser/tool/toolset paths, generated dashboard data, and Agent Operations parsing.
- Normal tools/toolsets/cases/intelligence/evidence must flow through canonical registries/manifests/site-data builders rather than bespoke HTML.

## Security / maintenance state

- Prior bounded default-branch searches found no indexed `shell=True`, `os.system(`, or `subprocess.run(` occurrences. This remains a targeted check, not a complete security audit.
- Exact-main Core compilation, source registry/history/report, intelligence, artifact inventory, 310 verification, dashboard-data generation, and maintenance gates are green via run `34157763456`.
- Workflow dependencies still use major-version action tags such as `actions/checkout@v4`, `actions/setup-python@v5`, and `actions/upload-artifact@v4` rather than immutable commit pins. Action pinning and stronger dependency locking remain supply-chain hardening debt, not a release blocker for this coordination-only pass.
- No primary research artifact, source-history record, source-registry timestamp, tool maturity label, case status, opportunity status, or authorization boundary is changed by this reconciliation.

## Known coordination debt

- `docs/WORK_QUEUE.md` is behind chronology: its P2 source-health row still describes the already-completed Aug. 28 afternoon replay rather than the verified Aug. 29 morning replay gate.
- `data/integration_queue.json` is behind chronology: the Aug. 28 item remains `needs-integration` and the Aug. 29 item remains blocked on Aug. 28 afternoon even though PR #132 completed that replay. Preserve queue history and update statuses/evidence rather than replacing prior entries.
- `docs/AGENT_HANDOFF.md` is materially stale: the stored append-only journal ends with the Aug. 26 PR #67 integrity entry. It must be appended history-preservingly; do not truncate or reconstruct earlier entries.
- PR #144 and PR #146 are stale relative to current `main` and must be reconciled at their chronology points without discarding their one-file contributed evidence.

## Current operating priorities

1. Merge this bounded post-PR145 coordination update only after fresh exact-head CI is green.
2. Reconcile `docs/WORK_QUEUE.md`, `data/integration_queue.json`, and the append-only handoff history without deleting or rewriting prior provenance.
3. Stage a separate Aug. 29 morning canonical replay using the verified raw snapshot, writing exactly five `2026-08-29T07:38:35Z` history records with predecessor links locked by `tests/test_aug29_source_readiness.py`.
4. Advance only the five corresponding source-registry timestamps; preserve all raw research evidence unchanged.
5. Run source-history, source-registry, collection-report, intelligence, site-data/Agent Operations, Core, Intelligence Source Report, and Daily Maintenance validation on the replay head.
6. Only after the replay is independently verified may Aug. 29 afternoon advance, followed by Aug. 30 morning/afternoon and later research PRs in timestamp/source-overlap order.
7. Reconcile PR #144 and PR #146 only when chronology reaches Sep. 7 and independently re-verify any time-sensitive source, event, benchmark, capability, license/provenance, or authorization-model claim before promotion.

## Coordination note

This integrity pass began from actual default-branch commit `901f481293fec25907f3f06a03069f4583c3028b`, re-read README/governance/automation/maintenance/current-state/work-queue/integration-queue/toolset surfaces, inspected the latest available append-only handoff entries, open PRs/issues, and exact-main Actions. PR #145 had merged but `ops/CURRENT_STATE.md` still described pre-merge `045bd624...`, creating a concrete coordination mismatch. PR #146 also appeared from that older base. Exact-main Core and Pages workflows are green. This reconciliation changes coordination truth only; it does not promote a solve, payout, security finding, tool maturity, source freshness, license claim, or authorization claim.

## Next handoff

Repo Integrity / Build Integration should merge this coordination update only after fresh exact-head validation is green. Then perform a history-preserving work-queue/integration-queue/handoff reconciliation and the separate bounded Aug. 29 morning canonical replay. Do not advance Aug. 29 afternoon or later contributed research until the five-record morning replay and matching registry timestamps are independently verified green.
