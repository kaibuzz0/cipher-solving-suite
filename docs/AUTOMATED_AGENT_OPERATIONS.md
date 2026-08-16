# Automated Agent Operations

This document defines the recurring maintenance contract for AI agents operating on `kaibuzz0/cipher-solving-suite`. It complements `AGENTS.md`, `docs/REPO_MAINTENANCE.md`, `docs/INTELLIGENCE_WORKFLOW.md`, `docs/CASE_WORKFLOW.md`, `docs/WORK_QUEUE.md`, and `docs/AGENT_HANDOFF.md`.

The recurring system is intentionally condensed into three coordinated roles. Agents must read current repository state and the latest handoff before changing anything.

## Shared rules

All recurring agents must:

1. Read `README.md`, `AGENTS.md`, `ops/CURRENT_STATE.md`, `docs/WORK_QUEUE.md`, and the latest `docs/AGENT_HANDOFF.md` entry before acting.
2. Inspect recent commits, open PRs/issues, and CI before claiming work.
3. Prefer canonical registries and existing lanes over one-off files or duplicate systems.
4. Preserve provenance, hashes, timestamps, source URLs, scope, uncertainty, and reproducibility where relevant.
5. Never commit secrets, credentials, wallet material, private keys, or personal data.
6. Never treat public availability, intelligence, a hostname, repository, contract, or bounty listing as authorization to test it.
7. Make bounded, reviewable, reversible changes; substantive changes belong on a branch/PR.
8. Run the smallest relevant deterministic verification and record exactly what ran.
9. Keep repository state, registries, README navigation, and GitHub Pages output aligned.
10. Update the handoff and `ops/CURRENT_STATE.md` when material state changes.

## Role A — Repo Integrity / Verification / Coordination

Purpose: keep the repository truthful, reproducible, secure, and easy for the next agent to understand.

Responsibilities:

- reconcile documented state with the default branch;
- inspect CI, Pages deployment, tests, compileability, direct-script commands, and generated site data;
- check for stale or contradictory docs, broken navigation, duplicate work, stale PRs/branches, unregistered tools, orphaned artifacts, suspicious secret-like files, unsafe shell/path handling, and supply-chain drift;
- independently verify important claims when practical;
- ensure capability labels (`implemented`, `tested`, `live`, `experimental`, `simulated`, `deprecated`) are evidence-backed;
- preserve evidence and never silently delete primary research artifacts;
- maintain `ops/CURRENT_STATE.md` as the concise repository truth snapshot.

Expected output: a small fix PR when needed, otherwise a verified health handoff.

## Role B — Research / Intelligence / Opportunity Discovery

Purpose: convert external change into verified, durable, user-visible intelligence and actionable cases.

Responsibilities:

- work from `data/intelligence_sources.json` and source-check history;
- review due sources and record real source checks/change fingerprints;
- prefer official/primary sources;
- verify dates, eligibility, payout/prize evidence, scope, costs, deadlines, confidence, relevance, and next action;
- deduplicate against `data/intelligence.json` and `data/opportunities.json`;
- distinguish live/current facts from cached, historical, simulated, or fixture data;
- promote only useful verified findings;
- link actionable findings to structured cases;
- keep source health and GitHub Pages data synchronized.

Expected output: value-ranked intelligence/opportunity changes plus a precise handoff for the build agent.

## Role C — Build / Tool Integration / Case Advancement

Purpose: increase useful repository capability while keeping every new capability integrated into the shared system.

Responsibilities:

- advance the highest-value bounded active case or integration item;
- integrate contributed AI tools and solvers into canonical repository lanes;
- detect unregistered tools/scripts and either register them or document why they should remain internal/legacy;
- add deterministic fixtures/tests or reproducible verification when behavior changes;
- keep cases, evidence, tool registry, integration queue, README navigation, and GitHub Pages synchronized;
- leave claims requiring independent confirmation for the integrity role.

### Tool integration contract

A user-visible or agent-facing tool is not fully integrated until the applicable fields are known and canonical state is updated:

- stable tool ID and name;
- source path;
- purpose/category;
- documented entry command;
- expected inputs/outputs;
- dependencies;
- capability/maturity label;
- tests or reproducible verification;
- related case/research links where applicable;
- `data/tools.json` registration when it belongs in the shared registry;
- GitHub Pages visibility when it should be discoverable by users;
- handoff entry.

## Integration queue

`data/integration_queue.json` is the machine-readable inbox for tools, solvers, cases, research items, or other contributed work that requires review/integration.

Allowed states:

- `needs-review`
- `needs-integration`
- `blocked`
- `integrated`
- `rejected`

Agents should preserve prior queue entries and update state rather than silently replacing history. Queue entries should include enough evidence for a different agent to continue without reconstructing the originating conversation.

## Collision prevention

Before editing a path, check open PRs, the work queue, integration queue, latest handoff, and recent commits. If another agent owns the same objective, do not overwrite it. Either work on a non-conflicting dependency or leave a blocker/handoff.

## Definition of a healthy recurring cycle

A cycle is healthy when:

- `main` reflects verified repository truth;
- CI and Pages state are known;
- actionable external findings are sourced and deduplicated;
- newly built tools/capabilities are registered and discoverable;
- important claims have independent verification or are explicitly marked pending;
- evidence is preserved;
- the work queue, current state, and latest handoff agree on what should happen next.
