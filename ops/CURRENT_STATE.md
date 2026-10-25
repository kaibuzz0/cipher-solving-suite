# Current Repository State

Last reconciled: 2026-10-25 07:18 UTC
Default branch: `main`
Reconciled default-branch head: `e3406be6fe981feee5c2ec8c3c79cca924792e67`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot. A branch/PR containing this file has a newer commit by definition; compare material repository facts rather than treating that self-reference difference as drift.

## Verified health

- Current `main` is `e3406be6fe981feee5c2ec8c3c79cca924792e67`, merge of PR #211 (`Research: preserve Sep 30 Build With AI Basics lead`).
- PR #211 added exactly one raw research file, `intelligence/feeds/2026-09-30-source-health.json`, with 45 added lines and no deletions. It explicitly records `canonical_replay: false`, canonical cutoff `2026-08-29T19:40:52Z`, and next gate `2026-08-30T07:38:20Z`.
- Latest inspected default-branch scheduled checks (Oct. 24) passed: Daily Repository Maintenance `40097607199` and Intelligence Source Report `40101017704` on `e3406be6`. PR #212 previous exact head `8238a9c088c2ac321bccf43a640723326318c359` passed Core `40074131286` (86 tests each on Python 3.11/3.12/3.13) and Daily Maintenance `40074131253`, including compile and source/data validation. These checks predate this coordination update; new exact-head CI is required. Scheduled report success does not establish source freshness: all 16 sources remain due.
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
- All 16 registered intelligence sources are overdue. Oct. 24 Source Report `40101017704` succeeded on current main with 78 history checks and 14 marked changed; reporting does not constitute a fresh external source check.
- The protected Aug. 30 morning five-observation replay remains pending. Oct. 24 independent SHA-256 recomputation (implementation checked against the `abc` test vector) matched all five raw `observed.strip().lower()` fingerprints; each latest predecessor matched the current registry timestamp, ordering was forward, and none was already replayed. This is pre-replay evidence, not native replay/idempotence execution. Contributed PRs #213, #214, #215 and new Oct. 23 afternoon PR #216 overlap on Code4rena/source-health observations and must not be promoted without deduplication, chronology and independent review; PR #216's UGREEN/Qloo eligibility, deadlines and prizes remain contributed claims, not independently verified by Repo Integrity.

## Known state / debt

- Committed `site-data/status.json` and `site-data/collection-health.json` report 77 history checks instead of 78 canonical; `site-data/cases.json` lists one case instead of two tracked structured cases.
- The committed repository browser snapshot omits five PwnSec case files and includes four untracked Python cache files. Site-data regeneration and live Pages rendering remain unverified on current main; last observed successful Pages deployment is Sep. 29 run `36622688071`.
- `scripts/build_agent_ops.py` expects the `Current research/intelligence state` and `Known state / debt` sections now supplied here; existing tests do not require these fields to be nonempty. Rebuild/CI is required before declaring the Agent Operations console fixed.
- Pages push triggers omit `intelligence/**`; README `workspace/` navigation has no tracked target; 11 of 20 tools use undocumented `verified` maturity. The PwnSec case still describes an expired Sep. 12–13 competition window as current.
- Preserve primary evidence and root artifact hashes before moving files. Filename screening found no obvious credential/private-key paths, but this is not a content secret audit. Actions use mutable tags; full supply-chain and security review remain outstanding.
- Local clone/test execution remains blocked by DNS resolution. Oct. 23 main Maintenance `39967810647` and Source Report `39978318791` passed. PR #212 head `26c00d59aa2ba05c4bcea77e654eebe6698b2a71` passed Core `40011485695` (86 tests per Python 3.11/3.12/3.13) and Maintenance `40011485660`; any later documentation commit requires new exact-head CI. Actions logs still report Node.js deprecations.
- Open PRs: 38 at Oct. 24 afternoon inspection (including new research-only PR #217); standalone open issues: zero. Draft PR #212 is the coordination lane; stale research PRs must reconcile current main and preserve compatible contributions.

## October 24 afternoon verification (19:24 UTC)

- Current default-branch head remains `e3406be6fe981feee5c2ec8c3c79cca924792e67`; recent commits on main still end with PR #211. Draft PR #212 was ten commits ahead and zero behind main before this update; its diff remains limited to `ops/CURRENT_STATE.md` and append-only `docs/AGENT_HANDOFF.md`, with zero unresolved review threads.
- Oct. 24 main Daily Maintenance `40097607199` and Intelligence Source Report `40101017704` passed. The Oct. 24 PR #212 prior head `8238a9c0...` passed Core `40074131286` (86 tests each on Python 3.11, 3.12 and 3.13) and Maintenance `40074131253`. CI logs contain Node.js 20 compatibility/deprecation warnings; these are not a failure. Revalidate exact PR head after this change.
- Re-read operating contracts, current state, work queue, handoff, integration inbox, catalog, current tree, recent commits, open PRs/issues, CI workflows and Pages workflow. Independently parsed canonical history: 78 records, zero duplicate source/time keys, all 16 registry last-check timestamps match latest canonical history. Twenty tools are registered (11 use undocumented `verified` maturity), one toolset catalogued, queue 11 integrated/1 needs-integration/8 blocked, two tracked case manifests but only one committed generated site case.
- New PR #217 preserves Oct. 24 GitLab Life After Code / Codex x TwitchCon and source-health research in a single raw snapshot. Its 127 added lines do not mutate canonical registry/history, opportunities, cases, or coordination files. Official-rule/prize/deadline/eligibility assertions are **contributed claims not independently reverified in this integrity pass**. Code4rena observations overlap PRs #213-#216; deduplicate before any later canonical replay. Total open PRs 38; standalone issues zero.
- Committed site-data is still Sep. 8 vintage (77 history entries versus 78 canonical; one generated case versus two tracked); repository browser includes four `.pyc` entries and omits five tracked PwnSec files. The Pages workflow regenerates site-data on deployment but excludes `intelligence/**` from push paths. Latest successful Pages workflow in the most recent 100 runs is Sep. 29 `36622688071` on a different main SHA. Current-main deployment and live browser rendering are **unverified** (public site fetch unavailable).
- The Agent Operations builder expects research/debt headings now present only on PR #212; regression tests do not assert nonempty sections. README links to untracked `workspace/`. Bounded inspection confirms the command-site exporter invokes subprocess with argument arrays, while its output path accepts absolute/parent paths and its refresh logic does not detect stale existing data; no exploit or comprehensive secret audit is claimed. Local git clone failed host DNS resolution; no local pytest or native replay ran. Preserve evidence and hashes.

## October 25 integrity verification (07:18 UTC)

- Default `main` remains `e3406be6fe981feee5c2ec8c3c79cca924792e67` (last commit Sep. 30). Draft coordination PR #212 head `04b83ce3e22c2dd5b8ca810db7e0083b8cbcd032` was 12 ahead / zero behind main, with only `docs/AGENT_HANDOFF.md` and `ops/CURRENT_STATE.md` changed and no unresolved review threads before this update. The repository has **39 open PRs and zero standalone open issues**; the new PR is research-only #218.
- Exact-head PR #212 Core `40125306106` succeeded on Python 3.11/3.12/3.13, and Maintenance `40125306075` succeeded; both predate this documentation edit. New PR #218 Core `40126622982` also succeeded. Latest main scheduled Maintenance `40097607199` and Intelligence Report `40101017704` passed Oct. 24; no newer main run was observed. Do not claim the new PR #212 head validated until fresh checks complete.
- Independently parsed current-main canonical data: **78** source-history checks with **78** unique source/timestamp pairs; **16/16** source registry last-check times equal latest history; **20** registered tools with all source paths tracked (11 use undocumented `verified` maturity), one catalogued `repo-factory` toolset with manifest and existing entrypoint, and **20** unique integration-queue IDs (11 integrated, one needs-integration, eight blocked). All 16 intelligence sources remain overdue. The Aug. 30 morning native replay, idempotence, and non-rewind tests were **not** executed in this pass.
- PR #218 contributes one `intelligence/feeds/2026-10-24-afternoon-source-health.json` research snapshot (163 added lines). Its claimed six observation hashes, Build With AI/RenderJuice prizes, dates, eligibility and participant readiness are **contributed claims**, not independently reverified here. PR #218 does not change canonical history, registry freshness, cases, tools, or coordination. Code4rena/source-health overlap with PRs #213-#217 requires chronology-aware deduplication before integration.
- Committed site-data remains stale: Sep. 8 status/collection-health report 77 checks versus 78 canonical, and one case versus two tracked manifests. Repository browser includes four untracked Python cache files and omits the five PwnSec case files. The Pages workflow regenerates site data but its push paths exclude `intelligence/**`; the newest Pages run in the latest 100 runs was successful Sep. 29 `36622688071` on an older commit, so current-main deployment and live browser rendering are **not verified**. Agent Operations headings exist on PR #212, but tests do not assert nonempty research/debt fields.
- Bounded Markdown audit checked 31 relative links across six operating/navigation files; README `workspace/` was the sole missing tracked target. Filename-only screening of 259 tracked blobs found no obvious secret/private-key paths; **not** a content secret audit. The registered tool paths and toolset manifest/entrypoint exist. Local clone/pytest/direct-script execution failed to start because `github.com` DNS resolution was unavailable; GitHub Actions results are reported separately. No research evidence, hashes, canonical registries, or governance contracts were modified.
- **Next action:** Review PR #212's final two-file diff and fresh exact-head Core/Maintenance, then merge only after green checks and review. Verify post-merge exact-main Core and Pages, and stage the protected Aug. 30 morning five-record/five-registry native replay with fingerprint/predecessor, uniqueness, idempotence and non-rewind gates. Address generated-data freshness and Agent Operations assertions through separate small PRs.

## Current operating priorities

1. Stage only the Aug. 30 morning native replay from `intelligence/feeds/2026-08-30-source-health.json`; do not mix later snapshots.
2. Require deterministic assertions for all five hashes, exact latest predecessors, five-record/five-registry scope, idempotence, and registry non-rewind behavior.
3. Require source-history/registry validation, Core matrix, Intelligence Source Report, Daily Maintenance, Agent Operations/site-data compatibility, semantic diff review, and no unresolved review threads before merge.
4. Require post-merge exact-main Core and Pages success before advancing to Aug. 30 afternoon.
5. Reconcile later research only from current `main`, preserving contributed evidence and expired/current-state distinctions.
6. Keep supply-chain pinning, root-artifact inventory, and legacy truthfulness cleanup as separate bounded objectives.

## Next handoff

At the Oct. 25 07:18 UTC check, main remains `e3406be6` with 78 unique source-history checks, 16/16 matching registry timestamps and all 16 sources overdue. PR #212 previous exact head `04b83ce3` passed Core `40125306106` and Maintenance `40125306075`, but this update needs fresh exact-head validation. New research-only PR #218 brings open PRs to 39; its external claims remain unpromoted. Pages deployment on current main remains unverified (last observed success Sep. 29 `36622688071`); committed site data remains stale. Review/merge the bounded coordination PR only after fresh checks, verify exact-main Core/Pages, then independently stage only the Aug. 30 morning five-record/five-registry replay with native idempotence and non-rewind verification. Preserve all research evidence and keep site-data/Agent Operations repairs separate.
