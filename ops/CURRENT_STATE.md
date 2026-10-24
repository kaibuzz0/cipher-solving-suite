# Current Repository State

Last reconciled: 2026-10-24 07:23 UTC
Default branch: `main`
Reconciled default-branch head: `e3406be6fe981feee5c2ec8c3c79cca924792e67`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot. A branch/PR containing this file has a newer commit by definition; compare material repository facts rather than treating that self-reference difference as drift.

## Verified health

- Current `main` is `e3406be6fe981feee5c2ec8c3c79cca924792e67`, merge of PR #211 (`Research: preserve Sep 30 Build With AI Basics lead`).
- PR #211 added exactly one raw research file, `intelligence/feeds/2026-09-30-source-health.json`, with 45 added lines and no deletions. It explicitly records `canonical_replay: false`, canonical cutoff `2026-08-29T19:40:52Z`, and next gate `2026-08-30T07:38:20Z`.
- Latest inspected default-branch scheduled checks (Oct. 23) passed: Daily Repository Maintenance `39967810647` and Intelligence Source Report `39978318791` on `e3406be6`. PR #212 exact head `26c00d59aa2ba05c4bcea77e654eebe6698b2a71` passed Core `40011485695` (86 tests each on Python 3.11/3.12/3.13) and Daily Maintenance `40011485660`, including compile and source/data validation. Any further PR commit requires fresh exact-head CI. Scheduled report success does not establish source freshness: all 16 sources remain due.
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
- `docs/AGENT_HANDOFF.md` is append-only; the Oct. 23 integrity handoff is now present on PR #212. Earlier Oct. 11 write failures are historical, not an active handoff blocker. Exact-head CI must be rerun after any further edits.

## October 11 release and maintenance findings

- GitHub reported 34 open PRs, no open issues, and disabled branch protection. PR #212 remains 1 commit ahead / 0 behind `main`; PR #213 adds a research-only snapshot and does not overlap this coordination change.
- Canonical history has 78 unique source/timestamp pairs and all 16 registry last-check timestamps match history. The integration queue has 20 unique IDs: 11 integrated, 1 needs-integration, 8 blocked. There are 20 registered tools and one registered experimental toolset.
- Committed `site-data/status.json` and `site-data/collection-health.json` still report 77 checks, versus canonical 78. The Pages build regenerates data, but the last observed successful Pages run is Sep. 29 `36622688071` on older head `5f314d9a58a8cbc9431340d37f692dbea10dbb76`; current-main deployment and live browser rendering are unverified.
- README's `workspace/` navigation points to a directory absent from the tracked tree. Legacy `tools/scanning/web_scraper.py` generates simulated competition/prize entries and writes to `intelligence/feeds/scrape-results.json` despite a production banner. Isolate any truthfulness correction in a separate small PR with deterministic tests; do not treat generated examples as live intelligence.
- CI workflows use mutable major-version action tags; Oct. 11 source-report logs warn Node.js 20-targeted actions are being forced onto Node.js 24. Direct local clone/testing was unavailable because DNS resolution for github.com failed; do not claim a local test pass.

## Current research/intelligence state

- Canonical source history is 78 records with 78 unique source/time pairs, latest through 2026-08-29 afternoon; 16/16 source registry last-check timestamps match latest canonical history.
- All 16 registered intelligence sources are overdue. Oct. 23 Source Report `39978318791` succeeded on current main with 78 history checks and 14 marked changed; reporting does not constitute a fresh external source check.
- The protected Aug. 30 morning five-observation replay remains pending. Oct. 24 independent SHA-256 recomputation (implementation checked against the `abc` test vector) matched all five raw `observed.strip().lower()` fingerprints; each latest predecessor matched the current registry timestamp, ordering was forward, and none was already replayed. This is pre-replay evidence, not native replay/idempotence execution. Contributed PRs #213, #214, #215 and new Oct. 23 afternoon PR #216 overlap on Code4rena/source-health observations and must not be promoted without deduplication, chronology and independent review; PR #216's UGREEN/Qloo eligibility, deadlines and prizes remain contributed claims, not independently verified by Repo Integrity.

## Known state / debt

- Committed `site-data/status.json` and `site-data/collection-health.json` report 77 history checks instead of 78 canonical; `site-data/cases.json` lists one case instead of two tracked structured cases.
- The committed repository browser snapshot omits five PwnSec case files and includes four untracked Python cache files. Site-data regeneration and live Pages rendering remain unverified on current main; last observed successful Pages deployment is Sep. 29 run `36622688071`.
- `scripts/build_agent_ops.py` expects the `Current research/intelligence state` and `Known state / debt` sections now supplied here; existing tests do not require these fields to be nonempty. Rebuild/CI is required before declaring the Agent Operations console fixed.
- Pages push triggers omit `intelligence/**`; README `workspace/` navigation has no tracked target; 11 of 20 tools use undocumented `verified` maturity. The PwnSec case still describes an expired Sep. 12–13 competition window as current.
- Preserve primary evidence and root artifact hashes before moving files. Filename screening found no obvious credential/private-key paths, but this is not a content secret audit. Actions use mutable tags; full supply-chain and security review remain outstanding.
- Local clone/test execution remains blocked by DNS resolution. Oct. 23 main Maintenance `39967810647` and Source Report `39978318791` passed. PR #212 head `26c00d59aa2ba05c4bcea77e654eebe6698b2a71` passed Core `40011485695` (86 tests per Python 3.11/3.12/3.13) and Maintenance `40011485660`; any later documentation commit requires new exact-head CI. Actions logs still report Node.js deprecations.
- Open PRs: 37 at Oct. 24 inspection (including new PR #216); standalone open issues: zero. Draft PR #212 is the coordination lane; stale research PRs must reconcile current main and preserve compatible contributions.

## Current operating priorities

1. Stage only the Aug. 30 morning native replay from `intelligence/feeds/2026-08-30-source-health.json`; do not mix later snapshots.
2. Require deterministic assertions for all five hashes, exact latest predecessors, five-record/five-registry scope, idempotence, and registry non-rewind behavior.
3. Require source-history/registry validation, Core matrix, Intelligence Source Report, Daily Maintenance, Agent Operations/site-data compatibility, semantic diff review, and no unresolved review threads before merge.
4. Require post-merge exact-main Core and Pages success before advancing to Aug. 30 afternoon.
5. Reconcile later research only from current `main`, preserving contributed evidence and expired/current-state distinctions.
6. Keep supply-chain pinning, root-artifact inventory, and legacy truthfulness cleanup as separate bounded objectives.

## Next handoff

Current `main` is `e3406be6fe981feee5c2ec8c3c79cca924792e67`, merge of research-only PR #211. Canonical source history remains through Aug. 29 afternoon (78 records). Oct. 23 main Maintenance `39967810647` and Source Report `39978318791` passed; PR #212 exact prior head `26c00d59` passed Core `40011485695` (86 tests per Python 3.11/3.12/3.13) and Maintenance `40011485660`. New Oct. 24 coordination edits require fresh exact-head CI. PR #216 is additional unpromoted research and overlaps #213/#214/#215 on Code4rena. The protected Aug. 30 morning snapshot passed five independent SHA-256/predecessor/ordering preflight checks but has not been natively replayed. No current-main Pages deployment or live browser rendering is verified. Next: verify PR #212 final diff and exact-head Core/Maintenance, review and merge only if green; then stage the Aug. 30 morning five-record/five-registry native replay with idempotence/non-rewind and post-merge Core/Pages checks before later chronology.
