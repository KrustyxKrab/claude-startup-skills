---
name: startup-pitch-deck
description: Builds a professional 10-slide Sequoia-format pitch deck directly in Figma using validated startup data from startup-validator. Requires claude-talk-to-figma MCP. Run after startup-validator is complete.
argument-hint: "[idea-slug or path to idea folder]"
---

## What this skill does

- Reads startup-validator output (T1–T12 templates) from `[idea-slug]/` folder
- Connects to Figma via claude-talk-to-figma MCP
- Builds 10 slides directly in Figma using MCP tool calls
- Each slide follows the professional design system defined in `references/design-system.md`

## Prerequisites

- startup-validator completed with output in `[idea-slug]/` folder
- claude-talk-to-figma MCP installed and running (see `references/setup-guide.md`)
- Figma Desktop open with the Claude MCP plugin active and connected

## Operating Principles

1. **Read before building** — parse all validator output files first, extract the data, THEN start building slides. Do not make up data.
2. **Confirm before starting** — after reading validator output, summarise the 5 key data points you'll use for each slide. Ask the founder to confirm before touching Figma.
3. **Build slide by slide** — create all elements for one slide, confirm it looks right, then move to the next.
4. **Exact design system** — follow `references/design-system.md` precisely. Do not improvise colors, fonts, or sizes.
5. **Act, don't narrate** — call the MCP tools directly. Don't say "I will now create a rectangle." Just create it.

## MCP connection

Before any Figma work: connect to the MCP channel. The founder will have the channel ID from the Figma plugin. Say: "What's your Figma channel ID?" then call `connect_to_figma` with the provided channel ID.

Verify the connection is live before issuing any draw commands. If connection fails, refer the founder to `references/setup-guide.md`.

---

## Data extraction map

Where to read data for each slide:

| Slide | Source file(s) | Key fields |
|-------|---------------|------------|
| Cover | `stage-0/idea-framing.md` | company name, one-liner tagline, archetype, sector |
| Problem | `stage-1/problem-validation-report.md` | top 2-3 pain points, severity scores, strongest customer quote, interview count |
| Solution | `stage-2/experiment-cards.md` or `stage-2/outreach-templates.md` | value proposition, 3 core benefits/features |
| Why Now | `[slug]-trends.xlsx` summary or `stage-3/market-analysis.md` | 3 timing factors, trend data points, inflection events |
| Market | `[slug]-market-sizing.xlsx` or `stage-3/market-analysis.md` | TAM, SAM, SOM, CAGR, market context |
| Product | `stage-2/experiment-cards.md` | how it works (3-step), 4 core features |
| Business Model | `stage-4/business-model-slides.md` | revenue model type, ACV/ARPU, LTV:CAC ratio, payback period, pricing tiers |
| Traction | `stage-1/problem-validation-report.md` + `stage-2/` folder | interview count, problem recognition %, commitments, LOIs/pilots, strongest quote |
| Team | `stage-0/idea-framing.md` | founder names, roles, backgrounds, "why us" statement, open roles |
| The Ask | `stage-0/idea-framing.md` or ask founder directly | funding amount, currency, round stage, 3 use-of-funds items with percentages, 12-month milestone |

If a field is missing from the validator output, ask the founder for that specific data point before proceeding to that slide. Never fabricate data.

---

## Build sequence

For each slide, execute MCP tool calls in this exact order:

1. `create_frame` — slide canvas at correct x/y position (see design-system.md for Y positions)
2. `create_rectangle` — full-bleed background fill (bg_dark: r=15, g=23, b=42)
3. Accent elements — left bar, decorative shapes per slide spec
4. `create_rectangle` for the top divider line (slides 2–10 only)
5. Slide number text (slides 2–10 only)
6. Section label (H2, uppercase, accent_blue)
7. Title (H1, text_primary)
8. Content elements — cards, columns, metric callouts per slide spec
9. For each card: `create_rectangle` (card background) then `create_text` elements on top
10. Style every element immediately after creation: `set_font_name`, `set_font_size`, `set_fill_color`, `set_font_weight`, `set_text_align`

Full per-slide specifications with exact pixel positions are in `references/slide-templates.md`.
Design system (exact RGB values, font sizes, all layout constants) is in `references/design-system.md`.

After completing each slide, pause and say: "Slide [N] complete — does it look right in Figma?" Wait for confirmation before moving to slide N+1.

---

## Pre-build checklist

Before touching Figma, confirm all of the following:

- [ ] Figma channel ID obtained from founder
- [ ] MCP connected successfully
- [ ] All validator files read
- [ ] Data summary confirmed by founder (5 key points per slide)
- [ ] Figma file open and blank canvas ready

## Error handling

- If an MCP tool call fails: retry once, then report the exact error message to the founder.
- If a font ("Inter") is not found in Figma: fall back to "SF Pro Display", notify the founder, and suggest installing Inter from fonts.google.com.
- If a validator file is missing: note which slide is affected, ask the founder for the missing data, and continue with other slides.
- If the channel connection drops mid-build: ask for the channel ID again and reconnect before resuming.
