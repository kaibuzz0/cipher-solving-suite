# AI Agent Operating Contract

This repository may be worked on by multiple AI agents. Every agent must leave the repository easier for the next agent to understand.

## Mission

Improve the cipher-solving suite as a reproducible, authorized puzzle/CTF/bug-bounty research platform. Do not claim live capability, verified payouts, production readiness, or solved results unless evidence exists in the repository.

## Safety and authorization boundary

- Work only on puzzles, CTFs, systems, programs, contracts, or targets that are explicitly authorized for testing.
- Record program scope and rules before performing security testing.
- Do not automate credential attacks, destructive actions, persistence, evasion, or testing outside stated scope.
- Prefer local fixtures, CTF targets, challenge data, and documented bug-bounty assets.
- Stop and flag ambiguous scope rather than guessing.

## Before making changes

1. Read `README.md` first. Treat its **Quick navigation**, **Agent start sequence**, and **Where new things belong** sections as the repository map.
2. Read `docs/REPO_MAINTENANCE.md`.
3. Read the latest entry in `docs/AGENT_HANDOFF.md`.
4. Check `docs/WORK_QUEUE.md` plus open issues and pull requests.
5. Identify the smallest verifiable unit of work and avoid duplicating an active task.

## Working rules

- One focused branch/PR per coherent change.
- Keep `README.md` navigation accurate when adding, moving, or removing major tools, workflows, catalogs, or operating documents.
- Do not silently rewrite research evidence or generated artifacts.
- Generated outputs belong under `workspace/`, `artifacts/`, or an existing output directory, not the repository root.
- New Python functionality should have deterministic tests when practical.
- External/network functionality must distinguish live data from fixtures or simulations.
- Never hard-code secrets, tokens, private keys, wallet seeds, or credentials.
- Preserve evidence: inputs, source URLs, timestamps, hashes, assumptions, and solver parameters when relevant.
- Prefer extending canonical catalogs/workflows over creating duplicate lists or one-off files.

## Verification standard

A task is not complete because code was written. The agent must record what was checked and the result. Prefer, in order:

1. automated tests,
2. deterministic fixture replay,
3. static validation / compile checks,
4. manual reproducible steps.

If verification cannot be run, state exactly why.

## Handoff requirement

Before ending work, append a short entry to `docs/AGENT_HANDOFF.md` containing:

- date/time in UTC,
- agent/task name,
- branch or PR,
- what changed,
- verification performed,
- evidence/artifacts,
- known risks or failures,
- exact next recommended action.

If a task changes a major repo entry point, tool, workflow, catalog, dashboard section, or directory lane, confirm that `README.md` still links to it correctly.

Do not delete prior handoff entries.
