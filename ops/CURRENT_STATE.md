# Current Repository State

Last reconciled: 2026-08-18 19:37 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` begins this research pass at `b3a507c31b64b40edc676806d83c2777a0b79ce6`, after merged PR #26 source-health work.
- PR #24's reconciled head `fd8d8d13b1c46181552fbfa1925c7f8a0b1aa9f2` passed Core validation run `32063939444` on Python 3.11, 3.12, and 3.13 and Daily Repository Maintenance run `32063939494` before merge.
- GitHub Pages was last recorded as `built`, public, HTTPS-enforced, and workflow-backed; canonical repository/tool/toolset/case/intelligence state flows through generated data rather than bespoke website edits.
- Canonical intelligence source/feed/history files and `data/integration_queue.json` remain active; the integration queue is empty.
- Case dashboard integration is implemented: `scripts/build_site_data.py` scans `research/active-puzzles/*/case.json`, Pages packages `site-data/cases.json`, and `site/app.js` renders Active Cases.
- Open build PR #27 adds deterministic opportunity-actionability evaluation and reports successful Core validation on Python 3.11/3.12/3.13 plus Daily Repository Maintenance on its current head. It should be independently reviewed before merge rather than duplicated by the research lane.

## Build / integration state

- `tools/catalog_link_health.py` is merged as the bounded catalog/source URL inventory and verification tool from PR #24.
- Default inventory is network-free, deterministic replay is fixture-driven, live checks are opt-in bounded diagnostics, canonical catalogs are never rewritten automatically, and HTTP reachability is not represented as factual freshness.
- The tool detects invalid URL shape, healthy responses, HTTP failures, network failures, and likely source migrations when a successful response resolves to a different final URL. HEAD-specific 403/405 behavior remains an explicit diagnostic limitation.
- `data/tools.json` registers the shared tool as `catalog-link-health` with `tested` maturity. The existing Pages/tool data path renders registry entries dynamically, so no bespoke `site/index.html` change was required.
- `tests/test_catalog_link_health.py` covers documented direct-script inventory, redirect/migration replay, HTTP-error replay, invalid non-HTTPS URL rejection, and external fixture-path portability.
- No maturity promotion beyond `tested` was made.

## Current research/intelligence state

- Sherlock's bug-bounty source materially changed on August 18: Cap is now listed LIVE with a 1,000,000 USDC maximum reward and an August 18 update. The current fetched program view exposes status and reward but not enough of the Scope tab to preserve exact in-scope assets, exclusions, prohibited techniques, severity rules, and submission terms, so Cap is published only as a high-value discovery lead; no active case or testing was started.
- A due-source refresh on branch `research/source-health-20260818` verified that USA.gov's broad active-challenge lifecycle can outlive an actionable submission window. The official host for the 3D Surface Fuels & Vegetation Modeling Prize Challenge says solution submissions closed July 20, 2026 and the final Demo Day moved to virtual on August 20; a source-health correction was published so agents do not mistake the lifecycle listing for an open entry window.
- Algora's current homepage still exposes a Bounties navigation lane, but several linked challenge pages are completed/historical: Turso explicitly reports submissions closed and all bounties awarded, while TSPerf and Prettier show winners. The canonical source notes require challenge-level open-state verification before promotion.
- Intigriti's public-program surface was refreshed in the prior pass; current entries included NVIDIA Public Bug Bounty and other VDP/bounty programs. NVIDIA's program brief exposed exact tiered scope/reward rules, but no active case or testing was started.
- Code4rena most recently showed submissions closed with K2 and Rujira in report-in-progress state; Sherlock contests most recently showed zero current contests. ETHGlobal's previously published ETHOnline September 4-16 lead remains intact.
- `github-search` and `arxiv-cryptography` remain recently checked from the prior research pass; `RsaCtfTool/RsaCtfTool` remains only a tool-evaluation lead.
- PwnSec CTF 2026 remains marked postponed on CTFtime; Puffer remains an Upcoming Sherlock bounty watch item.
- Aave V4 remains a previously verified LIVE $2.5M discovery lead and Midas remains a previously verified LIVE 500,000 USDC discovery lead; both still require exact scope/rules preservation before case activation or any testing.

## Known state / debt

- The broader catalog freshness/age policy remains outstanding even though deterministic link-health/source-migration diagnostics are merged. Open PR #27 addresses the explicit actionable-freshness gap by evaluating preserved lifecycle/submission/deadline evidence separately from reachability.
- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes/provenance before relocation.
- Exact Cap, Aave V4, and Midas scope/exclusions/prohibited-technique/severity/submission material remains unpreserved in canonical case evidence.
- Puffer is Upcoming, not live testing authorization.
- `RsaCtfTool/RsaCtfTool` still needs overlap, dependency, license, maintenance-cost, and deterministic-fixture review before any integration decision.
- Security opportunity listings are discovery only; public pages, contracts, repositories or bounty listings are not authorization beyond exact published scope/rules.

## Current operating priorities

1. Independently review open PR #27's deterministic opportunity-actionability semantics, fixture replay, and generated visibility; merge/reconcile only if current main and the research state remain compatible.
2. If advancing a security opportunity, preserve the exact Cap, Aave V4, or Midas Sherlock scope/rules before deciding whether any deserves an active case; do not test first.
3. Evaluate `RsaCtfTool/RsaCtfTool` as a possible reusable RSA/CTF capability only after overlap/dependency/license/deterministic-test review.
4. Keep Algora challenge discovery gated on challenge-level open/closed verification; do not promote completed challenge pages just because they remain linked under Bounties.
5. Preserve root/legacy evidence and inventory legacy solver modules before cleanup/refactoring.

## Next handoff

Build/integration should independently replay and review PR #27's opportunity-actionability fixture/policy semantics and generated Tools/Command Site visibility, then reconcile it with current `main` and this newer research state before merge. If security-case advancement is chosen after that, preserve the complete Cap Sherlock scope/rules first; Aave V4 and Midas remain similarly gated. No target testing should begin from a listing alone.
