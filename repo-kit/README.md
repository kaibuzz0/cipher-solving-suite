# AI Repository Starter Kit

Portable project-operating templates for new GitHub repositories.

The goal is to make a new repo immediately understandable to both humans and AI agents: what is being built, what has been tried, what must be verified, what failed, what is next, and exactly which CI test broke.

## Export

From `cipher-solving-suite`:

```bash
python repo-kit/export_starter_kit.py /path/to/new-repo --project-name "My Project"
```

Preview without writing:

```bash
python repo-kit/export_starter_kit.py /path/to/new-repo --project-name "My Project" --dry-run
```

Existing files are never overwritten unless `--force` is explicitly supplied.

## What gets installed

- `AGENTS.md` — operating contract for AI/human contributors.
- `ops/CURRENT_STATE.md` — compact source of truth for the current project state.
- `docs/PROJECT_BLUEPRINT.md` — architecture, goals, interfaces, risks, and acceptance gates.
- `docs/RESEARCH_LOG.md` — evidence-backed research ledger.
- `docs/WORK_QUEUE.md` — prioritized work with acceptance criteria.
- `docs/AGENT_HANDOFF.md` — persistent cross-agent memory.
- `docs/BUILD_CHECKLIST.md` — build/release/integration checklist.
- `data/integration_queue.json` — machine-readable inbox for tools/features produced by other agents.
- `.github/workflows/diagnostic-ci.yml` — reusable diagnostic CI that names matrix jobs, prints individual tests, writes JUnit XML, uploads diagnostics even on failure, and emits a GitHub step summary.

## Design principles

1. **CI explains failure.** Never stop at `exit code 1`; expose the failing test/check and preserve diagnostics.
2. **Blueprint before sprawl.** Define architecture, interfaces, constraints, and acceptance criteria before large implementation passes.
3. **Research is evidence, not memory.** Preserve source, date, claim, result, confidence, and next action.
4. **Every agent leaves a handoff.** The next agent should not reconstruct context from commit history alone.
5. **New tools integrate through a contract.** A tool is not integrated until location, command, inputs/outputs, tests, dependencies, registry/inbox state, docs, and ownership are known.
6. **Checklists are executable memory.** Use them to make hidden requirements visible.
7. **Claims have labels.** Distinguish implemented, tested, live, experimental, simulated, and deprecated.
8. **Small coherent PRs beat giant mixed passes.**

## Recommended new-repo flow

```text
PROJECT IDEA
   ↓
PROJECT_BLUEPRINT.md
   ↓
WORK_QUEUE.md
   ↓
AGENTS.md operating rules
   ↓
BUILD / RESEARCH
   ↓
DIAGNOSTIC CI
   ↓
HANDOFF
   ↓
CURRENT_STATE
   ↓
NEXT AGENT / NEXT PASS
```

The starter kit is intentionally generic. A new repository should customize the blueprint, dependency/install steps in CI, and project-specific verification commands immediately after export.
