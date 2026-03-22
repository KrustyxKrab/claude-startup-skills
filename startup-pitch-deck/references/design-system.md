# Design System — startup-pitch-deck

Follow every value in this file exactly. Do not improvise colors, sizes, or positions.

---

## Canvas

- Slide size: **1280 × 720 px** (16:9)
- Slides stacked vertically with 100px gap between them
- All slides at x=0

### Y positions for `create_frame`

| Slide | Y position |
|-------|-----------|
| Slide 1 — Cover | y=0 |
| Slide 2 — Problem | y=820 |
| Slide 3 — Solution | y=1640 |
| Slide 4 — Why Now | y=2460 |
| Slide 5 — Market | y=3280 |
| Slide 6 — Product | y=4100 |
| Slide 7 — Business Model | y=4920 |
| Slide 8 — Traction | y=5740 |
| Slide 9 — Team | y=6560 |
| Slide 10 — The Ask | y=7380 |

All frames: width=1280, height=720.

---

## Colors (RGB values for MCP set_fill_color calls)

| Token | R | G | B | Hex | Usage |
|-------|---|---|---|-----|-------|
| `bg_dark` | 15 | 23 | 42 | #0F172A | Slide background (deep navy) |
| `bg_card` | 30 | 41 | 59 | #1E293B | Card backgrounds (slate) |
| `bg_card_light` | 51 | 65 | 85 | #334155 | Divider lines, lighter cards |
| `accent_blue` | 99 | 102 | 241 | #6366F1 | Primary accent (indigo) |
| `accent_emerald` | 16 | 185 | 129 | #10B981 | Positive metrics, SAM card |
| `accent_amber` | 245 | 158 | 11 | #F59E0B | Warnings, highlights, SOM card, high-severity dots |
| `text_primary` | 248 | 250 | 252 | #F8FAFC | Headings, key content (near white) |
| `text_secondary` | 148 | 163 | 184 | #94A3B8 | Body text, descriptions (slate 400) |
| `text_muted` | 100 | 116 | 139 | #64748B | Captions, slide numbers (slate 500) |
| `white` | 255 | 255 | 255 | #FFFFFF | — |

---

## Typography

Font family: **"Inter"** for all text. Fallback: **"SF Pro Display"**.

| Role | Size | Weight | Color token | Notes |
|------|------|--------|-------------|-------|
| Display (cover name) | 72px | Bold (700) | `text_primary` | Cover slide only |
| H1 (slide title) | 48px | Bold (700) | `text_primary` | — |
| H2 (section label) | 13px | SemiBold (600) | `accent_blue` | UPPERCASE, letter-spacing 3px |
| H3 (card header) | 28px | SemiBold (600) | `text_primary` | — |
| Body | 20px | Regular (400) | `text_secondary` | Standard body copy |
| Body strong | 20px | SemiBold (600) | `text_primary` | Emphasized body |
| Metric large | 56px | Bold (700) | `accent_blue` | TAM/SAM/SOM values, big numbers |
| Metric label | 14px | Medium (500) | `text_secondary` | Below metric large |
| Bullet | 18px | Regular (400) | `text_secondary` | List items |
| Slide number | 13px | Regular (400) | `text_muted` | Format: "01 / 10" |
| Tag | 12px | Medium (500) | `accent_blue` | Badge text on bg_card |
| Caption / tiny | 12px | Regular (400) | `text_muted` | Confidential line, footnotes |

---

## Layout constants

| Constant | Value |
|----------|-------|
| Horizontal margin | 80px from left and right edges |
| Content area width | 1120px (1280 − 80 − 80) |
| Title block top | 60px from slide top |
| Slide label (H2) top | 60px |
| Title (H1) top | 88px |
| Content top margin | 140px (below title block) |
| Bottom margin | 60px from slide bottom |

---

## Recurring elements on every slide (slides 2–10)

These four elements appear on every slide except Slide 1 (Cover). Build them first, before any slide-specific content.

### 1. Full-bleed background
- `create_rectangle`: x=0, y=0, w=1280, h=720
- Fill: `bg_dark` (r=15, g=23, b=42)

### 2. Accent left bar
- `create_rectangle`: x=0, y=180, w=4, h=360
- Fill: `accent_blue` (r=99, g=102, b=241)

### 3. Top divider line
- `create_rectangle`: x=80, y=130, w=1120, h=1
- Fill: `bg_card_light` (r=51, g=65, b=85)

### 4. Slide number
- `create_text`: x=1180, y=32, text="0N / 10" (e.g., "02 / 10")
- Font: Inter, 13px, Regular, `text_muted` (r=100, g=116, b=139)
- Align: right

---

## Card component

Use this pattern for all metric and content cards:

| Property | Value |
|----------|-------|
| Shape | `create_rectangle` |
| corner_radius | 12 |
| Fill | `bg_card` (r=30, g=41, b=59) |
| Inner padding | 24px all sides |

Card text layers (position relative to card top-left):

| Layer | Offset | Style |
|-------|--------|-------|
| Label (H2) | x+24, y+24 | 13px, SemiBold, UPPERCASE, `accent_blue` |
| Value (Metric large) | x+24, y+52 | 56px, Bold, `accent_blue` (or `accent_emerald` for SAM) |
| Sub-label (Metric label) | x+24, y+120 | 14px, Medium, `text_secondary` |

For cards without a large metric (content cards), use H3 (28px SemiBold) as the value instead.

---

## Cover slide exceptions

Slide 1 (Cover) does NOT include:
- Accent left bar
- Top divider line
- Slide number

Cover uses a decorative accent ellipse instead (see slide-templates.md).
