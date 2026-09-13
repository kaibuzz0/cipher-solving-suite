# Current Repository State

Last reconciled: 2026-09-13 07:23 UTC
Default branch: `main`
Reconciled default-branch head: `c1acd2ae06b9240c0bfe4bbab0fca1a27df806f8`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot, not a self-referential assertion that the commit containing this file must equal the observed base SHA. A merge of this reconciliation will create a newer commit by definition. That SHA difference alone is not coordination drift; re-open this file only when substantive repository facts, health, chronology, risks, or priorities change.

## Verified health

- Current `main` is `c1acd2ae06b9240c0bfe4bbab0fca1a27df806f8`, the merge of PR #168 (`Research: reconcile Sep 12 source health after PwnSec start`).
- PR #168 exact head `c8f4c25a38a7f471e951ea8b8b53687d3ce9a6d3` passed Core validation `34714948001` before merge; the Python 3.12 lane ran 86/86 tests passing, and Python 3.11/3.13 matrix lanes also succeeded.
- Exact-main Core `34745069661` and Deploy operations dashboard / Pages `34745069671` succeeded on `c1acd2ae06b9240c0bfe4bbab0fca1a27df806f8` after merge.
- Core covers direct-script regressions, Python compilation, source-registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction verification, site-data generation, maintenance diagnostics, repository-browser/tool/toolset discovery, and canonical tool visibility.
- Source registry remains valid with 16 sources; source-check history remains valid with 77 checks; intelligence feed remains valid with 13 items.
- No standalone open GitHub issues currently block the chronological replay lane.
- Governance documents remain aligned that current repository state outranks agent memory, external AI output is contributed work rather than automatically trusted truth, primary evidence must be preserved, and normal tools/toolsets/cases/intelligence/evidence must flow through canonical registries/manifests/site-data builders.

## Canonical source / integration state

- Canonical source history still ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 remains the last canonical replay: exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`, with only those five matching source-registry timestamp advances.
- Aug. 29 afternoon remains the next canonical replay gate; neither PR #168 nor its Sep. 12 research snapshot changed canonical history or source-registry freshness.
- The preserved Aug. 29 afternoon snapshot contains exactly one `ethglobal-events` observation at `2026-08-29T19:40:52Z`.
- The protected expected fingerprint is `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179`; its latest canonical predecessor is Aug. 29 morning ETHGlobal fingerprint `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`.
- `tests/test_aug29_afternoon_source_readiness.py` protects the exact snapshot hash, predecessor linkage, canonical uniqueness, and absent-or-exact idempotence contract before replay.
- `docs/WORK_QUEUE.md` correctly records PR #148 as completed and Aug. 29 afternoon as the next replay gate.
- `data/integration_queue.json` is being reconciled separately on this integrity branch: preserve queue history, update stale PR/status language, and keep merged research distinct from canonical source replay.

## Concurrent / stale contribution state

- PR #168 is now merged research evidence. Its xTech, ETHOnline, Code4rena, and PwnSec claims were independently checked against current primary sources before merge, but the merge still does not advance canonical source chronology.
- PR #165 is closed unmerged and superseded by PR #168; do not revive its expired pre-event action language.
- PR #161 remains open xTech|Search 10 research from a stale base and must be reconciled from current `main` before merge.
- PR #163 remains a stale-base Sep. 11 afternoon EBL-Core research contribution; preserve its one-file evidence but require current-main reconciliation and fresh validation before merge.
- Older open research PRs remain contributed evidence lanes and must be reconciled only when chronology/source-overlap order permits.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; `source-history` remains verified and the 310 solver/analyzer/reproduction tools remain explicitly `experimental`.
- Structured active cases remain `20260816-310-btc-challenge` and `20260906-pwnsec-ctf-2026`.
- The 310 case remains internal evidence only and does not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- PwnSec remains an authorization-bounded event case. PR #168 records the live event window as Sep. 12 14:00 UTC through Sep. 13 14:00 UTC and explicitly keeps participant registration/team/faction state unknown; no payout, registration, or eligibility claim is inferred.
- User-facing repository state continues through generated site data; normal additions must not require bespoke `site/index.html` edits.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- Current artifact inventory remains preservation-sensitive: 40 items, 10 duplicate groups, 11 orphaned items, 12 generated outputs, 7 needing case links, one protected primary-evidence item, and zero unknown-provenance items. Inventory validation passes; cleanup must remain hash/provenance preserving.
- Bounded indexed searches in this pass found no `shell=True`, `os.system(`, `subprocess.run(`, or literal `PRIVATE KEY` matches. This is not a comprehensive secret scan or static-analysis audit.
- GitHub Actions still use major-version action tags (`actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4`) rather than immutable commit SHAs. Current runners warn those Node-20-targeting actions are being forced onto Node 24; immutable pinning/major-version refresh remains supply-chain hardening debt.
- CI installs broad dependency ranges (`pytest>=8,<10`, `numpy>=1.26,<3`, `Pillow>=10,<13`) rather than a lockfile, so dependency drift remains possible.
- `main` remains unprotected with required status-check enforcement disabled; release discipline depends on workflow verification and review practice.
- Legacy root truthfulness debt remains in `QUICK_START_REAL_MONEY.sh` and `TOOLS_AUDIT.md`; preserve history and reconcile those claims separately.

## Coordination drift requiring follow-up

- `data/integration_queue.json` was still dated Sep. 8 and incorrectly described PR #148's Aug. 29 morning replay as pending. This integrity branch updates that entry while preserving the afternoon gate and corrects stale `open` language for later research PRs that subsequently merged as evidence only.
- `docs/AGENT_HANDOFF.md` still ends with the Sep. 11 post-PR159 entry and needs an append-only record covering PR #166/#167 readiness state, PR #168 independent verification/merge, current-main CI/Pages, queue reconciliation, and the exact Aug. 29 afternoon next action.
- Stale research PRs must be reconciled from current `main` and rerun through validation before merge.
- Do not reopen this file merely because merging this reconciliation creates a newer SHA; use the reconciled-base field plus material-state checks.

## Current operating priorities

1. Finish the history-preserving `data/integration_queue.json` reconciliation and append the integrity handoff without deleting prior entries.
2. Execute the repository-native replay of `intelligence/feeds/2026-08-29-afternoon-source-health.json`, expecting exactly one `ethglobal-events` history addition at `2026-08-29T19:40:52Z` and one matching registry timestamp advance.
3. Require the readiness regression plus source-history, registry, collection-report, intelligence, Agent Operations/site-data, Core, Intelligence Source Report, Daily Maintenance, and Pages validation before Aug. 30 advances.
4. Independently verify the replay diff and exact-head CI before merge; preserve the raw snapshot unchanged.
5. Reconcile later research PRs only after current-main conflict review and according to chronology/source overlap.
6. Separately harden Actions/dependency pinning and reconcile legacy truthfulness documents without erasing provenance.

## Next handoff

Current reconciled `main` is `c1acd2ae06b9240c0bfe4bbab0fca1a27df806f8`. PR #168 was independently checked against current primary sources, passed exact-head Core `34714948001`, merged, and exact-main Core `34745069661` plus Pages `34745069671` succeeded. The merge preserved later Sep. 12 research and the PwnSec case update but did not advance canonical source history. Canonical history still ends at Aug. 29 morning. Reconcile the integration inbox and append this handoff safely, then execute only the bounded Aug. 29 afternoon replay using fingerprint `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179` with predecessor `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`, and require full validation before Aug. 30 or later research advances.
