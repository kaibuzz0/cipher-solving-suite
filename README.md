# Cipher Solving Suite v3.1.0

A multi-agent research and operations hub for cipher puzzles, CTFs, hackathons, authorized bug-bounty/audit work, coding challenges, GitHub research, reusable prompts, notes, and earnings tracking.

This repository is being converted from a loose collection of scripts and generated artifacts into a maintainable system where human and AI agents can share one work queue, one opportunity catalog, reproducible research, and explicit handoffs.

## What works now

- `suite.py` — honest top-level status and command router.
- `data/opportunities.json` — shared opportunity/link catalog used by both CLI and website.
- `data/prompts.json` — reusable AI prompt library.
- `tools/opportunity_finder.py` — list/search/filter/open catalog entries.
- `tools/earnings_tracker.py` — record attempts and verified earnings.
- `tools/scanning/opportunity_scanner.py` — timestamped catalog snapshots. It is deliberately labeled **not a live scrape**.
- `AGENTS.md` — operating contract for AI and human agents.
- `docs/AGENT_HANDOFF.md` — append-only agent handoff journal.
- `docs/WORK_QUEUE.md` — shared claimable work queue.
- `docs/REPO_MAINTENANCE.md` — maintenance rules and repository lanes.
- `scripts/maintenance_check.py` — deterministic hygiene/compile checks.
- `tests/test_core.py` — deterministic tests for catalog and earnings behavior.
- `site/` — static Operations Hub dashboard deployed through GitHub Pages after merge/configuration.

## Quick start

```bash
git clone https://github.com/kaibuzz0/cipher-solving-suite.git
cd cipher-solving-suite

python suite.py --status
python suite.py --opportunities
python tools/opportunity_finder.py --search crypto
python tools/opportunity_finder.py --category hackathon
python tools/earnings_tracker.py stats
python suite.py --scan
python suite.py --maintenance
python -m unittest discover -s tests -v
```

## Repository map

```text
cipher-solving-suite/
├── AGENTS.md                    # rules every agent reads first
├── README.md
├── suite.py                     # top-level command router
├── data/
│   ├── opportunities.json       # canonical opportunity/link catalog
│   └── prompts.json             # reusable AI prompts
├── docs/
│   ├── AGENT_HANDOFF.md         # append-only notes between agents
│   ├── REPO_MAINTENANCE.md      # maintenance/definition-of-done rules
│   └── WORK_QUEUE.md            # shared work claims and priorities
├── site/
│   ├── index.html               # GitHub Pages Operations Hub
│   ├── app.js
│   └── styles.css
├── tools/
│   ├── opportunity_finder.py
│   ├── earnings_tracker.py
│   └── scanning/opportunity_scanner.py
├── scripts/
│   └── maintenance_check.py
├── tests/
│   └── test_core.py
├── research/                    # active cases, research and solutions
├── intelligence/               # timestamped feeds/snapshots
├── solvers/                     # solving modules
├── workspace/                   # active/generated work
└── legacy/                      # older consolidated material
```

## AI-agent workflow

Every agent should:

1. Read `AGENTS.md`.
2. Read the latest `docs/AGENT_HANDOFF.md` entry.
3. Check `docs/WORK_QUEUE.md` and open PRs/issues.
4. Claim the smallest useful task.
5. Preserve sources, timestamps, hashes, assumptions, commands, and evidence.
6. Verify changes with tests or reproducible checks.
7. Append a handoff entry before stopping.

Agents should not silently overwrite prior research, fabricate live status, or create duplicated catalogs. New opportunity links belong in `data/opportunities.json`; new reusable prompts belong in `data/prompts.json`.

## Opportunity pipeline

The catalog is a launchpad, not a promise of payout. It currently includes categories such as:

- bug bounty programs,
- Web3 audit contests,
- CTF competitions,
- cryptography/security training,
- hackathons,
- government prize challenges,
- GitHub research.

Use:

```bash
python tools/opportunity_finder.py --list
python tools/opportunity_finder.py --search solidity
python tools/opportunity_finder.py --category ctf
python tools/opportunity_finder.py --open ctftime
```

Availability, prizes, eligibility, rules, and scopes change. Verify those facts on the official linked page before investing time or testing a target.

## Security authorization boundary

Security tooling is for authorized CTFs, labs, audits, puzzles, and bug-bounty programs. Before testing a real target, save the official rules/scope and confirm the asset/action is allowed. Do not treat a public hostname, contract, repository, or IP address as authorization by itself.

## Static Operations Hub

`site/` is a dependency-free dashboard with tabs for:

- opportunities,
- tools and commands,
- reusable AI prompts,
- agent workflow/handoffs,
- research launch links.

`.github/workflows/pages.yml` assembles the site with the same JSON catalogs and publishes it through GitHub Pages on `main` changes. The Pages repository setting may need to be set to **GitHub Actions** once; after that deployments are automated.

## Validation and maintenance

Pull requests run Python 3.11, 3.12, and 3.13 unit tests plus compile and maintenance checks through `.github/workflows/ci.yml`.

A daily hygiene workflow checks for missing required files, Python compile failures, version drift, generated files sitting at repository root, and suspicious secret-like filenames. Warnings are evidence for cleanup work; they are not automatically deleted.

## Known cleanup debt

The repository still contains older generated images/binaries and legacy research at the root. Those files are intentionally not mass-moved in the first maintenance pass because provenance could be lost. The next cleanup pass should inventory hashes and references, then relocate them safely into evidence/artifact directories.

Older research documents can also contain stale payout/platform claims. Treat them as historical notes until their sources are revalidated and migrated into the shared catalog.

## Goal

The goal is not to promise money or pretend every tool is live. The goal is to make this repository a dependable command center that helps agents rapidly answer:

- What legitimate opportunity should we investigate next?
- What tools do we already have?
- What has already been tried?
- What evidence and authorization do we have?
- What did the previous agent learn?
- What is the next highest-value piece of work?

License: MIT
