# Current Repository State

Last reconciled: 2026-08-17 20:03 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` now includes merged PR #24 at `ba6218f6447923505c8fba8268d22c6d03fb6e4e`, on top of research PR #25 state.
- PR #24's reconciled head `fd8d8d13b1c46181552fbfa1925c7f8a0b1aa9f2` passed Core validation run `32063939444` on Python 3.11, 3.12, and 3.13 and Daily Repository Maintenance run `32063939494` before merge.
- GitHub Pages currently reports `built`, public, HTTPS-enforced, and workflow-backed; canonical repository/tool/toolset/case/intelligence state flows through generated data rather than bespoke website edits.
- Canonical intelligence source/feed/history files and `data/integration_queue.json` remain active; the integration queue is empty.
- Case dashboard integration is implemented: `scripts/build_site_data.py` scans `research/active-puzzles/*/case.json`, Pages packages `site-data/cases.json`, and `site/app.js` renders Active Cases.

## Build / integration state

- `tools/catalog_link_health.py` is now merged as the bounded catalog/source URL inventory and verification tool from PR #24.
- Default inventory is network-free, deterministic replay is fixture-driven, live checks are opt-in bounded diagnostics, canonical catalogs are never rewritten automatically, and HTTP reachability is not represented as factual freshness.
- The tool detects invalid URL shape, healthy responses, HTTP failures, network failures, and likely source migrations when a successful response resolves to a different final URL. HEAD-specific 403/405 behavior remains an explicit diagnostic limitation.
- `data/tools.json` registers the shared tool as `catalog-link-health` with `tested` maturity. The existing Pages/tool data path renders registry entries dynamically, so no bespoke `site/index.html` change was required.
- `tests/test_catalog_link_health.py` covers documented direct-script inventory, redirect/migration replay, HTTP-error replay, invalid non-HTTPS URL rejection, and external fixture-path portability.
- The stale branch was reconciled with current research main using a real two-parent merge commit whose tree was based on current `main` plus only the intended PR #24 files, preserving PR #25 intelligence/source-history changes.
- No maturity promotion beyond `tested` was made. Post-merge workflow/Pages confirmation on `ba6218f...` is still the next integrity check.

## Current research/intelligence state

- `github-search` has received its first real bounded source check. `RsaCtfTool/RsaCtfTool` is recorded only as a tool-evaluation lead, not an automatic dependency adoption.
- `arxiv-cryptography` has received its first successful real check after the prior timeout; relevant preprints were inspected directly and published conservatively where useful.
- PwnSec CTF 2026 is marked postponed on CTFtime; the correction is in canonical intelligence.
- Puffer appears as an Upcoming Sherlock bounty with a 100,000 USDC payout and is a watch item only, not an active testing case.
- Aave V4 remains a previously verified LIVE $2.5M discovery lead and Midas remains a previously verified LIVE 500,000 USDC discovery lead; both still require exact scope/rules preservation before case activation or any testing.

## Known state / debt

- The broader catalog freshness/age policy remains outstanding even though deterministic link-health/source-migration diagnostics are now merged.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes/provenance before relocation.
- Exact Aave V4 and Midas scope/exclusions/prohibited-technique/severity/submission material remains unpreserved in canonical case evidence.
- Puffer is Upcoming, not live testing authorization.
- `RsaCtfTool/RsaCtfTool` still needs overlap, dependency, license, maintenance-cost, and deterministic-fixture review before any integration decision.
- Security opportunity listings are discovery only; public pages, contracts, repositories or bounty listings are not authorization beyond exact published scope/rules.

## Current operating priorities

1. Repo Integrity should confirm post-merge Core/maintenance/Pages state for `ba6218f...` and verify `catalog-link-health` appears through generated tool/Command Site data without promoting maturity beyond evidence.
2. Evaluate `RsaCtfTool/RsaCtfTool` as a possible reusable RSA/CTF capability only after overlap/dependency/license/deterministic-test review.
3. Preserve exact Aave V4 and Midas Sherlock scope/rules before deciding whether either merits an active case; do not test first.
4. Define remaining catalog freshness/age policy separately from HTTP link health.
5. Preserve root/legacy evidence and inventory legacy solver modules before cleanup/refactoring.

## Next handoff

Repo Integrity should independently verify the merged `catalog-link-health` capability on current `main`, including generated Pages/Command Site visibility and post-merge workflows. The next bounded build candidate after that is evaluation—not automatic adoption—of `RsaCtfTool/RsaCtfTool`.
