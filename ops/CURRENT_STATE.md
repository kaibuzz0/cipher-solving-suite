# Current Repository State

Last reconciled: 2026-08-16 20:00 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Latest `main` commit inspected: `03416162ff0a47f73b575df70b78465beda5be79` (Repo Factory/toolsets merge).
- The recurring-agent contract and integration queue are now present on `main`.
- Canonical tool registry exists at `data/tools.json`; this build pass adds the Repo Factory exporter entry on a scoped branch.
- GitHub Pages dark workspace remains intentionally unchanged by this pass.
- Research/intelligence work is active independently in PR #8; this build pass does not modify or duplicate those source/intelligence changes.

## Active build/integration work

- Branch `agent/build-repo-factory-toolset` converts the temporary root-level `repo-kit/` experiment into the first real member of the reusable `toolsets/` library: `toolsets/repo-factory/`.
- The toolset now has machine-readable `toolset.json`, an export script, project/agent/research/checklist templates, a reusable diagnostic-CI workflow, a `toolsets/catalog.json` registry, and deterministic exporter tests.
- `data/tools.json` registers the Repo Factory exporter so the existing website data pipeline can expose it without changing the working VS Code-style site layout.

## Known state / debt

- Generated/legacy root artifacts remain a documented P1 cleanup item; preserve hashes/provenance before relocation.
- Verified live opportunity/news adapters and source freshness work are being handled in the research lane/PR #8.
- Link-health/catalog freshness automation remains P2 work.
- Legacy solver inventory/input-output/dependency documentation remains P2 work.
- Additional reusable toolsets remain planned: CI diagnostics, research ops, agent coordination, evidence integrity, website workspace, security/quality, and release ops.

## Current operating priorities

1. Validate and merge the Repo Factory toolset without touching the accepted website layout.
2. Keep `main`, CI, Pages, registries, handoffs, and documentation aligned.
3. Preserve and inventory research artifacts before relocation.
4. Integrate future reusable capabilities as independent `toolsets/<id>/` packages with `toolset.json`, tests, and explicit dependencies.
5. Independently verify high-impact solve/live/payout/security claims before promoting them.

## Next handoff

The integrity pass should independently verify the Repo Factory exporter tests, toolset catalog/metadata, canonical tool registration, and removal of the duplicate `repo-kit/` path. The research pass can continue PR #8 independently because this branch does not change intelligence/opportunity data.
