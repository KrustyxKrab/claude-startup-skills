# Slide Templates — startup-pitch-deck

Per-slide layout specifications with exact element positions, MCP tool call sequences, and data sources.

All coordinates are relative to each slide's top-left corner (0, 0).
All color values reference tokens defined in `design-system.md`.
All font names are "Inter" (fallback: "SF Pro Display").

---

## SLIDE 1 — Cover

**Purpose:** First impression. Company name, tagline, archetype.
**Data source:** `stage-0/idea-framing.md`
**Y position on canvas:** 0

### MCP tool call sequence

**Step 1 — Slide frame**
```
create_frame: x=0, y=0, w=1280, h=720, name="01 — Cover"
```

**Step 2 — Background**
```
create_rectangle: x=0, y=0, w=1280, h=720
set_fill_color: r=15, g=23, b=42  (bg_dark)
```

**Step 3 — Decorative accent ellipse (subtle glow, top-right)**
```
create_ellipse: x=980, y=-100, w=500, h=500
set_fill_color: r=99, g=102, b=241  (accent_blue)
set_opacity: 8
```

**Step 4 — Category tag background pill**
```
create_rectangle: x=80, y=60, w=140, h=32, corner_radius=6
set_fill_color: r=30, g=41, b=59  (bg_card)
```

**Step 5 — Category tag text**
```
create_text: x=96, y=68, text="[SECTOR]"   (e.g. "B2B SAAS" — uppercase, from archetype)
set_font_name: Inter
set_font_size: 12
set_font_weight: 500
set_fill_color: r=99, g=102, b=241  (accent_blue)
```

**Step 6 — Company name (Display)**
```
create_text: x=80, y=240, w=900, text="[Company Name]"
set_font_name: Inter
set_font_size: 72
set_font_weight: 700
set_fill_color: r=248, g=250, b=252  (text_primary)
set_text_align: left
```

**Step 7 — Tagline**
```
create_text: x=80, y=340, w=900, text="[One-liner tagline from idea-framing.md]"
set_font_name: Inter
set_font_size: 24
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)
set_text_align: left
```

**Step 8 — Accent divider under tagline**
```
create_rectangle: x=80, y=410, w=120, h=3
set_fill_color: r=99, g=102, b=241  (accent_blue)
```

**Step 9 — Archetype / round / year badge**
```
create_text: x=80, y=434, text="[Archetype] · [Round Stage] · [Year]"
              e.g. "B2B SaaS · Series Seed · 2026"
set_font_name: Inter
set_font_size: 16
set_font_weight: 400
set_fill_color: r=100, g=116, b=139  (text_muted)
```

**Step 10 — Confidential footer**
```
create_text: x=80, y=670, text="Confidential — [Company Name] · [Year]"
set_font_name: Inter
set_font_size: 12
set_font_weight: 400
set_fill_color: r=100, g=116, b=139  (text_muted)
```

---

## SLIDE 2 — Problem

**Purpose:** Establish the pain. Show severity with real evidence.
**Data source:** `stage-1/problem-validation-report.md`
**Y position on canvas:** 820

### Layout overview
Left column (x=80–520): pull-quote from strongest customer interview.
Right column (x=560–1200): 2–3 pain point cards stacked vertically.
Bottom bar: stats summary.

### MCP tool call sequence

**Steps 1–4:** Standard recurring elements (background, left bar, divider, slide number "02 / 10") — see design-system.md.

**Step 5 — Section label**
```
create_text: x=80, y=60, text="THE PROBLEM"
set_font_name: Inter
set_font_size: 13
set_font_weight: 600
set_fill_color: r=99, g=102, b=241  (accent_blue)
set_text_align: left
(letter-spacing: 3px if MCP supports it)
```

**Step 6 — Title**
```
create_text: x=80, y=88, w=900, text="Why [problem domain] is broken."
set_font_name: Inter
set_font_size: 48
set_font_weight: 700
set_fill_color: r=248, g=250, b=252  (text_primary)
```

**Step 7 — Pull-quote: large quotation mark**
```
create_text: x=80, y=160, text="""
set_font_name: Inter
set_font_size: 80
set_font_weight: 700
set_fill_color: r=99, g=102, b=241  (accent_blue)
```

**Step 8 — Pull-quote: quote text**
```
create_text: x=80, y=240, w=420, text="[Strongest customer quote from interviews]"
set_font_name: Inter
set_font_size: 22
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)
(italic if MCP supports it)
```

**Step 9 — Pull-quote: attribution**
```
create_text: x=80, y=430, text="— [Role/Title], [Company type]"
set_font_name: Inter
set_font_size: 14
set_font_weight: 400
set_fill_color: r=100, g=116, b=139  (text_muted)
```

**Steps 10–18 — Pain point cards (repeat for each pain point, up to 3)**

Card 1 (top):
```
create_rectangle: x=560, y=155, w=640, h=145, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

// Severity dot (high severity = amber, medium = blue)
create_ellipse: x=584, y=175, w=12, h=12
set_fill_color: r=245, g=158, b=11  (accent_amber) OR r=99, g=102, b=241 (accent_blue)

// Pain point title
create_text: x=608, y=171, w=570, text="[Pain point name]"
set_font_name: Inter
set_font_size: 20
set_font_weight: 600
set_fill_color: r=248, g=250, b=252  (text_primary)

// Pain point detail
create_text: x=608, y=201, w=570, text="[Frequency or cost data from interviews]"
set_font_name: Inter
set_font_size: 16
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)

// Severity score (right-aligned)
create_text: x=1100, y=171, text="[X]/10"
set_font_name: Inter
set_font_size: 20
set_font_weight: 700
set_fill_color: r=99, g=102, b=241  (accent_blue)
set_text_align: right
```

Card 2 (middle): same structure, y=316 (155 + 145 + 16 gap)
Card 3 (bottom): same structure, y=477 (316 + 145 + 16 gap)

**Step 19 — Bottom stat bar**
```
create_text: x=80, y=628, w=1120,
  text="[X]% of [target segment] experience this problem  ·  [N] interviews conducted  ·  Top pain: [pain point name]"
set_font_name: Inter
set_font_size: 14
set_font_weight: 400
set_fill_color: r=100, g=116, b=139  (text_muted)
set_text_align: center
```

---

## SLIDE 3 — Solution

**Purpose:** Show the answer. Value prop + 3 core benefits.
**Data source:** `stage-2/experiment-cards.md` or `stage-2/outreach-templates.md`
**Y position on canvas:** 1640

### Layout overview
Full-width value proposition headline below the title.
Three equal columns for benefits (01 / 02 / 03).
Optional before/after divider.

### MCP tool call sequence

**Steps 1–4:** Standard recurring elements. Slide number: "03 / 10"

**Step 5 — Section label**
```
create_text: x=80, y=60, text="THE SOLUTION"
[H2 styles: Inter, 13px, SemiBold, accent_blue]
```

**Step 6 — Title**
```
create_text: x=80, y=88, w=900, text="[Solution name]. Built for [audience]."
[H1 styles: Inter, 48px, Bold, text_primary]
```

**Step 7 — Value proposition**
```
create_text: x=80, y=155, w=1000, text="[One-liner value proposition from validator]"
set_font_name: Inter
set_font_size: 24
set_font_weight: 600
set_fill_color: r=248, g=250, b=252  (text_primary)
```

**Steps 8–16 — Three benefit columns**

Column 1 (x=80, w=340):
```
// Number label
create_text: x=80, y=230, text="01"
set_font_name: Inter
set_font_size: 13
set_font_weight: 600
set_fill_color: r=99, g=102, b=241  (accent_blue)

// Benefit title
create_text: x=80, y=256, w=340, text="[Benefit 1 name]"
set_font_name: Inter
set_font_size: 24
set_font_weight: 600
set_fill_color: r=248, g=250, b=252  (text_primary)

// Benefit description
create_text: x=80, y=296, w=340, text="[1-2 sentence description]"
set_font_name: Inter
set_font_size: 18
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)
```

Column 2 (x=440, w=340): same structure, x=440
Column 3 (x=800, w=400): same structure, x=800

**Step 17 — Optional before/after divider line**
```
create_rectangle: x=80, y=510, w=1120, h=1
set_fill_color: r=51, g=65, b=85  (bg_card_light)
```

---

## SLIDE 4 — Why Now

**Purpose:** "The window is open." Show three timing factors with data.
**Data source:** `[slug]-trends.xlsx` summary or `stage-3/market-analysis.md`
**Y position on canvas:** 2460

### Layout overview
Three full-width factor cards stacked vertically (y=160, 306, 452).
Each card has a left accent bar, factor name, explanation, and right-aligned data point.
Source footnote at bottom.

### MCP tool call sequence

**Steps 1–4:** Standard recurring elements. Slide number: "04 / 10"

**Step 5 — Section label**
```
create_text: x=80, y=60, text="WHY NOW"
[H2 styles]
```

**Step 6 — Title**
```
create_text: x=80, y=88, w=900, text="The Window Is Open."
[H1 styles]
```

**Steps 7–18 — Three timing factor cards (repeat pattern)**

Factor Card 1 (y=155):
```
// Card background
create_rectangle: x=80, y=155, w=1120, h=120, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

// Left accent bar
create_rectangle: x=80, y=155, w=4, h=120
set_fill_color: r=99, g=102, b=241  (accent_blue)

// Factor name
create_text: x=112, y=171, w=620, text="[Timing factor 1 name]"
set_font_name: Inter
set_font_size: 22
set_font_weight: 600
set_fill_color: r=248, g=250, b=252  (text_primary)

// Explanation
create_text: x=112, y=203, w=620, text="[1-2 sentence explanation with context]"
set_font_name: Inter
set_font_size: 16
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)

// Data point (right-aligned, prominent)
create_text: x=900, y=171, w=270, text="[+X% or Year or Key stat]"
set_font_name: Inter
set_font_size: 28
set_font_weight: 700
set_fill_color: r=99, g=102, b=241  (accent_blue)
set_text_align: right
```

Factor Card 2 (y=291): same structure, y=291. Use accent_emerald (r=16, g=185, b=129) for left bar.
Factor Card 3 (y=427): same structure, y=427. Use accent_amber (r=245, g=158, b=11) for left bar.

**Step 19 — Source footnote**
```
create_text: x=80, y=598, w=1120,
  text="Sources: [list trend data sources, e.g. Google Trends, NewsAPI, industry reports]"
set_font_name: Inter
set_font_size: 12
set_font_weight: 400
set_fill_color: r=100, g=116, b=139  (text_muted)
```

---

## SLIDE 5 — Market

**Purpose:** Prove the opportunity is large. TAM / SAM / SOM with growth rate.
**Data source:** `[slug]-market-sizing.xlsx` or `stage-3/market-analysis.md`
**Y position on canvas:** 3280

### Layout overview
Three metric cards in a horizontal row (TAM / SAM / SOM) at y=155.
Growth rate statement below.
Market context paragraph.

### MCP tool call sequence

**Steps 1–4:** Standard recurring elements. Slide number: "05 / 10"

**Step 5 — Section label**
```
create_text: x=80, y=60, text="MARKET OPPORTUNITY"
[H2 styles]
```

**Step 6 — Title**
```
create_text: x=80, y=88, w=900, text="A Large and Growing Market."
[H1 styles]
```

**Steps 7–12 — TAM card (x=80, w=340, h=240)**
```
create_rectangle: x=80, y=155, w=340, h=240, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

create_text: x=104, y=179, text="TOTAL ADDRESSABLE MARKET"
[H2 styles: 13px, SemiBold, accent_blue, uppercase]

create_text: x=104, y=207, text="$[X]B"
set_font_name: Inter
set_font_size: 56
set_font_weight: 700
set_fill_color: r=99, g=102, b=241  (accent_blue)

create_text: x=104, y=275, text="Global market, [year]"
set_font_name: Inter
set_font_size: 14
set_font_weight: 500
set_fill_color: r=148, g=163, b=184  (text_secondary)
```

**Steps 13–18 — SAM card (x=440, w=340, h=240)**
Same structure, x=440. Use accent_emerald (r=16, g=185, b=129) for the value.
```
create_text label: "SERVICEABLE ADDRESSABLE MARKET"
create_text value: "$[X]M" — set_fill_color: r=16, g=185, b=129  (accent_emerald)
create_text sub: "Reachable segment, [geography/vertical]"
```

**Steps 19–24 — SOM card (x=800, w=400, h=240)**
Same structure, x=800. Use accent_amber (r=245, g=158, b=11) for the value.
```
create_text label: "SERVICEABLE OBTAINABLE MARKET"
create_text value: "$[X]M" — set_fill_color: r=245, g=158, b=11  (accent_amber)
create_text sub: "Year-1 target revenue"
```

**Step 25 — Growth rate callout**
```
create_text: x=80, y=430, w=1120, text="Market growing at [X]% CAGR through [year]"
set_font_name: Inter
set_font_size: 28
set_font_weight: 600
set_fill_color: r=248, g=250, b=252  (text_primary)
```

**Step 26 — Market context paragraph**
```
create_text: x=80, y=478, w=1120, text="[1-2 sentences on market dynamics, tailwinds, or structural shift driving growth]"
set_font_name: Inter
set_font_size: 18
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)
```

---

## SLIDE 6 — Product

**Purpose:** Show what it is and how it works.
**Data source:** `stage-2/experiment-cards.md`
**Y position on canvas:** 4100

### Layout overview
Left column (x=80, w=480): 4 core features as a list.
Right column (x=600, w=600): "How it works" — 3 numbered steps.

### MCP tool call sequence

**Steps 1–4:** Standard recurring elements. Slide number: "06 / 10"

**Step 5 — Section label**
```
create_text: x=80, y=60, text="THE PRODUCT"
[H2 styles]
```

**Step 6 — Title**
```
create_text: x=80, y=88, w=900, text="The Product."
[H1 styles]
```

**Steps 7–22 — Four feature list items (left column)**

For each feature (4 total), spaced 100px apart starting at y=160:

Feature 1 (y=160):
```
// Bullet rectangle
create_rectangle: x=80, y=169, w=4, h=4
set_fill_color: r=99, g=102, b=241  (accent_blue)

// Feature name
create_text: x=96, y=160, w=450, text="[Feature 1 name]"
set_font_name: Inter
set_font_size: 20
set_font_weight: 600
set_fill_color: r=248, g=250, b=252  (text_primary)

// Feature description
create_text: x=96, y=190, w=450, text="[One line description]"
set_font_name: Inter
set_font_size: 16
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)
```

Feature 2: y=260. Feature 3: y=360. Feature 4: y=460.

**Steps 23–34 — Three "How it works" steps (right column)**

Step numbers at x=600, each block ~140px tall, starting y=160.

How-it-works step 1 (y=160):
```
// Large step number
create_text: x=600, y=160, text="1"
set_font_name: Inter
set_font_size: 48
set_font_weight: 700
set_fill_color: r=99, g=102, b=241  (accent_blue)

// Step title
create_text: x=650, y=165, w=520, text="[Step 1 name]"
set_font_name: Inter
set_font_size: 22
set_font_weight: 600
set_fill_color: r=248, g=250, b=252  (text_primary)

// Step description
create_text: x=650, y=197, w=520, text="[Step 1 description]"
set_font_name: Inter
set_font_size: 16
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)
```

How-it-works step 2: y=300. How-it-works step 3: y=440.

**Step 35 — Connecting dotted line between steps**
```
// Vertical connector between step 1 and step 2
create_rectangle: x=622, y=230, w=2, h=60
set_fill_color: r=51, g=65, b=85  (bg_card_light)

// Vertical connector between step 2 and step 3
create_rectangle: x=622, y=370, w=2, h=60
set_fill_color: r=51, g=65, b=85  (bg_card_light)
```

---

## SLIDE 7 — Business Model

**Purpose:** Prove the business makes money. Show unit economics and pricing.
**Data source:** `stage-4/business-model-slides.md`
**Y position on canvas:** 4920

### Layout overview
Revenue model tag badge below the title.
Three metric cards in a row (ACV/ARPU, LTV:CAC, Payback Period).
Pricing tier note below.

### MCP tool call sequence

**Steps 1–4:** Standard recurring elements. Slide number: "07 / 10"

**Step 5 — Section label**
```
create_text: x=80, y=60, text="BUSINESS MODEL"
[H2 styles]
```

**Step 6 — Title**
```
create_text: x=80, y=88, w=900, text="A Sustainable Business Model."
[H1 styles]
```

**Step 7 — Revenue model badge background**
```
create_rectangle: x=80, y=155, w=220, h=32, corner_radius=6
set_fill_color: r=30, g=41, b=59  (bg_card)
```

**Step 8 — Revenue model badge text**
```
create_text: x=96, y=163, text="[Revenue model type, e.g. SUBSCRIPTION SaaS]"
set_font_name: Inter
set_font_size: 12
set_font_weight: 500
set_fill_color: r=99, g=102, b=241  (accent_blue)
```

**Steps 9–18 — ACV/ARPU metric card (x=80, w=340, h=200)**
```
create_rectangle: x=80, y=203, w=340, h=200, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

create_text: x=104, y=227, text="ANNUAL CONTRACT VALUE"  [H2 styles]

create_text: x=104, y=255, text="$[X]K"
set_font_name: Inter
set_font_size: 56
set_font_weight: 700
set_fill_color: r=99, g=102, b=241  (accent_blue)

create_text: x=104, y=323, text="per customer, annual"  [Metric label styles]
```

**Steps 19–28 — LTV:CAC card (x=440, w=340, h=200)**
```
create_rectangle: x=440, y=203, w=340, h=200, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

create_text: x=464, y=227, text="LTV : CAC RATIO"  [H2 styles]

create_text: x=464, y=255, text="[X]:1"
set_font_name: Inter
set_font_size: 56
set_font_weight: 700
// accent_emerald if ratio > 3:1, accent_amber if < 3:1
set_fill_color: r=16, g=185, b=129  (accent_emerald)  OR  r=245, g=158, b=11 (accent_amber)

create_text: x=464, y=323, text="target > 3:1 for healthy unit economics"  [Metric label styles]
```

**Steps 29–38 — Payback Period card (x=800, w=400, h=200)**
```
create_rectangle: x=800, y=203, w=400, h=200, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

create_text: x=824, y=227, text="PAYBACK PERIOD"  [H2 styles]

create_text: x=824, y=255, text="[X] months"
set_font_name: Inter
set_font_size: 48
set_font_weight: 700
set_fill_color: r=99, g=102, b=241  (accent_blue)

create_text: x=824, y=323, text="to recover CAC"  [Metric label styles]
```

**Step 39 — Pricing tiers note**
```
create_text: x=80, y=438, w=1120,
  text="Pricing: [Tier 1 name] $[X]/mo  ·  [Tier 2 name] $[X]/mo  ·  [Tier 3 name] $[X]/mo"
set_font_name: Inter
set_font_size: 18
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)
```

---

## SLIDE 8 — Traction

**Purpose:** Show what you've proven. Early validation signals build trust.
**Data source:** `stage-1/problem-validation-report.md` + `stage-2/` folder
**Y position on canvas:** 5740

### Layout overview
2×2 grid of traction cards (each w=530, h=190, gap=24px).
Gate status strip at bottom.

### Card positions
- Top-left: x=80, y=155
- Top-right: x=634, y=155
- Bottom-left: x=80, y=369
- Bottom-right: x=634, y=369

### MCP tool call sequence

**Steps 1–4:** Standard recurring elements. Slide number: "08 / 10"

**Step 5 — Section label**
```
create_text: x=80, y=60, text="EARLY VALIDATION"
[H2 styles]
```

**Step 6 — Title**
```
create_text: x=80, y=88, w=900, text="Early Validation."
[H1 styles]
```

**Steps 7–12 — Top-left card: Interviews conducted**
```
create_rectangle: x=80, y=155, w=530, h=190, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

create_text: x=104, y=175, text="INTERVIEWS CONDUCTED"  [H2 styles]

create_text: x=104, y=203, text="[N]"
set_font_name: Inter
set_font_size: 56
set_font_weight: 700
set_fill_color: r=99, g=102, b=241  (accent_blue)

create_text: x=104, y=271, text="customer discovery interviews"  [Metric label styles]
```

**Steps 13–18 — Top-right card: Problem recognition rate**
```
create_rectangle: x=634, y=155, w=530, h=190, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

create_text: x=658, y=175, text="PROBLEM RECOGNITION"  [H2 styles]

create_text: x=658, y=203, text="[X]%"
set_font_name: Inter
set_font_size: 56
set_font_weight: 700
set_fill_color: r=16, g=185, b=129  (accent_emerald)

create_text: x=658, y=271, text="confirmed the problem in interviews"  [Metric label styles]
```

**Steps 19–24 — Bottom-left card: Strongest commitment signal**
```
create_rectangle: x=80, y=369, w=530, h=190, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

create_text: x=104, y=389, text="COMMITMENT SIGNALS"  [H2 styles]

create_text: x=104, y=417, text="[N] [LOIs / pilots / waitlist signups]"
set_font_name: Inter
set_font_size: 28
set_font_weight: 600
set_fill_color: r=248, g=250, b=252  (text_primary)

create_text: x=104, y=455, text="[Description: e.g. letters of intent from enterprise prospects]"
set_font_name: Inter
set_font_size: 16
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)
```

**Steps 25–30 — Bottom-right card: Strongest quote**
```
create_rectangle: x=634, y=369, w=530, h=190, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

create_text: x=658, y=389, text="FOUNDER QUOTE"  [H2 styles]

create_text: x=658, y=417, w=476, text='"[Strongest quote from an interview]"'
set_font_name: Inter
set_font_size: 16
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)
(italic if MCP supports it)

create_text: x=658, y=527, text="— [Role], [Company type]"
set_font_name: Inter
set_font_size: 13
set_font_weight: 400
set_fill_color: r=100, g=116, b=139  (text_muted)
```

**Step 31 — Gate status strip background**
```
create_rectangle: x=80, y=590, w=1120, h=48, corner_radius=8
set_fill_color: r=30, g=41, b=59  (bg_card)
```

**Step 32 — Gate status text**
```
create_text: x=104, y=606,
  text="Stage 0 ✓   Stage 1 ✓   Stage 2 ✓   Stage 3 ✓   Stage 4 ✓"
  (replace ✓ with ○ for stages not yet completed)
set_font_name: Inter
set_font_size: 14
set_font_weight: 500
set_fill_color: r=16, g=185, b=129  (accent_emerald for ✓) / r=100, g=116, b=139 (text_muted for ○)
```

---

## SLIDE 9 — Team

**Purpose:** Build trust in the founders. Show relevant expertise and "why us."
**Data source:** `stage-0/idea-framing.md`
**Y position on canvas:** 6560

### Layout overview
Up to 3 founder cards in a horizontal row.
Open roles note below.
Advisor row at bottom if space.

### Card sizing by founder count
- 1 founder: w=700, centered (x=290)
- 2 founders: w=520 each, x=80 and x=624
- 3 founders: w=340 each, x=80, x=444, x=808

### MCP tool call sequence

**Steps 1–4:** Standard recurring elements. Slide number: "09 / 10"

**Step 5 — Section label**
```
create_text: x=80, y=60, text="THE TEAM"
[H2 styles]
```

**Step 6 — Title**
```
create_text: x=80, y=88, w=900, text="The Team."
[H1 styles]
```

**Steps 7–18 — Founder card (repeat per founder)**

Founder Card 1 (adjust x based on count, y=155, h=320):
```
// Card background
create_rectangle: x=[X], y=155, w=[W], h=320, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

// Photo placeholder circle
create_ellipse: x=[X+24], y=179, w=64, h=64
set_fill_color: r=99, g=102, b=241  (accent_blue)

// Name
create_text: x=[X+24], y=259, text="[Founder Name]"
set_font_name: Inter
set_font_size: 24
set_font_weight: 700
set_fill_color: r=248, g=250, b=252  (text_primary)

// Role
create_text: x=[X+24], y=291, text="[Role, e.g. CEO & Co-founder]"
set_font_name: Inter
set_font_size: 16
set_font_weight: 500
set_fill_color: r=99, g=102, b=241  (accent_blue)

// Background (2-3 lines)
create_text: x=[X+24], y=321, w=[W-48], text="[Relevant background, prior experience]"
set_font_name: Inter
set_font_size: 15
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)

// "Why me" line
create_text: x=[X+24], y=421, w=[W-48], text="[Why you/why now — 1 line]"
set_font_name: Inter
set_font_size: 13
set_font_weight: 400
set_fill_color: r=100, g=116, b=139  (text_muted)
(italic if MCP supports it)
```

**Step 19 — Open roles note (if applicable)**
```
create_text: x=80, y=502, w=1120,
  text="Actively hiring: [Role 1], [Role 2]"
set_font_name: Inter
set_font_size: 16
set_font_weight: 400
set_fill_color: r=100, g=116, b=139  (text_muted)
(italic if MCP supports it)
```

**Step 20 — Advisors row (if applicable, at y=540)**
```
create_text: x=80, y=540, w=1120,
  text="Advisors: [Name] ([credential])  ·  [Name] ([credential])  ·  [Name] ([credential])"
set_font_name: Inter
set_font_size: 14
set_font_weight: 400
set_fill_color: r=100, g=116, b=139  (text_muted)
```

---

## SLIDE 10 — The Ask

**Purpose:** The close. Funding amount, use of funds, milestone.
**Data source:** `stage-0/idea-framing.md` or ask founder directly.
**Y position on canvas:** 7380

### Layout overview
Left side: large funding amount, round label, three use-of-funds items.
Right side: milestone card.
Footer: contact / thank you.

### MCP tool call sequence

**Steps 1–4:** Standard recurring elements. Slide number: "10 / 10"

**Step 5 — Section label**
```
create_text: x=80, y=60, text="THE ASK"
[H2 styles]
```

**Step 6 — Title**
```
create_text: x=80, y=88, w=600, text="The Ask."
[H1 styles]
```

**Step 7 — Funding amount (Display)**
```
create_text: x=80, y=155, text="[€/$][X]M"
set_font_name: Inter
set_font_size: 72
set_font_weight: 700
set_fill_color: r=99, g=102, b=241  (accent_blue)
```

**Step 8 — Round label**
```
create_text: x=80, y=250, text="[ROUND STAGE, e.g. SEED ROUND]"
set_font_name: Inter
set_font_size: 13
set_font_weight: 600
set_fill_color: r=148, g=163, b=184  (text_secondary)
(uppercase, letter-spacing 3px)
```

**Steps 9–21 — Use-of-funds items (3 items, stacked, starting y=300)**

Use-of-funds item 1 (y=300):
```
// Bullet rectangle
create_rectangle: x=80, y=310, w=8, h=8
set_fill_color: r=99, g=102, b=241  (accent_blue)

// Allocation text
create_text: x=100, y=300, w=500, text="[Allocation 1, e.g. Product development]"
set_font_name: Inter
set_font_size: 20
set_font_weight: 600
set_fill_color: r=248, g=250, b=252  (text_primary)

// Percentage (right-aligned in left column)
create_text: x=500, y=300, w=100, text="[X]%"
set_font_name: Inter
set_font_size: 20
set_font_weight: 700
set_fill_color: r=99, g=102, b=241  (accent_blue)
set_text_align: right
```

Use-of-funds item 2: y=348. Use-of-funds item 3: y=396.

**Steps 22–30 — Milestone card (right side)**
```
// Card background
create_rectangle: x=700, y=155, w=500, h=340, corner_radius=12
set_fill_color: r=30, g=41, b=59  (bg_card)

// Card label
create_text: x=724, y=179, text="12-MONTH MILESTONE"
[H2 styles: 13px, SemiBold, accent_blue, uppercase]

// Milestone headline
create_text: x=724, y=207, w=452, text="[Key milestone statement, e.g. 'Reach $1M ARR with 20 paying customers']"
set_font_name: Inter
set_font_size: 22
set_font_weight: 600
set_fill_color: r=248, g=250, b=252  (text_primary)

// What it unlocks
create_text: x=724, y=310, w=452, text="[What this milestone unlocks — e.g. 'Qualifies for Series A raise at proven PMF']"
set_font_name: Inter
set_font_size: 16
set_font_weight: 400
set_fill_color: r=148, g=163, b=184  (text_secondary)

// Accent bar at bottom of card
create_rectangle: x=700, y=471, w=500, h=3, corner_radius=0
set_fill_color: r=99, g=102, b=241  (accent_blue)
```

**Step 31 — Footer contact / thank you**
```
create_text: x=80, y=658,
  text="[Founder Name]  ·  [email]  ·  [website]   —   Thank you."
set_font_name: Inter
set_font_size: 14
set_font_weight: 400
set_fill_color: r=100, g=116, b=139  (text_muted)
```
