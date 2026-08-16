# Repo Factory Toolset

Reusable bootstrap kit for new AI-assisted GitHub repositories. This is one toolset inside the shared `toolsets/` library, not a root-level project architecture.

## Purpose

Install a compact operating foundation into a new repository so humans and AI agents can immediately understand project intent, current state, research, work ownership, handoffs, integration requirements, and exact CI failures.

## Export

```bash
python toolsets/repo-factory/export_toolset.py /path/to/new-repo --project-name "My Project"
```

Preview only:

```bash
python toolsets/repo-factory/export_toolset.py /path/to/new-repo --project-name "My Project" --dry-run
```

Existing files are not overwritten unless `--force` is supplied.

## Installed surfaces

- `AGENTS.md`
- `ops/CURRENT_STATE.md`
- `docs/PROJECT_BLUEPRINT.md`
- `docs/RESEARCH_LOG.md`
- `docs/WORK_QUEUE.md`
- `docs/AGENT_HANDOFF.md`
- `docs/BUILD_CHECKLIST.md`
- `data/integration_queue.json`
- `.github/workflows/diagnostic-ci.yml`

## Design rules

CI must explain exactly what failed. Research must preserve evidence. Agents must leave handoffs. New tools/features must enter through a visible integration contract. Blueprints and checklists should expose hidden assumptions before large implementation passes.

Customize the generated files immediately for the new project's language, dependencies, architecture, and validation commands.
