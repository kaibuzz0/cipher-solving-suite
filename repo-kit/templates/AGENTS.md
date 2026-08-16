# AI Agent Operating Contract — {{PROJECT_NAME}}

This repository may be maintained by multiple humans and AI agents. Every pass must be auditable, bounded, reversible, and easy to hand off.

## Start every pass here

Read, in order:

1. `README.md`
2. `ops/CURRENT_STATE.md`
3. `docs/PROJECT_BLUEPRINT.md`
4. `docs/WORK_QUEUE.md`
5. latest entries in `docs/AGENT_HANDOFF.md`
6. recent commits, open PRs/issues, and current CI state

Do not begin implementation until you know what another agent is already doing.

## Operating rules

- Work on one bounded objective at a time.
- Prefer the smallest coherent PR that advances an acceptance criterion.
- Never convert an assumption into a verified claim.
- Use capability labels consistently: `implemented`, `tested`, `live`, `experimental`, `simulated`, `deprecated`.
- Preserve research sources, timestamps, hashes, parameters, fixtures, and provenance when relevant.
- Do not commit credentials, secrets, private keys, tokens, personal data, or generated junk.
- Add or update deterministic tests when behavior changes.
- Any documented direct command must be tested in that exact invocation form.
- Do not weaken verification merely to get green CI.
- Do not silently overwrite another agent's active work.
- Update the canonical structure instead of creating duplicate lists, registries, or workflows.

## Standard pass

### 1. Orient
Confirm current state, active work, relevant blueprint section, and exact acceptance criterion.

### 2. Verify baseline
Run the smallest relevant test/smoke/static check before modifying code. Record pre-existing failures.

### 3. Execute
Make one bounded change with explicit inputs, outputs, assumptions, and dependencies.

### 4. Validate
Prefer automated tests, deterministic fixtures, static/compile checks, then reproducible manual verification.

### 5. Integrate
If adding a tool, component, service, or workflow, register it through `data/integration_queue.json` until all integration requirements are satisfied: location, entry command/API, inputs, outputs, dependencies, tests, docs, owner, maturity, and related project work.

### 6. Handoff
Append to `docs/AGENT_HANDOFF.md` with date/time, objective, branch/PR, files changed, exact verification, failures/risks, artifacts/evidence, and the next action.

Update `ops/CURRENT_STATE.md` whenever repository truth materially changes.

## Definition of done

A change is done only when:

- acceptance criteria are satisfied or explicitly blocked,
- relevant verification results are recorded,
- docs do not knowingly contradict behavior,
- no secrets or unexplained generated artifacts were added,
- integration metadata is complete when applicable,
- handoff and next action are explicit.
