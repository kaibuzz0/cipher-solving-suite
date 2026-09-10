# Current Repository State

Last reconciled: 2026-09-10 07:19 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `962b80c70fa724794c08991682d7832bd410f834`, the merge of PR #155 (`Ops: record PR #153 merge and current replay gate`).
- Exact-main Core validation run `34398567688` completed successfully on `962b80c70fa724794c08991682d7832bd410f834`; Python 3.11, 3.12 and 3.13 all passed. The inspected Python 3.12 job ran 84/84 tests successfully and also passed direct-script regressions, Python compilation, source-registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction verification, dashboard-data generation, maintenance, Agent Operations parsing, repository-browser/tool/toolset discovery, relationship/visibility contracts, diagnostics, and the final failure gate.
- Exact-main Deploy operations dashboard run `34398567728` also completed successfully on `962b80c70fa724794c08991682d7832bd410f834`.
- No open repository issues currently block the chronological source-replay lane.
- The Core run reports `Source registry valid: 16 sources`, `Source check history valid: 77 checks`, and `Intelligence feed valid: 13 items`.

## Canonical source / integration state

- Canonical source history still ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 remains the last canonical replay: exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`, with only those five matching source-registry timestamp advances.
- `github-search` remains at the Aug. 28 afternoon canonical observation.
- The preserved raw Aug. 29 morning snapshot remains evidence and was not rewritten by later research merges.
- Aug. 29 afternoon remains the next chronological replay gate. Aug. 30 and later evidence must not advance canonical freshness before it.

## Concurrent / stale contribution state

- Open PR #154 is a one-file Sep. 9 afternoon research contribution based on stale `939ae4c978b8ec26d5fe5a13a481f3a2d7cb4a64`; GitHub currently reports it non-mergeable against current `main`. Preserve its Ledger/ETHOnline, CTFtime, and arXiv observations as contributed evidence only until independently verified and chronologically eligible.
- PR #152 remains a stale one-file Sep. 9 morning contribution from pre-PR151 state. Preserve its contribution when reconciling, but do not treat its Chainlink/ETHOnline/MemSentry/CTF claims as canonical truth.
- Older open research PRs #116, #123, #125, #131, and #139 remain contributed/noncanonical and stale relative to current `main`.
- Several later research PRs are already merged as preserved evidence only. Merge status does not promote their source, benchmark, prize, security, licensing, event-status, or capability claims to canonical truth.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; `source-history` is `verified`, while the 310 case tools remain `experimental`.
- Active structured cases include `20260816-310-btc-challenge` and the contributed `20260906-pwnsec-ctf-2026` triage case. The PwnSec lane is authorized-event planning only; prize remains TBD and current event rules must be reopened before hands-on work.
- Repository-internal 310 reproduction remains green but does not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- Normal tools, toolsets, cases, intelligence, evidence, and opportunities must surface through canonical registries/manifests/site-data builders rather than bespoke HTML.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- The exact-main artifact inventory reports 40 items, 10 duplicate groups, 11 orphaned items, 20 duplicate-marked items, 12 generated outputs, 7 items needing case links, 1 protected primary-evidence item, and 0 unknown-provenance items. No artifact cleanup is safe as a blind deletion task.
- Maintenance remains `ok` with the known warning for 12 generated/root image files, including protected `310_challenge.png`; resolve only through hash/provenance-preserving migration work.
- Fresh bounded default-branch searches found no indexed `shell=True` or `os.system(` use; this is not a complete security audit.
- GitHub Actions still reference major action tags (`actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4`) rather than immutable commit SHAs. The current runner also warns that Node-20-targeting actions are being forced onto Node 24.
- CI installs broad dependency ranges (`pytest>=8,<10`, `numpy>=1.26,<3`, `Pillow>=10,<13`) rather than a fully locked dependency set. Immutable action pinning and stronger dependency locking remain supply-chain hardening debt.

## Coordination drift requiring follow-up

- `docs/WORK_QUEUE.md` still describes the already-merged Aug. 29 morning replay as staged and awaiting independent verification instead of recording PR #148 as completed.
- `data/integration_queue.json` still marks the Aug. 29 morning item `needs-integration` and contains stale `open` wording for several research PRs that were subsequently merged as preserved evidence (including #103, #106, #109, #112, and #120). Reconcile statuses history-preservingly rather than deleting entries or promoting claims.
- `docs/AGENT_HANDOFF.md` latest stored entry remains the Sep. 8 Aug. 29 morning replay-staging handoff and therefore predates PR #148, the rapid research merges, PR #151, PR #153, and PR #155. Append a new entry without truncating prior journal history.
- PR #155 itself is now merged, so any state describing its coordination snapshot as pending is stale.

## Current operating priorities

1. History-preservingly reconcile `docs/WORK_QUEUE.md`, `data/integration_queue.json`, and `docs/AGENT_HANDOFF.md` to record the completed Aug. 29 morning replay and subsequent coordination merges without promoting later contributed research claims.
2. Independently inspect `intelligence/feeds/2026-08-29-afternoon-source-health.json` against canonical Aug. 29 morning history.
3. Recompute every protected fingerprint from preserved observation text and verify each predecessor against the latest canonical record for that source.
4. If any contributed hash is invalid, preserve the raw snapshot unchanged and create a separate provenance-safe reconciliation rather than rewriting evidence.
5. If valid, replay only evidence-backed Aug. 29 afternoon records, advance only matching registry timestamps, regenerate repository-managed site/source outputs, and require source-history, registry, collection-report, intelligence, Agent Operations/site-data, Core, Intelligence Source Report, Daily Maintenance, and Pages validation before Aug. 30 advances.
6. Reconcile stale one-file research PRs from current `main` only when their chronology gate is reached; preserve useful evidence without accepting stale shared coordination state.

## Next handoff

First complete the history-preserving coordination reconciliation after PR #155 and the completed Aug. 29 morning replay. Then independently verify and process Aug. 29 afternoon as the next chronological canonical replay gate. Preserve all raw and merged research evidence unchanged; no later agent-authored claim becomes canonical merely because its PR exists or has merged.
