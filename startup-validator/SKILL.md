---
name: startup-validator
description: Guided startup idea validation through a 5-stage pipeline (Problem → Solution → Market → Business Model → Synthesis). Run AFTER startup-research. Produces structured output templates T1-T12 and a Sequoia-format pitch deck outline. Use when someone wants to systematically validate a startup idea before building or fundraising.
argument-hint: "[research-briefing-file or idea description]"
allowed-tools: WebSearch, WebFetch, Bash(python3 *)
---

## Pipeline Overview

```
[startup-research] → Stage 0 → Stage 1 → Stage 2 → Stage 3 → Stage 4 → Synthesis
      ↑                  ↑         ↑         ↑         ↑         ↑          ↑
  Autonomous         Idea      Problem   Solution   Market   Business    Pitch Deck
  web research      Intake   Validation Validation Validation  Model     from Evidence
```

Each stage has:
- Specific tasks for Claude to do autonomously
- Questions/experiments for the founder to run
- Explicit gate criteria (proceed / iterate / kill)
- An output template to generate

**CRITICAL — B2B/B2C routing:** Before entering any stage, confirm the business model archetype (B2C Direct / B2B SMB / B2B Mid-Market / B2B Enterprise / Marketplace). Load `references/b2b-b2c-routing.md` at Stage 0 and keep active throughout. All gate criteria, interview counts, experiment types, and templates adjust per archetype.

---

## Operating Principles

Follow these throughout every stage — they override any default behavior:

1. **Idea first** — Always open by inviting the founder to describe their vision. Never lead with business mechanics, archetype classification, or administrative questions. Let classification emerge from the conversation.

2. **Environment-aware output** — Detect whether running in Claude.ai (browser/cowork) or Claude Code (terminal):
   - **Claude.ai / cowork:** Render stage outputs, analyses, and charts as interactive HTML visuals directly in the chat. Structured templates can be shown inline with full formatting.
   - **Claude Code (terminal):** All structured content goes to `[idea-slug]/[stage]/[filename].md`. Only questions, confirmations, and 3–5 bullet summaries appear in the terminal.
   - **Detection signal:** If the user is in a browser chat or mentions "cowork", use interactive output. If running via CLI, use file-first output.

3. **Interactive charts in Claude.ai** — When in Claude.ai or cowork, generate inline HTML charts for:
   - Assumption map (2×2 Importance × Uncertainty)
   - Interview convergence tracker (progress bar per pain point)
   - Competitor matrix (scatter/bubble chart)
   - TAM/SAM/SOM funnel
   - Unit economics sensitivity (LTV:CAC across scenarios)
   Do not narrate what charts you will make — just produce them.

4. **File-first output in terminal** — Save every stage output to `[idea-slug]/[stage]/[filename].[md|xlsx]`. Announce the filename, save it, return a bullet summary.

5. **Background work stays silent** — Never show script paths or shell commands. Ask: "Should I run a background [competitive / market / trend] scan?" Run it if yes, save to file or render as chart.

6. **Discovery interview for B2B** — Use "discovery interview" or "stakeholder interview" — not "Mom Test". The underlying principle (ask about past behavior, not opinions) is the same. But B2B buyers are economic decision-makers.

7. **Act, don't suggest** — State actions as done: "I've drafted…" / "I started…" / "Here's the…". Never "My recommendation is…" or "You might want to…".

8. **Results as bullets** — All research, script output, and compiled data summarized in 3–7 bullets. Full detail in files or interactive visuals.

---

## Stage 0: Idea Intake & Framing

**Input:** Research Briefing from `startup-research` (or raw founder description if research skipped)
**Output:** Idea Framing Document (template: `references/templates/T1-idea-framing.md`)
**Runtime:** 10-15 minutes

### Claude's tasks

1. **Understand the idea first** — if a Research Briefing was provided, confirm you've read it and summarize the idea back in 2 sentences. If the founder is starting fresh, open with: "Tell me about your idea — what does it do and who is it for?" Let the idea lead; classification follows.

2. **Classify archetype** — infer from the idea description first. If still unclear after hearing the idea:
   - "Is the end customer paying out of their own pocket, or is a business buying this?"
   - If B2B: "What size companies are you imagining as your first customers?"
   - Brief the founder: *"This looks like a [archetype] play. Validation from here will focus on [1-sentence summary]."*

3. **Extract assumptions** — parse all implicit and explicit assumptions from the idea:
   - Desirability: "Customers have this problem and want this solution"
   - Viability: "We can build a sustainable business around this"
   - Feasibility: "We can build this product"
   - Ethical: "This creates value for everyone involved"

4. **Map assumptions** onto Importance × Uncertainty 2×2 matrix

5. **Identify Riskiest Assumption** — the one that collapses everything if false

6. **Generate Validation Plan** — ordered experiment sequence across Stage 1-4

7. **Output** Idea Framing Document → save to `[idea-slug]/stage-0/idea-framing.md`; state filename + 3-bullet summary in terminal

---

## Stage 1: Problem Validation

**Core question:** Does this problem exist? Is it painful enough to pay to solve?
**Output:** Problem Validation Report (template: `references/templates/T2-problem-validation-report.md`)

### Claude's tasks

- Search Reddit, HN, Quora for organic problem discussions → compile pain point frequency data; ask if a background trend scan should run
- Generate interview scripts tailored to the specific idea and archetype:
  - **B2C:** Customer discovery interview (Mom Test principles — ask about past behavior, never opinions)
  - **B2B:** Stakeholder discovery interview (economic buyer + end user scripts; focus on quantified cost and org commitment signals)
- Save interview scripts to `[idea-slug]/stage-1/interview-scripts.md`; state filename in terminal
- Create interview tracking table → save to `[idea-slug]/stage-1/interview-tracker.xlsx`
- After founder pastes in interview notes → analyze patterns, score severity, identify convergence; save findings to `[idea-slug]/stage-1/problem-validation-report.md`

### B2B/B2C routing (see `references/b2b-b2c-routing.md` for full tables)

| | B2C | B2B |
|--|-----|-----|
| Interviews needed | 20-30 | 10-15 (must include decision-makers) |
| Interview length | 15-20 min | 30-60 min |
| Finding subjects | Reddit, panels, social | LinkedIn, warm intros, industry events |
| Success signal | Emotional intensity + workaround behavior | Quantified cost of problem + org commitment |
| Commitment currency | Email signup, pre-order | Meeting with their boss, pilot discussion, LOI |

### Gate criteria

**B2C proceed:**
- 20+ interviews with pattern convergence
- >70% of segment recognizes the problem
- Evidence of workarounds or spending
- At least 5 commitment signals

**B2B proceed:**
- 10+ interviews WITH decision-makers or budget holders
- >80% recognize AND quantify the problem
- Can articulate cost in €/$/time per year
- At least 1 organizational commitment signal

**Kill signals (either archetype):**
- <50% problem recognition across interviews
- No emotional intensity (B2C) or no quantified cost (B2B)
- Zero commitment signals
- "That's interesting, keep me posted" = polite rejection

---

## Stage 2: Solution Validation

**Core question:** Will people change behavior for THIS solution?
**Output:** Experiment Card(s) + Solution Validation Report (templates: T3, T4)

### Claude's tasks

- Design experiment card(s) for the archetype-appropriate experiment type → save to `[idea-slug]/stage-2/experiment-cards.md`
- **B2C:** Draft landing page copy for Fake Door test → save to `[idea-slug]/stage-2/landing-page-copy.md`
- **B2B:** Draft cold outreach emails and LOI template → save to `[idea-slug]/stage-2/outreach-templates.md`
- Create survey instruments for solution validation → save to `[idea-slug]/stage-2/survey.md`
- Calculate conversion rates from raw data founder provides; return bullet summary in terminal
- Research comparable MVPs and their results → 3–5 bullets in terminal

### Experiment selection by archetype

| Experiment | B2C | B2B |
|-----------|-----|-----|
| Fake Door / Landing Page | ✅ Primary | ⚠️ Limited (B2B buyers don't buy from landing pages) |
| Concierge MVP | ⚠️ Doesn't scale | ✅ Primary (white-glove IS the product initially) |
| LOI / Pre-sales | ⚠️ High-ticket only | ✅ Primary validation |
| Pilot program | ❌ | ✅ Essential for enterprise |
| Crowdfunding | ✅ Excellent | ❌ Businesses don't Kickstart |
| Sales Conversation Test | ❌ | ✅ Outreach → calls → proposals |

**B2B Sales Conversation Test (when no product exists yet):**
1. Identify 20-30 target companies via LinkedIn
2. Cold outreach with problem-first messaging (not product pitch)
3. Goal: book 10 discovery calls
4. Present value proposition in calls (slides, not product)
5. Ask: "If this existed today, what would next steps look like?"
- Success: 10+ calls booked from 30 outreach; 3+ advance to proposal
- Kill: <3 calls booked OR all end with "interesting, keep me posted"

### Gate criteria

**B2C proceed:**
- Fake Door: >5% signup from cold traffic (500+ visitors), OR
- Crowdfunding: funding goal met in first 48h, OR
- Pre-orders: 50+ with real payment

**B2B proceed:**
- 3+ LOIs or signed pilot agreements (SMB: 5+), OR
- 1 enterprise customer commits budget + timeline, OR
- >30% of discovery calls advance to proposal stage

---

## Stage 3: Market Validation

**Core question:** Is the market big enough and reachable?
**Output:** Market Sizing Workbook + Competitive Matrix + Why Now Brief (templates: T5, T6, T7)

### Claude's tasks (automated)

- Ask: "Should I run background market and competitive data scans?" — if yes, run and save to `[idea-slug]/stage-3/`
- Calculate TAM/SAM/SOM using triangulation (bottom-up primary, top-down cross-check, value-theory sanity check)
- Generate market sizing workbook (`[idea-slug]/stage-3/[slug]-market-sizing.xlsx`) — three-method triangulation with live formulas; founder fills highlighted input cells
- Build competitive matrix as Excel workbook (`[idea-slug]/stage-3/[slug]-competitive-matrix.xlsx`) — sortable by axis, with conditional formatting on key differentiators
- Research "Why Now" factors → save Porter's Five Forces + Why Now brief to `[idea-slug]/stage-3/market-analysis.md`
- Terminal summary: TAM/SAM/SOM headline numbers + top 3 competitive insights

### Key outputs

- TAM/SAM/SOM with three-method triangulation (divergence >30% → revise inputs)
- Competitive matrix with archetype-appropriate axes (B2C: price vs experience; B2B: features vs implementation ease)
- "Why Now" brief with trend data and timing assessment

---

## Stage 4: Business Model Validation

**Core question:** Can we build a sustainable business?
**Output:** Unit Economics Model + Pricing Analysis (templates: T8, T9)

### Claude's tasks

- Generate unit economics workbook → `[idea-slug]/stage-4/[slug]-unit-economics.xlsx` — sheets for B2C Model, B2B Model, Sensitivity Analysis (LTV:CAC across churn/CAC/price scenarios), Benchmark comparison; founder fills highlighted input cells only
- Calculate unit economics (CAC, LTV, payback) from founder-provided data; return 3–5 bullet summary in terminal
- Research pricing benchmarks for comparable products → bullets in terminal
- Generate pricing analysis workbook → `[idea-slug]/stage-4/[slug]-pricing-analysis.xlsx` — Van Westendorp data entry with PMC/AAC/IDP/IPP formulas pre-wired; founder pastes survey responses into the data sheet
- Research channel benchmarks (CPC/CTR by channel and industry) → bullets in terminal
- Draft Business Model slide content → save to `[idea-slug]/stage-4/business-model-slides.md`

### Unit economics by archetype

| Metric | B2C | B2B SMB | B2B Mid-Market | B2B Enterprise |
|--------|-----|---------|----------------|----------------|
| Target LTV:CAC | >3:1 | >3:1 | >4:1 | >5:1 |
| CAC payback | <3 mo | <6 mo | <12 mo | <18 mo |
| Monthly churn target | <5% | <3% | <2% | <1% |

### Sean Ellis test

Survey users who've used the product 3+ times. **≥40% "very disappointed" = PMF.**
- **B2B:** Survey END USERS, not the economic buyer. Also check separately: would the buyer renew?

---

## Synthesis

**Output:** Validation Scorecard + Pitch Deck Outline (templates: T10, T11)

Combine all stage evidence into:
1. **Validation Scorecard** — scores per stage, overall assessment, top risks, bias alerts
2. **Pitch Deck Outline** — Sequoia 10-slide structure, every claim backed by specific validation evidence
3. **Risk Register** — ongoing tracking table (template: T12)

**Evidence-linking rules for T11 (Pitch Deck Outline):**
- Every slide claim must reference the specific template that supplies its evidence (e.g., "T2 interview data", "T3 experiment results", "T5 market sizing workbook")
- If a stage has not been completed, mark the claim: `[PENDING Stage X — do not use in investor conversations until filled]`
- A pitch deck with PENDING items is a planning tool, not an investor-ready document
- The deck is investor-ready only when every PENDING is replaced with real evidence from a completed template

---

## Ongoing: Bias Detection

Flag these **at every stage, not just at the end**. When a bias is detected, name it explicitly and state the intervention before continuing.

| Bias | Signal | Intervention |
|------|--------|-------------|
| Confirmation bias | Founder only hears validating signals | Require 3+ disconfirming interviews before proceeding |
| Survivorship bias | Only talking to people who like the idea | Deliberately interview skeptics and people who tried alternatives |
| Solution-first thinking | Designing before understanding problem | Return to Stage 1; no mockups until gate criteria met |
| Vanity metrics | Citing impressions / likes / traffic without conversion | Ask: "What did they actually do?" — only actions count |
| False positive signals | Friends and family saying yes | Require strangers and paying signals; warm contacts = hypothesis only |
| Premature scaling | Jumping to growth before PMF | Check Sean Ellis score first; ≥40% "very disappointed" required |

**Archetype-specific must-catch biases:**
- **B2C:** Confirmation bias — especially when the founder IS the target user. Their own pain is real but not representative.
- **B2B SMB:** False positive signals — friendly business owners describing pain ≠ paying customers. Require commitment currency.
- **B2B Enterprise:** Premature scaling — optimizing the product/ML/technology before validating that the buying process (procurement, model risk, security review) can actually close a deal.
- **Marketplace:** Solution-first thinking — building the platform before confirming both sides will transact through it. Run a concierge experiment first.

---

## Additional resources

- B2B/B2C routing tables (load at Stage 0): [references/b2b-b2c-routing.md](references/b2b-b2c-routing.md)
- Bias detection library: [references/bias-library.md](references/bias-library.md)
- Stage 1 — Problem validation (Mom Test, severity scoring): [references/stage-1-problem.md](references/stage-1-problem.md)
- Stage 2 — Solution validation (experiment types, Van Westendorp): [references/stage-2-solution.md](references/stage-2-solution.md)
- Stage 3 — Market validation (TAM/SAM/SOM, Porter's Five Forces): [references/stage-3-market.md](references/stage-3-market.md)
- Stage 4 — Business model (unit economics, Sean Ellis): [references/stage-4-business-model.md](references/stage-4-business-model.md)
- Output templates T1–T12: [references/templates/](references/templates/)
