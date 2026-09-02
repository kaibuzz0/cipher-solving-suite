# Current Repository State

Last reconciled: 2026-09-02 07:22 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `222bd054551c44845fa50c1837e379cc1dc6ab53`, the independently reviewed merge of PR #114 (`Build: replay reconciled Aug 27 source health`).
- PR #114 exact final head `cef3541926fb93245de0fa43b851d2b0918ed2e6` was mergeable, had no review threads, and passed Core validation `33554018254`, Intelligence Source Report `33554018512`, and Daily Repository Maintenance `33554018586` before merge.
- Core passed Python 3.11/3.12/3.13. The inspected Python 3.12 job collected 77 tests and passed all 77, then passed compilation, source registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction, site-data generation, maintenance, and the final failure gate.
- No open repository issues were found. Open research PRs are #103, #106, #109, and #112; all are later one-file contributed research lanes with bases older than current `main` and remain noncanonical until reconciled at their chronology points.
- Post-merge workflow runs for `222bd054...` had not surfaced through the connected commit-run query at this reconciliation point. The exact tested PR head is therefore the current release-verification basis; do not claim an unobserved post-merge run.

## Build / integration state

- Canonical source history now advances through Aug. 27 at `2026-08-27T19:39:25Z`.
- PR #114 replayed only `intelligence/feeds/2026-08-27-source-health-reconciled.json`. The original PR #75 raw file remains unchanged with its five invalid contributed hashes and preserved provenance.
- Exactly five Aug. 27 history records are canonical and exactly five matching source `last_checked_at` timestamps advanced: `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`.
- Repo Integrity independently recomputed all five corrected fingerprints from the preserved observation strings and matched the replay values exactly; all five Aug. 26 predecessor fingerprints also matched canonical history.
- `data/source_check_history.json` advanced to the replay timestamp. Registry-level `data/intelligence_sources.json.updated_at` correctly remained at the already-newer `2026-08-27T20:02:00Z`, so the replay did not rewind registry state.
- The Aug. 27 regression verifies original-vs-reconciled provenance, corrected hashes, canonical uniqueness, exact predecessor/change state, five registry timestamp advances, registry non-rewind, and byte-for-byte idempotence through both library and documented direct-script replay.
- The next canonical replay lane is Aug. 28 morning (`intelligence/feeds/2026-08-28-source-health.json`), followed by Aug. 28 afternoon. Later Aug. 29, Aug. 30, Aug. 31, and Sep. 1 research remains chronology-blocked.

## Current research / intelligence state

- PR #103 contributes Aug. 31 morning research; PR #106 contributes Aug. 31 afternoon ETHOnline research; PR #109 contributes Sep. 1 morning source/tool research; PR #112 contributes Sep. 1 afternoon ETHOnline/xTech research. Their original CI can establish that their contributed files were syntactically/repository-compatible on stale bases, not that their source claims are current canonical truth.
- PR #112 head `bf905e8159e58739ef68999c2c511ca4731de764` passed Core validation `33551030545` but GitHub reports it non-mergeable against current `main`; preserve its one-file evidence and reconcile later rather than overwriting newer state.
- Careers in Your Community remains specialized school/team opportunity intelligence, not generic individual work.
- xTech|Search 10 remains non-actionable until authoritative Army/RFI/application evidence resolves the conflicting official date/state surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal extraction reproducibility remains established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Artifact inventory on PR #114 reported 40 items, 10 duplicate groups, 11 orphaned items, 12 generated outputs, seven items needing case links, one protected primary-evidence item, and zero unknown-provenance items. Root generated/legacy artifacts remain preservation debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- No tool/toolset maturity or registration change and no bespoke site HTML was introduced by PR #114.
- Core regression coverage confirms Agent Operations parsing, canonical tool visibility, Command Site snapshots, repository-browser discovery, repo-factory toolset discovery, and generated site-data continue to consume canonical repository state.
- GitHub Pages direct API state was not available through the connected endpoint in this pass. Site-data generation passed on the exact PR #114 head; do not claim an independently observed post-merge browser render until one is obtained.

## Security / dependency health

- Fresh bounded code searches found no default-branch matches for `shell=True`, `os.system(`, or `subprocess.Popen`.
- Daily Maintenance was green and reported the known root generated-file warning without secret-like filename failures.
- CI uses supported major action tags (`actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4`) and bounded Python dependency ranges rather than immutable action SHAs/full lockfiles. Keep this as non-blocking supply-chain hardening debt; do not represent the environment as fully pinned.

## Known state / debt

- Safely mark the Aug. 27 integration-queue item integrated and add missing machine-readable records for Sep. 1 PR #109 and PR #112 without dropping prior queue history.
- Keep `docs/WORK_QUEUE.md` synchronized so Aug. 28 morning is the active chronological replay rather than the already-completed Aug. 27 replay.
- Preserve later one-file research contributions and reconcile them onto current `main` only when chronology reaches them; rerun validation after reconciliation.
- `docs/AGENT_HANDOFF.md` must receive an append-only entry for this merge/reconciliation without truncating historical entries.
- External 310 provenance, root artifact relocation, and supply-chain/runtime hardening remain separate debt.

## Current operating priorities

1. Verify and canonically process `intelligence/feeds/2026-08-28-source-health.json` before the Aug. 28 afternoon snapshot.
2. Independently recompute protected hashes and verify each source's Aug. 27 predecessor; replay only evidence-backed observations and advance only matching registry timestamps.
3. Rerun source-history/registry/report/intelligence/site-data/Agent Operations/Core/Maintenance validation and independently review the reconciled head before merge.
4. Continue Aug. 28 afternoon, Aug. 29 morning/afternoon, Aug. 30 morning/afternoon, Aug. 31 morning/afternoon, Sep. 1 morning, then Sep. 1 afternoon in timestamp/source-overlap order.
5. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

PR #114 was merged only after independent fingerprint/predecessor verification, exact-head CI review, no-review-thread confirmation, and registry non-rewind inspection. It preserved the original invalid-hash PR #75 evidence and did not touch later research, opportunities, active cases, tool maturity, security authorization, or bespoke website markup. Open later research branches are stale by chronology/base and must preserve compatible current-main state when eventually reconciled.

## Next handoff

Build Integration should take Aug. 28 morning as the next bounded replay lane. Verify the snapshot against canonical Aug. 27 history, preserve any raw evidence and uncertainty, stage only exact evidence-backed history/registry changes, run direct-script/idempotence plus full repository validation, and hand the final head back to Repo Integrity for independent review before Aug. 28 afternoon is allowed to advance.