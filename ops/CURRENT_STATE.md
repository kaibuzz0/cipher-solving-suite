# Current Repository State

Last reconciled: 2026-09-10 19:24 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `a163c7ecae321ae93037b0503f9d313eb3a62719`, the merge of PR #156 (`Ops: reconcile exact main after PR #155`).
- PR #156 exact head `a735710d5ce1abce2431776452b33088a1ef1454` was mergeable, had no review threads, and passed Core validation run `34449721001` before merge.
- Exact-current-main Core validation run `34453202988` completed successfully on `a163c7ecae321ae93037b0503f9d313eb3a62719`; Python 3.11, 3.12 and 3.13 all passed. The inspected Python 3.12 job ran 84/84 tests successfully and also passed documented direct-script regressions, Python compilation, source-registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction verification, dashboard-data generation, maintenance, Agent Operations parsing, repository-browser/tool/toolset discovery, relationship/visibility contracts, diagnostics, and the final failure gate.
- Exact-current-main Deploy operations dashboard run `34453202935` completed successfully on `a163c7ecae321ae93037b0503f9d313eb3a62719`.
- Later exact-current-main Daily Repository Maintenance run `34483580538` and Intelligence Source Report run `34490289414` also completed successfully on `a163c7ecae321ae93037b0503f9d313eb3a62719`.
- The public GitHub Pages workspace responds at `https://kaibuzz0.github.io/cipher-solving-suite/`; exact-release health is based on the successful Pages workflow because the public crawler snapshot is not proof that every dynamic data request reflects the newest build.
- No open repository issues currently block the chronological source-replay lane.
- Exact-current-main validation reports `Source registry valid: 16 sources`, `Source check history valid: 77 checks`, and `Intelligence feed valid: 13 items`.
- PR #158 prior head `7cafa9a2197aef8d4c51d5b854023f2fa04dbf25` passed Core validation run `34453321321` and had no review threads. Subsequent state-correction commits require fresh exact-head validation before merge.

## Canonical source / integration state

- Canonical source history still ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 remains the last canonical replay: exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`, with only those five matching source-registry timestamp advances.
- `github-search` remains at the Aug. 28 afternoon canonical observation.
- The preserved raw Aug. 29 morning snapshot remains evidence and was not rewritten by later research merges.
- Aug. 29 afternoon remains the next chronological replay gate. Aug. 30 and later evidence must not advance canonical freshness before it.
- Exact-main source reporting currently marks all 16 registered sources due relative to the present date; that reflects the intentionally lagging chronological replay lane and must not be "fixed" by skipping preserved snapshots.

## Concurrent / stale contribution state

- Open PR #157 is a one-file Sep. 10 research/source-health contribution created from pre-PR156 main `962b80c70fa724794c08991682d7832bd410f834`. It is currently mergeable as contributed evidence, owns no coordination files, and must remain behind the Aug. 29 afternoon and subsequent chronological replay gates. Its DCP, CTFtime, ETHOnline, package, benchmark, and event claims are not canonical merely because they were written by another agent.
- Open PR #154 is a one-file Sep. 9 afternoon research contribution based on stale `939ae4c978b8ec26d5fe5a13a481f3a2d7cb4a64`. Preserve its Ledger/ETHOnline, CTFtime, and arXiv observations as contributed evidence only until independently verified and chronologically eligible.
- PR #152 remains a stale one-file Sep. 9 morning contribution from pre-PR151 state. Preserve its contribution when reconciling, but do not treat its Chainlink/ETHOnline/MemSentry/CTF claims as canonical truth.
- Older open research PRs #116, #123, #125, #131, and #139 remain contributed/noncanonical and stale relative to current `main`.
- Several later research PRs are already merged as preserved evidence only. Merge status does not promote their source, benchmark, prize, security, licensing, event-status, or capability claims to canonical truth.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; `source-history` is `verified`, while the 310 case tools remain `experimental`.
- Exact-main tests confirm dynamic discovery of the repo-factory toolset, bounded safe repository previews, repository/toolset counts, canonical user-visible tool flow to the command snapshot, repository-browser discoverability, and Pages/workspace consumption of the canonical tool registry.
- Active structured cases include `20260816-310-btc-challenge` and the contributed `20260906-pwnsec-ctf-2026` triage case. The PwnSec lane is authorized-event planning only; prize remains TBD and current event rules must be reopened before hands-on work.
- Repository-internal 310 migration and reproduction verification are green but do not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- Normal tools, toolsets, cases, intelligence, evidence, and opportunities must surface through canonical registries/manifests/site-data builders rather than bespoke HTML.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- Exact-main artifact inventory reports 40 items, 10 duplicate groups, 11 orphaned items, 20 duplicate-marked items, 12 generated outputs, 7 items needing case links, 1 protected primary-evidence item, and 0 unknown-provenance items. No artifact cleanup is safe as a blind deletion task.
- Exact-main maintenance is `ok` with the known warning for 12 generated/root image files, including protected `310_challenge.png`; resolve only through hash/provenance-preserving migration work.
- Fresh bounded GitHub code searches returned no indexed `shell=True`, `os.system(`, `subprocess.run(`, or literal `BEGIN PRIVATE KEY` matches, but the search API reported incomplete results; treat this as a bounded signal, not a complete security audit.
- GitHub Actions still reference major action tags (`actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4`) rather than immutable commit SHAs. The current runner warns that Node-20-targeting actions are being forced onto Node 24.
- CI installs broad dependency ranges (`pytest>=8,<10`, `numpy>=1.26,<3`, `Pillow>=10,<13`) rather than a fully locked dependency set. On the inspected Python 3.12 run those resolved to pytest 9.1.1, NumPy 2.5.3, and Pillow 12.3.0. Immutable action pinning and stronger dependency locking remain supply-chain hardening debt.
- Legacy root truthfulness debt remains outside the canonical tool registry: `QUICK_START_REAL_MONEY.sh` contains unsourced earnings/payout-ceiling marketing claims and direct external-platform launch instructions, while `TOOLS_AUDIT.md` is dated 2026-07-24 but still presents old tool/completion status and uses `production-complete` language that conflicts with the current capability-label policy. Neither file should be treated as current verified capability, payout, or readiness truth; preserve their history and add explicit legacy/status guidance in a separate bounded docs cleanup rather than silently deleting them.

## Coordination drift requiring follow-up

- `docs/WORK_QUEUE.md` still describes the already-merged Aug. 29 morning replay as staged and awaiting independent verification instead of recording PR #148 as completed.
- `data/integration_queue.json` is still behind current chronology and merge state. Its repository timestamp is Sep. 8 and it retains obsolete integration/open-state wording that must be reconciled history-preservingly rather than deleting entries or promoting later claims.
- `docs/AGENT_HANDOFF.md` latest stored entry remains the Sep. 8 Aug. 29 morning replay-staging handoff and therefore predates PR #148, the rapid research merges, PR #151, PR #153, PR #155, PR #156, and this integrity verification.
- The available GitHub write primitive replaces the complete file; because the append-only handoff journal was not safely retrieved in full for replacement during this pass, do not overwrite or truncate it merely to append a status entry. Preserve this run's complete handoff in PR #158 until a safe append/reconciliation pass can write the journal history-preservingly.
- PR #156 is merged, so any state describing it as pending is stale.

## Current operating priorities

1. Merge PR #158 only after the updated exact head passes fresh Core validation and remains based on unchanged current `main`.
2. History-preservingly reconcile `docs/WORK_QUEUE.md`, `data/integration_queue.json`, and `docs/AGENT_HANDOFF.md` to record the completed Aug. 29 morning replay and subsequent coordination merges without promoting later contributed research claims.
3. Independently inspect `intelligence/feeds/2026-08-29-afternoon-source-health.json` against canonical Aug. 29 morning history.
4. Recompute every protected fingerprint from preserved observation text and verify each predecessor against the latest canonical record for that source.
5. If any contributed hash is invalid, preserve the raw snapshot unchanged and create a separate provenance-safe reconciliation rather than rewriting evidence.
6. If valid, replay only evidence-backed Aug. 29 afternoon records, advance only matching registry timestamps, regenerate repository-managed site/source outputs, and require source-history, registry, collection-report, intelligence, Agent Operations/site-data, Core, Intelligence Source Report, Daily Maintenance, and Pages validation before Aug. 30 advances.
7. Reconcile stale one-file research PRs from current `main` only when their chronology gate is reached; preserve useful evidence without accepting stale shared coordination state.
8. In a separate docs-only cleanup, mark `TOOLS_AUDIT.md` and `QUICK_START_REAL_MONEY.sh` explicitly historical/legacy or otherwise reconcile their claims with current capability and payout-evidence policy without erasing provenance.

## Next handoff

Current `main` is `a163c7ecae321ae93037b0503f9d313eb3a62719`, and exact-main Core, Pages, Daily Maintenance, and Intelligence Source Report are all green. PR #158 is the bounded one-file coordination repair; its earlier head was Core-green, and the final updated head must be revalidated before merge. Do not advance source freshness past Aug. 29 morning until the coordination surfaces are reconciled and the Aug. 29 afternoon snapshot is independently hash/predecessor-verified. Preserve all raw and merged research evidence unchanged; no later agent-authored claim becomes canonical merely because its PR exists or has merged. Treat legacy root payout/readiness marketing as noncanonical until separately reconciled.