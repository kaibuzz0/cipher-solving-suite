# Automated Agent Operations

This document defines the recurring maintenance contract for AI agents operating on `kaibuzz0/cipher-solving-suite`. It complements `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, `docs/REPO_MAINTENANCE.md`, `docs/INTELLIGENCE_WORKFLOW.md`, `docs/CASE_WORKFLOW.md`, `docs/WORK_QUEUE.md`, and `docs/AGENT_HANDOFF.md`.

The recurring system is intentionally condensed into three coordinated roles. Agents must read current repository state and the latest handoff before changing anything.

## Shared rules

All recurring agents must:

1. Read `README.md`, `AGENTS.md`, `docs/AI_AGENT_INTEGRATION.md`, `ops/CURRENT_STATE.md`, `docs/WORK_QUEUE.md`, and the latest `docs/AGENT_HANDOFF.md` entry before acting.
2. Inspect recent commits, open PRs/issues, integration queue, and CI before claiming work.
3. Prefer canonical registries and existing lanes over one-off files or duplicate systems.
4. Preserve provenance, hashes, timestamps, source URLs, scope, uncertainty, and reproducibility where relevant.
5. Never commit secrets, credentials, wallet material, private keys, or personal data.
6. Never treat public availability, intelligence, a hostname, repository, contract, or bounty listing as authorization to test it.
7. Make bounded, reviewable, reversible changes; substantive changes belong on a branch/PR.
8. Run the smallest relevant deterministic verification and record exactly what ran.
9. Keep repository state, registries, README navigation, dynamic site-data builders, Agent Operations data, and GitHub Pages output aligned.
10. Update the handoff and `ops/CURRENT_STATE.md` when material state changes.
11. Treat other AI output as contributed work, not automatically trusted truth. Reconcile it through current `main`, canonical registries, `data/integration_queue.json`, tests, CI, and independent verification where appropriate.
12. Expect concurrent agents. Before resolving conflicts, identify which side contains newer verified state and preserve both non-conflicting changes rather than blindly choosing one branch.

## Role A — Repo Integrity / Verification / Coordination

Purpose: keep the repository truthful, reproducible, secure, and easy for the next agent to understand.

Responsibilities:

- reconcile documented state with the default branch;
- inspect CI, Pages deployment, tests, compileability, direct-script commands, generated site data, Agent Operations data, and dynamic website discovery;
- check for stale or contradictory docs, broken navigation, duplicate work, stale PRs/branches, unregistered tools/toolsets, orphaned artifacts, suspicious secret-like files, unsafe shell/path handling, and supply-chain drift;
- verify that newly added tools/toolsets/cases/intelligence/evidence appear through canonical website data paths rather than one-off hardcoded HTML;
- verify that `docs/AI_AGENT_INTEGRATION.md`, `AGENTS.md`, and this recurring contract remain mutually consistent;
- independently verify important claims when practical;
- ensure capability labels (`implemented`, `tested`, `live`, `experimental`, `simulated`, `deprecated`) are evidence-backed;
- preserve evidence and never silently delete primary research artifacts;
- maintain `ops/CURRENT_STATE.md` as the concise repository truth snapshot;
- inspect external-agent/integration-queue contributions and flag incomplete or conflicting integration before they can silently drift into canonical state.

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
- keep source health and GitHub Pages data synchronized;
- preserve enough provenance that another AI with no conversation history can re-open the source and independently understand the finding;
- route research produced by another AI through canonical source/feed/case structures instead of copying unverified narrative into repository truth.

Expected output: value-ranked intelligence/opportunity changes plus a precise handoff for the build agent.

## Role C — Build / Tool Integration / Case Advancement

Purpose: increase useful repository capability while keeping every new capability integrated into the shared system.

Responsibilities:

- advance the highest-value bounded active case or integration item;
- integrate contributed AI tools, toolsets, and solvers into canonical repository lanes;
- detect unregistered tools/scripts/toolsets and either register them or document why they should remain internal/legacy;
- enforce `docs/AI_AGENT_INTEGRATION.md` for contributions originating from other AI sessions/models;
- add deterministic fixtures/tests or reproducible verification when behavior changes;
- reconcile toolset manifests/catalog entries, `data/tools.json`, related cases/evidence, integration queue, README navigation, and GitHub Pages discovery;
- prefer data-driven website discovery. Normal additions must flow through manifests/registries/site-data builders rather than bespoke edits to `site/index.html`;
- validate the repository browser, Toolsets/Tools detail views, relationship drill-downs, and Agent Operations console when relevant generated data changes;
- keep cases, evidence, tool registry, toolset catalog, integration queue, current state, handoff, and GitHub Pages synchronized;
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
- parent toolset linkage where applicable;
- GitHub Pages visibility when it should be discoverable by users;
- handoff entry.

### Toolset integration contract

A reusable toolset should live under `toolsets/<toolset-id>/`, include a readable `toolset.json` manifest and documentation, and be reconciled with `toolsets/catalog.json` when it is intended to be part of the reusable library. Referenced entrypoints/files must exist, shared tools should be registered in `data/tools.json`, and the static site should discover the toolset automatically from canonical state.

If a normal toolset requires manual HTML to become visible, treat that as a site-data/discovery defect rather than normal integration work.

## Integration queue

`data/integration_queue.json` is the machine-readable inbox for tools, toolsets, solvers, cases, research items, or other contributed work that requires review/integration.

Allowed states:

- `needs-review`
- `needs-integration`
- `blocked`
- `integrated`
- `rejected`

Agents should preserve prior queue entries and update state rather than silently replacing history. Queue entries should include enough evidence for a different agent to continue without reconstructing the originating conversation.

External or newly introduced AI agents should use this inbox whenever they cannot complete the full canonical integration contract themselves.

## Website and Agent Operations contract

The GitHub Pages workspace is a static visual interface over repository state, not a separate source of truth.

Normal flow:

`canonical repo files -> site-data builders -> Pages artifact -> browser refresh`

The site is expected to surface new repository data without repetitive hand-edits to HTML. Current user-facing capabilities include tool/toolset discovery, repository file previews, cases, intelligence, opportunities, evidence, source health, relationship drill-downs, prompts, and the Agent Operations console.

Recurring agents must treat a Pages build as incomplete if canonical data changed but generated data, packaging, or deployed UI no longer reflects it.

The Agent Operations console is generated from `docs/WORK_QUEUE.md`, `docs/AGENT_HANDOFF.md`, `ops/CURRENT_STATE.md`, and `data/integration_queue.json`. These remain the canonical coordination files; do not create a competing operations database just for the website.

## Collision prevention

Before editing a path, check open PRs, the work queue, integration queue, latest handoff, and recent commits. If another agent owns the same objective, do not overwrite it. Either work on a non-conflicting dependency or leave a blocker/handoff.

When a branch becomes stale because another agent merged shared-state changes, reconcile current `main`, preserve both sides where compatible, re-run verification on the reconciled head, and document the conflict resolution.

## Definition of a healthy recurring cycle

A cycle is healthy when:

- `main` reflects verified repository truth;
- CI and Pages state are known;
- actionable external findings are sourced and deduplicated;
- newly built tools/toolsets/capabilities are registered and discoverable;
- contributions from newly introduced AI agents are integrated through the same contracts rather than special-cased;
- important claims have independent verification or are explicitly marked pending;
- evidence is preserved;
- dynamic website views reflect canonical repo state;
- the work queue, integration inbox, current state, Agent Operations console, and latest handoff agree on what should happen next.
