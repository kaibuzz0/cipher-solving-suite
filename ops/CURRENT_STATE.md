# Current Repository State

Last reconciled: 2026-10-01 19:21 UTC
Default branch: `main`
Reconciled default-branch head: `e3406be6fe981feee5c2ec8c3c79cca924792e67`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot. A branch/PR containing this file has a newer commit by definition; compare material repository facts rather than treating that self-reference difference as drift.

## Verified health

- Current `main` is `e3406be6fe981feee5c2ec8c3c79cca924792e67`, merge of PR #211 (`Research: preserve Sep 30 Build With AI Basics lead`).
- PR #211 added exactly one raw research file, `intelligence/feeds/2026-09-30-source-health.json`, with 45 added lines and no deletions. It explicitly records `canonical_replay: false`, canonical cutoff `2026-08-29T19:40:52Z`, and next gate `2026-08-30T07:38:20Z`.
- Commit-associated workflow/status surfaces queried in this pass exposed no PR-triggered runs or legacy status contexts for the merge commit; do not infer failed CI from those empty surfaces, and do not invent an exact-head release claim from them.
- No open repository issues were found. Bounded default-branch code search returned no matches for `shell=True`, `os.system`, `subprocess`, or `BEGIN PRIVATE KEY`.

## Canonical source / integration state

- Canonical source history remains at 78 checks through Aug. 29 afternoon, `2026-08-29T19:40:52Z`.
- PR #148 remains the canonical Aug. 29 morning replay: five records at `2026-08-29T07:38:35Z` for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`.
- PR #171 adds exactly one later canonical record for `ethglobal-events` at `2026-08-29T19:40:52Z`, fingerprint `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179`.
- `docs/WORK_QUEUE.md` continues to identify Aug. 30 morning as the next chronological replay gate. The next eligible snapshot is `intelligence/feeds/2026-08-30-source-health.json` at `2026-08-30T07:38:20Z`.
- Protected Aug. 30 morning scope remains exactly five history additions and five corresponding registry timestamp advances. Do not mix Aug. 30 afternoon or later September research into that replay.
- Independently preserved Aug. 30 morning observation fingerprints remain:
  - `challenge-gov`: `0570aab0fa0e07a2a97db33360d99e65c1a97260df3b71eb88dd753bd3885a75`
  - `ctftime-upcoming`: `1867c7ba3ec559aac232f71474198bd8eef43eb9b5ce0a71689930794044510e`
  - `sherlock-bounties`: `f691382d715d50fcf471cb70e074abbbd1d00b0335a3fa4046ed2b99dbe1b986`
  - `arxiv-cryptography`: `708237551c62ad0e0e7e1b9a823dff2c946745a99c6d279ba894aaf284c00a99`
  - `ethglobal-events`: `06a6fd437851f24e1b0513421f1389620ee201851f396b5220ac04031a06310a`

## Sep. 30 contributed research review

- PR #211 preserves Devpost Build With AI: Basics as raw contributed research only.
- The snapshot records a Sep. 22-Oct. 26 build window, a $2,500 advertised cash-prize pool, project/originality/open-source/demo requirements, and explicit third-party authorization/licensing boundaries.
- Participant-specific registration, jurisdiction eligibility, rule amendments, clean new-project/pre-existing-work separation, and third-party SDK/API/data authorization remain unresolved.
- It does not advance canonical history or registry freshness and does not create a case, opportunity, tool, payout claim, or testing authorization.

## Concurrent / stale contribution state

- Open research PRs including #208, #207, #205, #202 and older lanes predate current `main`; they are contributed evidence, not merge-ready truth solely because their external facts are newer.
- Any stale branch that becomes eligible must reconcile current `main`, preserve compatible evidence from both sides, rerun validation on the reconciled head, and document conflict resolution.
- No open research PR may leapfrog the Aug. 30 morning replay gate.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; normal tools/toolsets/cases/intelligence/evidence must surface through canonical registries/manifests/site-data builders rather than bespoke `site/index.html` edits.
- No new tool/toolset/case was introduced by PR #211.
- Structured active cases remain authorization-bounded. Repository evidence must not be interpreted as an external solve, private key, payout, participant registration, team state, or permission to test a public target.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not silently delete or relocate evidence.
- Exact-main Core, Daily Maintenance, and Intelligence Source Report are green, but these do not substitute for a comprehensive secret/static-analysis audit.
- This pass repeated bounded default-branch searches and found no `shell=True`, `os.system`, `subprocess`, or `BEGIN PRIVATE KEY` matches; this is not a comprehensive secret/static-analysis audit.
- GitHub Actions have historically used major-version action tags such as `actions/checkout@v4` and `actions/setup-python@v5` rather than immutable commit SHAs; immutable action pinning remains supply-chain hardening debt until separately remediated and verified.
- Legacy root truthfulness/artifact debt remains separate work; preserve references and hashes before relocation.

## Coordination state

- `docs/WORK_QUEUE.md` still correctly points to Aug. 30 morning as the next replay gate.
- `data/integration_queue.json` remains the machine-readable integration inbox and must be preserved chronologically.
- `docs/AGENT_HANDOFF.md` is append-only; this reconciliation appends a new entry rather than rewriting historical handoffs.

## Current operating priorities

1. Stage only the Aug. 30 morning native replay from `intelligence/feeds/2026-08-30-source-health.json`; do not mix later snapshots.
2. Require deterministic assertions for all five hashes, exact latest predecessors, five-record/five-registry scope, idempotence, and registry non-rewind behavior.
3. Require source-history/registry validation, Core matrix, Intelligence Source Report, Daily Maintenance, Agent Operations/site-data compatibility, semantic diff review, and no unresolved review threads before merge.
4. Require post-merge exact-main Core and Pages success before advancing to Aug. 30 afternoon.
5. Reconcile later research only from current `main`, preserving contributed evidence and expired/current-state distinctions.
6. Keep supply-chain pinning, root-artifact inventory, and legacy truthfulness cleanup as separate bounded objectives.

## Next handoff

Current `main` is `e3406be6fe981feee5c2ec8c3c79cca924792e67`, merge of research-only PR #211. Canonical source history remains through Aug. 29 afternoon. This reconciliation intentionally makes no new exact-head CI/Pages claim from empty commit-status surfaces. The exact next action remains the protected Aug. 30 morning five-record/five-registry replay, followed by exact-head and post-merge Core/Pages verification before any Aug. 30 afternoon or September contribution advances canonical chronology.
