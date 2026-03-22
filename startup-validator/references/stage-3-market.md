# Stage 3: Market Validation Reference

---

## TAM/SAM/SOM Triangulation Method

Always use three methods and triangulate. If divergence >30%, revise inputs before proceeding.

### Method 1: Bottom-Up (PRIMARY — most credible to investors)

**B2C:**
```
TAM = Total population in target geography
    × % in target demographic segment
    × % who have the problem
    × ARPU (annual revenue per user)

SAM = TAM
    × % reachable through planned channels
    × % who are willing to pay (not just use for free)

SOM = SAM × realistic Y1 adoption rate (1-3%)
```

**B2B:**
```
TAM = Total companies in target industries (by NAICS, company size)
    × Average Contract Value (ACV)

SAM = TAM
    × % with the specific problem your product solves
    × % with budget for this category

SOM = Realistic customer count Y1 (5-10 enterprise; 50-200 SMB) × ACV
```

### Method 2: Top-Down (cross-check)

Find an industry report total → segment by relevance → your TAM is a slice.

Example:
- Global HR software market: $24B
- SMB segment: ~20% → $4.8B
- US only: ~40% → $1.9B → this is your TAM

Source hierarchy (credibility): Gartner/Forrester > IBISWorld > Statista > blog posts

### Method 3: Value Theory (sanity check)

What value does the product create? Price as a fraction of that value.

```
Value-based TAM = Target user count × (annual value created per user × pricing capture rate)

Example:
HR tool saves each company 20 hours/month at €50/hr = €12,000/year value created
If priced at 10% of value = €1,200/year ACV
200,000 target companies × €1,200 = €240M TAM
```

### Triangulation Table

| Method | Result | Confidence |
|--------|--------|-----------|
| Bottom-up | €[X] | High |
| Top-down | €[X] | Medium |
| Value-theory | €[X] | Low |
| **Divergence** | **[%]** | <15%: good; 15-30%: investigate; >30%: revise |

---

## Data Sources for Market Sizing

**Using market_data.py:**

```bash
# B2C: Consumer demographics
python market_data.py --source census --api-key YOUR_KEY
python market_data.py --source fred --series PCE --api-key YOUR_KEY

# B2B: Business establishment counts by NAICS
python market_data.py --source census --naics 54 --api-key YOUR_KEY  # Professional services
python market_data.py --source bls --series CES0500000001  # Employment by sector

# International context
python market_data.py --source worldbank --indicator NY.GDP.MKTP.CD --country DE
```

**Common NAICS codes:**
| Code | Sector |
|------|--------|
| 51 | Information technology |
| 52 | Finance and insurance |
| 54 | Professional, scientific, technical services |
| 56 | Administrative and support services |
| 62 | Healthcare and social assistance |
| 72 | Accommodation and food services |
| 44-45 | Retail trade |

---

## Competitive Matrix Construction

### B2C axes (pick the two that best reveal market gaps):

- **Price vs. User experience quality**
- **Simplicity vs. Feature depth**
- **Niche targeting vs. Mass market**
- **Self-service vs. Guided/coached**

### B2B axes (pick the two that best reveal market gaps):

- **Price vs. Feature completeness**
- **Ease of implementation vs. Customizability**
- **SMB-focused vs. Enterprise-focused**
- **Point solution vs. Platform play**

### Matrix format:

```
              │ Low [Axis 2]         │ High [Axis 2]
──────────────┼──────────────────────┼──────────────────────
High [Axis 1] │ [Quadrant A]         │ [Quadrant B]
              │ Competitor A, B      │ Competitor C
──────────────┼──────────────────────┼──────────────────────
Low [Axis 1]  │ [Quadrant C]         │ [Quadrant D] ← OUR SPACE
              │ Competitor D         │ [White space]
```

Identify the quadrant where your product sits. Is it a genuinely unoccupied space, or are you in a crowded quadrant?

---

## "Why Now" Analysis Framework

### Five categories of "Why Now" factors:

**1. Regulatory / policy change**
- New law creates compliance requirement → forces adoption
- Enforcement action → incumbent players face restrictions
- Standard changes → existing solutions become non-compliant

**2. Technology maturity threshold**
- Cost of key technology drops below viability threshold (compute, sensors, bandwidth)
- New API / platform enables previously impossible integration
- AI capability reaches the required performance level

**3. Behavioral / cultural shift**
- COVID aftermath, remote work normalization
- Gen Z entering workforce with different expectations
- Consumer behavior change creates new habit or abandons old one

**4. Market structure change**
- Incumbent acquired → customers stranded without support or roadmap
- Consolidation creates underserved niche
- Platform shift → existing solutions become obsolete

**5. Economic pressure**
- Companies forced to cut costs → automation becomes ROI-positive
- Labor shortage → automation becomes necessity
- Inflation → price sensitivity changes purchasing behavior

### Using trend_analysis.py for "Why Now":

```bash
python trend_analysis.py \
  --keywords "[keyword1],[keyword2]" \
  --timeframe "today 5-y" \
  --news-key YOUR_KEY \
  --news-query "[space] market 2025"
```

- Rising trend + inflection point in last 12 months = strong "Why Now"
- Declining trend = timing may be wrong
- Spike + plateau = post-hype, be careful

---

## Porter's Five Forces Template

Generate this for Stage 3 to assess industry attractiveness:

**1. Threat of new entrants** [Low / Medium / High]
- Barriers: [capital requirements, regulation, network effects, brand, switching costs]
- Assessment: [...]

**2. Bargaining power of suppliers** [Low / Medium / High]
- Key suppliers: [cloud, data, talent, APIs]
- Assessment: [...]

**3. Bargaining power of buyers** [Low / Medium / High]
- Buyer concentration: [many small / few large]
- Switching cost: [high / low]
- Assessment: [...]

**4. Threat of substitutes** [Low / Medium / High]
- Substitutes: [what else solves the problem]
- Assessment: [...]

**5. Competitive rivalry** [Low / Medium / High]
- Number of players, market growth rate, differentiation
- Assessment: [...]

**Overall industry attractiveness:** [High / Medium / Low]
- Most favorable forces: [...]
- Key risks: [...]
