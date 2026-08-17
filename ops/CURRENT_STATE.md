# Current Repository State

Last reconciled: 2026-08-17 08:09 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Main currently includes merged research PR #23 at `d234397d20607a7b4f98cd8df184fcbe382e7d86`.
- Core validation run `32008197711` passed on Python 3.11, 3.12, and 3.13 for that main commit.
- Pages run `32008197700` passed for the same main commit; the operations dashboard remains workflow-backed.
- PR #22 registered the directly tested Command Site snapshot exporter in canonical `data/tools.json`.
- Canonical intelligence source/feed/history files and `data/integration_queue.json` are active; the integration queue is empty.
- The repository is connected to `kaibuzz0/Git-hub-command-site`; repository/tool/toolset state flows through generated snapshot/site-data paths rather than bespoke website edits.

## Build / integration state

- Branch `agent/build-link-health-20260817` adds `tools/catalog_link_health.py` as a bounded catalog/source URL inventory and verification tool.
- The tool defaults to deterministic network-free inventory, supports deterministic `replay` fixtures for CI, and offers opt-in bounded `check` mode for live HTTP/redirect diagnostics without mutating canonical source data.
- It detects invalid URL shape, healthy responses, HTTP failures, network failures, and likely source migrations when a successful response resolves to a different final URL.
- `data/tools.json` registers the shared tool as `catalog-link-health`; website/Command Site visibility should therefore flow through the existing tool registry and generated data path.
- `tests/test_catalog_link_health.py` covers direct-script inventory, redirect/migration replay, HTTP-error replay, and invalid non-HTTPS URL rejection.
- PR/CI verification for this branch is pending and must pass before the capability is called verified or merged.

## Current research/intelligence state

- The latest source-health pass reviewed CTFtime, HackerOne Directory, Code4rena contests, Sherlock contests, and Sherlock bug bounties and recorded real fingerprints in `data/source_check_history.json`.
- Aave V4 is published only as a high-value Sherlock bounty discovery lead; exact Scope-tab assets/exclusions/prohibited techniques/severity/reward/submission terms still need preservation before case activation or any testing.
- Midas remains a discovery lead with the same exact-scope preservation requirement.
- `github-search` and `arxiv-cryptography` remain never-checked; the arXiv fetch timed out and was not falsely marked fresh.

## Known state / debt

- Generated/legacy root artifacts remain a P1 cleanup item; preserve hashes/provenance before relocation.
- Legacy solver inventory/input-output/dependency documentation remains P2 work.
- Several merged topic branches remain on the remote; do not prune automatically without evidence/dependency review.
- Security opportunity listings are discovery only; public availability is not authorization beyond exact published scope/rules.

## Current operating priorities

1. Independently verify the new link-health/source-migration tool, including direct-script behavior, deterministic fixture replay, registry/site-data visibility, and bounded live semantics before calling it verified.
2. Preserve and verify exact Aave V4 and Midas Sherlock scope/rules before deciding whether either merits an active case; do not test first.
3. Complete real checks for `github-search` and `arxiv-cryptography` without fabricating freshness on fetch failures.
4. Preserve root/legacy evidence and inventory legacy solver modules before cleanup/refactoring.

## Next handoff

The integrity pass should independently verify `catalog-link-health`, confirm its registry entry appears through the generated dashboard/Command Site data path, and review live-mode redirect/error semantics before maturity is promoted beyond `tested`. Research/case agents should keep Aave V4 and Midas in discovery-only state until exact scope/rules are preserved.
