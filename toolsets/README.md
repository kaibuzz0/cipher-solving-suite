# Reusable Toolsets Library

This directory is a library of independent, exportable toolsets for GitHub projects and AI-assisted development.

Each toolset should be self-contained and include:

- a clear purpose and scope,
- installation/export instructions,
- templates or scripts,
- tests or validation where practical,
- integration notes,
- version/maturity information,
- machine-readable metadata in `toolset.json`.

## Planned toolset families

- `repo-factory/` — bootstrap a new AI-friendly repository with blueprints, handoffs, checklists, research logs, integration queues, and diagnostic CI.
- `ci-diagnostics/` — reusable GitHub Actions patterns that expose exact failing tests/checks and retain artifacts.
- `research-ops/` — source tracking, research ledgers, freshness, provenance, and review checklists.
- `agent-coordination/` — current state, work queue, handoffs, collision avoidance, and contribution protocols.
- `evidence-integrity/` — hashing, provenance, artifact inventories, duplicate detection, and migration safety.
- `website-workspace/` — reusable GitHub Pages workspace/dashboard scaffolding.
- `security-quality/` — secret checks, dependency/supply-chain review, static checks, and capability-label verification.
- `release-ops/` — release checklists, changelog/version gates, packaging, rollback, and deployment verification.

Toolsets may depend on one another, but dependencies must be explicit. Do not duplicate the same template or workflow across multiple toolsets unless one is intentionally a vendored snapshot.
