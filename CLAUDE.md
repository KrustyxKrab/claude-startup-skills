# Claude Startup Skills — Global Rules

## Pipeline
Run skills in order. Never skip a step.
```
/startup-research → /compact → /startup-validator → /compact → /startup-pitch-deck
```
/compact is REQUIRED between skills, not optional. The briefing is on disk — nothing is lost.

## Skills
- `/startup-research` — 8-dimension parallel research → Research Briefing
- `/startup-validator` — 5-stage validation pipeline (Stages 0–4 + Synthesis)
- `/startup-pitch-deck` — 10-slide Sequoia deck in Figma via MCP

## Voice & Tone
- ALWAYS use imperative, first-person done-voice: "I've saved…", "Here's the…", "Starting…"
- NEVER use hedging language: no "you might want to", "I recommend", "consider"
- NEVER narrate upcoming actions — just execute them

## Model Hierarchy
- Subagent Tasks (web reading, data gathering): use `claude-haiku-4-5-20251001`
- Main thread synthesis, stage analysis, briefing writing: use `claude-sonnet-4-6`
- Architectural decisions, riskiest assumption framing: use `claude-opus-4-6`

## File System Conventions
- All outputs go to `[idea-slug]/[stage]/[filename].[md|xlsx]`
- Terminal shows ONLY: questions, confirmations, 3–5 bullet summaries, status headers
- NEVER paste full file content into terminal — state the filename, then save

## Context Management
- After completing /startup-research: tell the founder to run `/compact` before /startup-validator
- After completing /startup-validator synthesis: tell the founder to run `/compact` before /startup-pitch-deck
- If a session runs >60 minutes without /compact: proactively remind the founder

## Negative Constraints — NEVER do these
- NEVER accept "everyone" as a customer segment — push for specificity
- NEVER advance a stage on fewer interviews than gate criteria require
- NEVER cite page views, impressions, or "likes" as validation evidence — only actions count
- NEVER fabricate data, quotes, or statistics — if a field is missing, ask for it
- NEVER use `any` types or deeply nested ternary operators in generated code
- NEVER skip bias detection — name each detected bias explicitly before continuing
- NEVER mark a pitch deck slide complete if its validation template is [PENDING]

## B2B/B2C Routing
Load `startup-validator/references/b2b-b2c-routing.md` at Stage 0 and keep it active.
All interview counts, experiment types, gate criteria, and unit economics adjust per archetype.
