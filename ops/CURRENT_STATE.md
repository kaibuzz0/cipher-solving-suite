# Current Repository State

Last reconciled: 2026-08-16 19:17 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Latest `main` commit inspected: `dcfde9ae526997e0f730fdd2cceeffc7ce196a63` (`Merge pull request #5 ... VS Code dark theme`).
- Latest `Core validation` run for that commit completed successfully.
- Latest `Deploy operations dashboard` run for that commit completed successfully.
- No open pull requests were present at reconciliation time.
- No open GitHub issues were present at reconciliation time.
- Canonical tool registry exists at `data/tools.json` with shared user-visible tooling.
- Repository operating contract, maintenance policy, work queue, intelligence workflow, case workflow, and agent handoff are present.

## Known state / debt

- Generated/legacy root artifacts remain a documented P1 cleanup item; preserve hashes/provenance before relocation.
- Verified live opportunity/news adapters remain P1 work.
- Link-health/catalog freshness automation remains P2 work.
- Legacy solver inventory/input-output/dependency documentation remains P2 work.
- `data/integration_queue.json` and `docs/AUTOMATED_AGENT_OPERATIONS.md` are being established by the integrity bootstrap PR so outside AI contributions have a canonical integration path.
- The GitHub Pages UI was recently redesigned and the dark theme fix merged; future UI changes should preserve the working layout unless a specific defect is verified.

## Current operating priorities

1. Keep `main`, CI, Pages, registries, handoffs, and documentation aligned.
2. Preserve and inventory research artifacts before relocation.
3. Convert useful external changes into sourced intelligence/opportunities and structured cases.
4. Integrate new tools/solvers through `data/tools.json` and the integration queue rather than leaving orphan scripts.
5. Independently verify high-impact solve/live/payout/security claims before promoting them.

## Next handoff

The research/intelligence role should read this file and the latest handoff, then perform source-freshness/value discovery without duplicating existing catalog entries. The build/integration role should consume any actionable case or `needs-integration` queue item and keep tests, registries, and Pages synchronized.
