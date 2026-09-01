# Current Repository State

Last reconciled: 2026-09-01 07:21 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `2b697ea245262971353f29208e1e3fde41e628e2`, the merge of PR #107 (`Ops: preserve green post-PR104 integrity state`).
- PR #107 merged the exact previously tested head `ffdeb89ebd69e0d6e46748f34cd4aa56ebc6c128`; that head passed Core validation `33430182872` before merge.
- Post-merge Core validation `33433612292` and Deploy operations dashboard `33433612321` both succeeded on exact merge commit `2b697ea...`.
- The exact-main Core matrix passed Python 3.11, 3.12 and 3.13. The inspected Python 3.12 job collected 77 tests and passed all 77, plus compilation, source registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction verification, dashboard-data generation, maintenance and the final gate.
- Two open pull requests exist: PR #103 (`Research: preserve Aug 31 source health and agent-evidence paper`) and PR #106 (`Research: preserve Aug 31 afternoon ETHOnline evidence`). Both are one-file raw-research contributions, both are currently reported mergeable, and both passed their own Core validation heads (`33369490812` and `33432441873`). Their bases predate current `main`, so they remain contributed/noncanonical evidence pending current-main reconciliation and chronological integration.
- No open issues were found.
- Source-health observations through Aug. 26 remain canonical. Aug. 27 and later raw/reconciled research has not been replayed canonically.

## Build / integration state

- PR #107 contained only the post-PR104 current-state reconciliation. It did not advance source history, source-registry freshness, primary evidence, tool maturity, cases, opportunities, authorization state or bespoke website HTML.
- PR #101 previously resolved the Aug. 27 fingerprint-provenance blocker without modifying the original PR #75 raw snapshot. `intelligence/feeds/2026-08-27-source-health.json` remains preserved unchanged.
- `intelligence/feeds/2026-08-27-source-health-reconciled.json` remains the only eligible Aug. 27 replay surface. It preserves the exact PR #75 observation strings and original contributed hashes while recording independently recomputed canonical fingerprints separately.
- Canonical Aug. 27 replay has **not** occurred. PR #107's post-merge build follow-up attempted a checkout but could not resolve `github.com`; it correctly refused to reconstruct source history/registry by whole-file replacement. The verified replay timestamp remains `2026-08-27T19:39:25Z` with five corrected fingerprints and five Aug. 26 predecessors preserved in the PR #107 discussion.
- `data/integration_queue.json` still identifies Aug. 27 as `needs-integration`; Aug. 28-Aug. 30 remain chronology-blocked. The queue did not yet contain the two Aug. 31 open research contributions at this reconciliation point, so this integrity branch records them as blocked contributed work rather than treating their claims as canonical.

## Current research / intelligence state

- Canonical source history is current through Aug. 26 only.
- The Careers in Your Community Challenge remains specialized school/team opportunity intelligence, not generic individual work.
- xTech|Search 10 remains non-actionable until authoritative RFI/application evidence resolves conflicting official date surfaces.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.
- Raw later research already preserved on `main` includes PR #82 (Aug. 28 morning/afternoon), PR #85 and PR #91 (Aug. 29 morning/afternoon), and PR #95 and PR #99 (Aug. 30 morning/afternoon).
- PR #103 contributes Aug. 31 morning research at `2026-08-31T07:38:39Z`; PR #106 contributes Aug. 31 afternoon research at `2026-08-31T19:41:50Z`. Both remain open and chronology-blocked behind Aug. 27-Aug. 30. Their arXiv/ETHOnline/opportunity claims remain contributed evidence until independently verified when chronology reaches them.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Current artifact inventory is valid but intentionally reports migration debt: 40 items, 10 duplicate groups, 11 orphaned items, 12 generated outputs, 7 items needing case links and one `PRIMARY EVIDENCE — DO NOT MOVE YET` item. Root legacy/generated artifacts must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- No new tool/toolset registration or bespoke website HTML was introduced by PR #107 or the two open Aug. 31 research PRs.
- Canonical discovery contracts remain unchanged: tools, toolsets, cases, intelligence, evidence, repository data and Agent Operations flow through canonical registries/manifests/site-data builders.
- Exact-main Core validation passed Agent Operations parsing, dynamic site-data generation, Command Site snapshot tests, repository-browser/toolset discovery and the generic user-visible tool visibility contract. The tool visibility regression confirms user-visible tools flow from canonical `data/tools.json` into Command Site/repository-browser/Pages/workspace data rather than requiring bespoke HTML.
- Direct GitHub Pages REST state was not exposed through the connector, but the exact-main `Deploy operations dashboard` workflow succeeded. Release-health claims are therefore based on that exact-commit deployment workflow rather than a separate browser/API assertion.

## Known state / debt

- Canonically replay the reconciled Aug. 27 snapshot in a separate bounded PR, advancing only the five matching registry timestamps after exact predecessor/hash verification.
- Process Aug. 28, Aug. 29, Aug. 30 and Aug. 31 research only after Aug. 27 becomes canonical, in timestamp/source-overlap order.
- PR #103 and PR #106 both predate current main. Preserve their separate one-file evidence, reconcile them against current main before integration, and do not infer source freshness merely because GitHub currently reports them mergeable.
- Daily maintenance continues to report known generated files at repository root. Artifact inventory reports no unknown-provenance items; relocation remains a hash/reference-preserving task, not deletion cleanup.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- CI dependencies remain bounded ranges (`pytest>=8,<10`, `numpy>=1.26,<3`, `Pillow>=10,<13`) rather than a full lockfile, and workflows use supported major action tags rather than immutable action SHAs. Current Actions logs also emit Node.js 20 deprecation warnings for `actions/checkout@v4`, `actions/setup-python@v5`, and `actions/upload-artifact@v4` being forced onto Node 24. Treat this as non-blocking supply-chain/runtime hardening debt.
- A bounded indexed-code search for `shell=True`, `os.system`, or `subprocess` returned no matches in this pass; this is not a complete security audit.
- `docs/AGENT_HANDOFF.md` remains append-only but its canonical tail is materially stale (latest stored entry is Aug. 26). The available repository mutation primitive replaces whole-file content rather than atomically appending; do not truncate historical handoffs. The exact current integrity handoff is preserved in this PR description for a safe append-capable pass.

## Current operating priorities

1. Replay `intelligence/feeds/2026-08-27-source-health-reconciled.json` with the canonical `source-history replay-snapshot` dry-run/write workflow in a separate bounded PR.
2. Require exactly five Aug. 27 history records with the reconciled hashes and verified Aug. 26 predecessor chain; advance only matching source-registry timestamps.
3. Rerun source-history/registry/report/intelligence/site-data/Agent Operations/Core/Maintenance validation before merge, then require independent integrity verification.
4. Only afterward process Aug. 28 morning/afternoon, Aug. 29 morning/afternoon, Aug. 30 morning/afternoon, then PR #103 Aug. 31 morning and PR #106 Aug. 31 afternoon research chronologically.
5. Keep PR #103's preprint claims and PR #106's ETHOnline actionability claims at contributed-research status until their primary-source evidence and participant-specific gates are independently verified at the correct chronology point.
6. Continue 310 external-provenance and hash-preserving artifact work without inflating experimental capability claims.

## Coordination note

PR #107 is merged and exact-merge Core/Pages workflow health is green. Its embedded `current main` statement naturally became stale at merge and it did not include PR #106, which opened shortly before the merge. This branch corrects only coordination truth and integration-inbox chronology; it preserves both open Aug. 31 research branches and all earlier source evidence. No later source freshness is manufactured and no compatible agent work is discarded.

## Next handoff

Build Integration should create the separate bounded Aug. 27 canonical replay PR from `intelligence/feeds/2026-08-27-source-health-reconciled.json`. Independently verify exactly five Aug. 26 predecessor/hash pairs, advance only matching source timestamps, and rerun source/history/report/intelligence/site-data/Agent Operations/Core/Maintenance before Repo Integrity reviews it. Do not replay Aug. 28-Aug. 31 research until the preceding chronology is canonical.