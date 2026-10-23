# Current Repository State

Last reconciled: 2026-10-23 07:24 UTC
Default branch: `main`
Reconciled default-branch head: `e3406be6fe981feee5c2ec8c3c79cca924792e67`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot. A branch/PR containing this file has a newer commit by definition; compare material repository facts rather than treating that self-reference difference as drift.

## Verified health

- Current `main` is `e3406be6fe981feee5c2ec8c3c79cca924792e67`, merge of PR #211 (`Research: preserve Sep 30 Build With AI Basics lead`).
- PR #211 added exactly one raw research file, `intelligence/feeds/2026-09-30-source-health.json`, with 45 added lines and no deletions. It explicitly records `canonical_replay: false`, canonical cutoff `2026-08-29T19:40:52Z`, and next gate `2026-08-30T07:38:20Z`.
- Exact-main Core validation run `36687149015` succeeded Sep. 30. Oct. 11 exact-main Daily Repository Maintenance `38152171540` and Intelligence Source Report `38155338908` succeeded. Draft PR #212 prior head `e93df4945bc3b3cdd0e9687e18ca2f20cfb073fc` passed Core `37053379825` on Python 3.11/3.12/3.13; any new head requires fresh CI. Scheduled report success does not establish source freshness: all 16 sources remain due.
- No open repository issues were found. A bounded indexed-code search returned no matches for selected patterns, but it was incomplete: direct inspection confirms `subprocess` imports in `scripts/export_command_site_snapshot.py` and `tests/test_agent_ops_site_data.py`. Do not treat negative indexed-search results as an absence or security-audit claim.

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
- Earlier indexed-code searches returned no matches for selected patterns, but direct file inspection confirms `subprocess` imports and argument-vector subprocess calls. No repository-wide absence or comprehensive security-audit claim is supported.
- GitHub Actions have historically used major-version action tags such as `actions/checkout@v4` and `actions/setup-python@v5` rather than immutable commit SHAs; immutable action pinning remains supply-chain hardening debt until separately remediated and verified.
- Legacy root truthfulness/artifact debt remains separate work; preserve references and hashes before relocation.

## Coordination state

- `docs/WORK_QUEUE.md` still correctly points to Aug. 30 morning as the next replay gate.
- `data/integration_queue.json` remains the machine-readable integration inbox and must be preserved chronologically.
- `docs/AGENT_HANDOFF.md` is append-only; the required Oct. 11 handoff append remains blocked by connected write safety checks and must be completed before merging this draft PR.

## October 11 release and maintenance findings

- GitHub reported 34 open PRs, no open issues, and disabled branch protection. PR #212 remains 1 commit ahead / 0 behind `main`; PR #213 adds a research-only snapshot and does not overlap this coordination change.
- Canonical history has 78 unique source/timestamp pairs and all 16 registry last-check timestamps match history. The integration queue has 20 unique IDs: 11 integrated, 1 needs-integration, 8 blocked. There are 20 registered tools and one registered experimental toolset.
- Committed `site-data/status.json` and `site-data/collection-health.json` still report 77 checks, versus canonical 78. The Pages build regenerates data, but the last observed successful Pages run is Sep. 29 `36622688071` on older head `5f314d9a58a8cbc9431340d37f692dbea10dbb76`; current-main deployment and live browser rendering are unverified.
- README's `workspace/` navigation points to a directory absent from the tracked tree. Legacy `tools/scanning/web_scraper.py` generates simulated competition/prize entries and writes to `intelligence/feeds/scrape-results.json` despite a production banner. Isolate any truthfulness correction in a separate small PR with deterministic tests; do not treat generated examples as live intelligence.
- CI workflows use mutable major-version action tags; Oct. 11 source-report logs warn Node.js 20-targeted actions are being forced onto Node.js 24. Direct local clone/testing was unavailable because DNS resolution for github.com failed; do not claim a local test pass.

## Current research/intelligence state

- Canonical source history is 78 records with 78 unique source/time pairs, latest through 2026-08-29 afternoon; 16/16 source registry last-check timestamps match latest canonical history.
- All 16 registered intelligence sources are overdue. Oct. 22 Source Report `39806644419` succeeded on current main but does not constitute a fresh external source check.
- The protected Aug. 30 morning five-observation replay remains pending; contributed PRs #213 and #214 contain overlapping Code4rena observations and must not be promoted without reconciliation and independent evidence review.

## Known state / debt

- Committed `site-data/status.json` and `site-data/collection-health.json` report 77 history checks instead of 78 canonical; `site-data/cases.json` lists one case instead of two tracked structured cases.
- The committed repository browser snapshot omits five PwnSec case files and includes four untracked Python cache files. Site-data regeneration and live Pages rendering remain unverified on current main; last observed successful Pages deployment is Sep. 29 run `36622688071`.
- `scripts/build_agent_ops.py` expects the `Current research/intelligence state` and `Known state / debt` sections now supplied here; existing tests do not require these fields to be nonempty. Rebuild/CI is required before declaring the Agent Operations console fixed.
- Pages push triggers omit `intelligence/**`; README `workspace/` navigation has no tracked target; 11 of 20 tools use undocumented `verified` maturity. The PwnSec case still describes an expired Sep. 12–13 competition window as current.
- Preserve primary evidence and root artifact hashes before moving files. Filename screening found no obvious credential/private-key paths, but this is not a content secret audit. Actions use mutable tags; full supply-chain and security review remain outstanding.
- Local clone/test execution failed due DNS resolution; Oct. 22 Maintenance `39796200533` and Source Report `39806644419` passed on main. Last observed Core for PR #212 was `39013625784` before this documentation update; rerun exact-head Core.
- Open PRs: 35; standalone open issues: zero. Draft PR #212 is the coordination lane; stale research PRs must reconcile current main and preserve compatible contributions.

## Current operating priorities

1. Stage only the Aug. 30 morning native replay from `intelligence/feeds/2026-08-30-source-health.json`; do not mix later snapshots.
2. Require deterministic assertions for all five hashes, exact latest predecessors, five-record/five-registry scope, idempotence, and registry non-rewind behavior.
3. Require source-history/registry validation, Core matrix, Intelligence Source Report, Daily Maintenance, Agent Operations/site-data compatibility, semantic diff review, and no unresolved review threads before merge.
4. Require post-merge exact-main Core and Pages success before advancing to Aug. 30 afternoon.
5. Reconcile later research only from current `main`, preserving contributed evidence and expired/current-state distinctions.
6. Keep supply-chain pinning, root-artifact inventory, and legacy truthfulness cleanup as separate bounded objectives.

## Next handoff

Current `main` is `e3406be6fe981feee5c2ec8c3c79cca924792e67`, merge of research-only PR #211. Canonical source history remains through Aug. 29 afternoon. The Oct. 22 scheduled maintenance and intelligence workflows passed on main, but this Oct. 23 documentation head has not yet passed exact-head Core; no current-main Pages or live browser rendering is verified. The exact next action remains the protected Aug. 30 morning five-record/five-registry replay, followed by exact-head and post-merge Core/Pages verification before any Aug. 30 afternoon or September contribution advances canonical chronology.
