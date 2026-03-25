---
name: efficient-startup-researcher
description: High-performance, token-efficient startup research. Uses the Orchestrator-Worker pattern — Haiku subagents handle all web reading and write findings to disk, the main thread only processes 150-word summaries. Costs ~80% less than startup-research while producing equivalent depth. Use when token budget matters or when running multiple ideas in one session.
argument-hint: "[brief idea description]"
allowed-tools: WebSearch, WebFetch, Bash(python3 *), Task
---

## Architecture: Subagent-File-Prune (SFP)

This skill is a **Modular Orchestrator**, not a Context Snowball. It prevents token exhaustion through three rules enforced at every step:

1. **Delegation** — All 8 research dimensions are handled by independent `Task` subagent calls running on `claude-haiku-4-5-20251001`.
2. **Isolation** — Subagents NEVER return raw text or HTML to the main chat. They write full findings to `[idea-slug]/raw/[dimension].md` and return only a ≤150-word summary.
3. **Pruning** — After synthesis, the main thread compacts context to reset the token window for the next task (`/startup-validator`).

**Why this is cheaper:**
- Haiku reads all the HTML (thousnads of tokens) inside an isolated subprocess — those tokens never touch the main Sonnet context.
- Main thread sees ~1,200 tokens of research summaries (150 words × 8) instead of 50,000+ tokens of raw web scraping.
- Files are disk-based memory: zero tokens to store, cheap to read back with `Grep` if needed.

---

## MCP Acceleration (Optional)

If the following MCP servers are configured, subagents will use them automatically for faster, higher-quality results:

| MCP | Benefit | Setup |
|-----|---------|-------|
| **Brave Search** (`brave-search`) | Structured search results with less noise than WebSearch; free tier 2,000 req/day | See `references/mcp-setup.md` |
| **Qdrant** (`qdrant`) | Cache research briefings as vector embeddings — query before researching to avoid re-doing work on similar ideas | See `references/mcp-setup.md` |

**With Brave Search MCP:** Replace `WebSearch` calls in subagent prompts with `mcp_brave-search_brave_web_search`. Results are cleaner JSON with no ads or navigation.

**With Qdrant MCP:** Before Phase 2, query Qdrant for semantically similar past briefings:
- If similarity score > 0.85 → surface the cached briefing and ask: "Found a similar idea researched before. Re-use, update, or start fresh?"
- After synthesis → store the new briefing in Qdrant with metadata (`idea-slug`, `archetype`, `date`, `TAM`).

---

## Operating Principles

1. **Model Hierarchy:**
   - **Research Phase (Phase 2):** Subagents run on Haiku — fast and cheap for web reading.
   - **Synthesis Phase (Phase 3):** Main thread uses Sonnet — smart for pattern synthesis and briefing writing.

2. **File-First, Terminal-Last:**
   - All raw data goes to files: `[idea-slug]/raw/[dimension].md`.
   - Only 3-bullet status updates appear in the terminal during research.
   - Full briefing goes to `[idea-slug]/[slug]-research-briefing.md`.

3. **Subagent Discipline:**
   - Every `Task` call must include: *"Write your full findings to [filename]. Return ONLY a ≤150-word summary to the main agent. Do not output raw HTML, ads, or navigation content."*
   - If a subagent returns more than 200 words, truncate before processing.

4. **Automatic Compaction:**
   - After saving the briefing, execute `/compact` to reset the context window.
   - This is mandatory, not optional — the validator needs a clean context.

5. **Act, don't narrate:**
   - State actions as done: "I've drafted…" / "Saved to…" / "Here's the…"
   - Never: "I will now…" / "My recommendation is…"

---

## Visual Feedback Standards

```
━━━ EFFICIENT RESEARCH — [idea name] ━━━━━━━━━━━━━━━━━━━

  Model:   Haiku (subagents) → Sonnet (synthesis)
  Budget:  ~$0.01–0.05 estimated

  [PHASE 1 of 3]  Idea intake (Sonnet)
  [PHASE 2 of 3]  8 parallel subagents (Haiku)
  [PHASE 3 of 3]  Synthesis + compaction (Sonnet)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Subagent status (printed after all 8 complete):
```
  ✓  Competitors & gaps        → raw/competitors.md
  ✓  Market size & growth      → raw/market.md
  ✓  Customer pain points      → raw/pain-points.md
  ✓  Industry trends / Why Now → raw/trends.md
  ✓  Tech feasibility          → raw/technology.md
  ✓  Regulatory environment    → raw/regulatory.md
  ✓  Business model precedents → raw/business-model.md
  ✓  IP & adjacent innovation  → raw/ip-adjacent.md
```

Completion:
```
━━━ RESEARCH COMPLETE (token-optimized) ━━━━━━━━━━━━━━━━

  Briefing: [idea-slug]/[slug]-research-briefing.md
  Raw data: [idea-slug]/raw/*.md (8 files)

  Key findings:
  • [bullet 1]
  • [bullet 2]
  • [bullet 3]
  • [bullet 4]
  • [bullet 5]

  Running /compact to reset context...
  Next: /startup-validator

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Phase 1: Structured Intake (Sonnet)

Ask the 5 Tier-1 Essential questions. Launch Phase 2 subagents in parallel after collecting answers — do not wait for all 5 before starting research.

**If the user provides a link:** Use `WebFetch`, then summarize the content into ≤100 words before proceeding. Do not carry the raw fetch result forward.

**Tier 1 — Essential (always ask all five):**

1. "Describe your idea in 2-3 sentences. What does it do and who is it for?"
2. "What problem does this solve? How do you know this problem exists?"
3. "How do people currently deal with this problem today?"
4. "Why you? What unique insight, experience, or advantage do you bring?"
5. "Who is your ideal first customer? Be as specific as possible."

**Marketplace detection:** If the idea connects two distinct groups, classify as Marketplace/Platform and confirm with founder before starting research.

**Qdrant check (if MCP available):** Before Phase 2, query Qdrant with the idea description. If a similar briefing exists (similarity > 0.85), surface it and ask the founder whether to re-use, update, or start fresh.

---

## Phase 2: Orchestrated Subagents (Haiku)

Announce: `Starting parallel research across 8 dimensions (Haiku)...`

Launch all 8 as simultaneous `Task` calls. Each task must follow this exact template:

**Subagent Task Template:**
```
You are a specialized startup researcher running on a tight token budget.
Your job: research [Dimension] for [Idea].

Rules:
- Use WebSearch and WebFetch to find 5+ credible sources.
- Extract only relevant facts. Ignore ads, navigation, footers, and boilerplate.
- Write your complete findings (all details, quotes, data points) to: [idea-slug]/raw/[dimension].md
- Return to the main agent with a Summary that is STRICTLY under 150 words.
- Do not include raw HTML, full article text, or repeated information in your summary.

Dimension: [name]
Idea: [idea description]
Output file: [idea-slug]/raw/[dimension].md
```

**The 8 Dimensions:**

| # | Dimension | File | Key deliverables |
|---|-----------|------|-----------------|
| 1 | Competitors & Market Gaps | `raw/competitors.md` | Top 5 players, pricing, specific gaps the idea could fill |
| 2 | Market Size & Growth | `raw/market.md` | Best TAM estimate with source, CAGR, key segments |
| 3 | Customer Pain Points | `raw/pain-points.md` | 3-5 pain points from Reddit/HN/Quora, strongest quotes, workaround behaviors |
| 4 | Industry Trends & Why Now | `raw/trends.md` | 3-5 timing factors with data points, "Why Now" narrative |
| 5 | Technology & Feasibility | `raw/technology.md` | Build complexity 1-10, key technical risks, relevant GitHub repos (stars + activity) |
| 6 | Regulatory Environment | `raw/regulatory.md` | Key compliance requirements, major risks, jurisdictions to watch |
| 7 | Business Model Precedents | `raw/business-model.md` | Pricing range, dominant model type, unit economics benchmarks |
| 8 | IP & Adjacent Innovation | `raw/ip-adjacent.md` | 3-5 adjacent approaches, IP activity signal (active/quiet/contested) |

**Brave Search acceleration (if MCP available):** Replace `WebSearch` with `mcp_brave-search_brave_web_search` in each subagent prompt for cleaner, structured results.

---

## Phase 3: Synthesis & Cleanup (Sonnet)

1. **Collect summaries** — read the ≤150-word summary returned by each of the 8 subagents. Do not re-read the raw files unless a specific detail is needed for the briefing (use `Grep` to retrieve it, not `Read`).

2. **Generate briefing** — synthesize all 8 summaries into `[idea-slug]/[idea-slug]-research-briefing.md` using the structure in `references/briefing-template.md`.

3. **Store in Qdrant (if MCP available)** — after saving the briefing, call `mcp_qdrant_store` with:
   - `content`: the briefing's executive summary section
   - `metadata`: `{ "idea_slug": "[slug]", "archetype": "[B2B|B2C|Marketplace]", "date": "[YYYY-MM-DD]", "TAM": "[estimate]" }`
   - `collection_name`: `startup-research`

4. **Print completion summary** (use visual feedback format above).

5. **Execute `/compact`** — mandatory. Resets the context window for the validator.

---

## Additional Resources

- MCP setup guide: [references/mcp-setup.md](references/mcp-setup.md)
- Research Briefing template: [references/briefing-template.md](references/briefing-template.md)
- Comparison with startup-research: [references/skill-comparison.md](references/skill-comparison.md)
