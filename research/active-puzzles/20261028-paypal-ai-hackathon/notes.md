# Research notes — PayPal AI Hackathon

Verified from official competition rules and organizer update on 2026-10-28 UTC.

Cash math: grand $12k+$8k+$5k=$25k; five $5k honorable mentions=$25k; AG Grid $5k+$2k+3×$1k=$10k; APIMatic 3×$1k=$3k; Bryntum 3×$1k=$3k; Channel3 $1.5k. **Cash total $67,500**. Render prizes are **$1,000+$750+$500=$2,250 credits**, not cash. Organizer Oct 28 update uses $69,750 aggregate prizes, while main event card says $67,500 cash; these are consistent when credits are separated.

The rules permit existing projects only when significantly updated during the contest period. Judges must be able to run the application or access a working demo. Public source code requires a detectable open-source license. Winner payment is conditional on identity/eligibility and completed forms, with tax obligations and possible delivery up to 60 days after forms. No payout is established for this repo.

PayPal's first-party sandbox guide (updated Oct 14) confirms mock transactions do not touch live user accounts. Sandbox account access itself has not been tested. Any required judging access must be arranged without publishing secrets or account credentials in Git.

**Next:** Build agent should verify participant join, sandbox signup and feasible demo before promoting case beyond triage. Reconcile this PR against PR #223 and #226 queue changes. Chronological Aug 30 replay gate still blocks canonical source-history advancement.
