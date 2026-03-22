# B2B/B2C Routing Reference

Quick lookup tables for routing validation guidance by business model archetype. Load this at Stage 0 and keep active throughout all stages.

---

## Archetype Classification

```
Archetype          │ Definition                               │ Validation profile
───────────────────┼──────────────────────────────────────────┼─────────────────────
B2C Direct         │ Sell to individual consumers              │ Volume game
B2B SMB            │ Sell to small businesses (<50 employees)  │ Hybrid — some B2C patterns
B2B Mid-Market     │ Sell to mid-size companies (50-1000)      │ Classic B2B
B2B Enterprise     │ Sell to large organizations (1000+)       │ Relationship-heavy B2B
Marketplace/       │ Two-sided: serve both businesses           │ Must validate BOTH sides
Platform           │ and consumers, or two consumer groups      │ independently
```

**Detection logic:**
- Individual spending personal money → B2C Direct
- Business paying → ask company size → SMB / Mid-Market / Enterprise
- Connects two groups → Marketplace → validate BOTH sides independently
- Unclear → ask: "Who writes the check?"

**B2B stakeholder types to identify (Miller-Heiman):**
| Stakeholder | Role | What they care about |
|------------|------|---------------------|
| Economic Buyer | Controls budget | ROI, cost reduction, revenue impact |
| End User | Uses product daily | Ease of use, time savings, workflow |
| Technical Buyer | Evaluates feasibility | Security, integrations, compliance |
| Coach/Champion | Internal advocate | Career advancement, looking good |

---

## Stage 1: Problem Validation Routing

| Dimension | B2C | B2B |
|-----------|-----|-----|
| Interview count | 20-30 | 10-15 (must include decision-makers) |
| Interview length | 15-20 min | 30-60 min |
| Finding interviewees | Reddit, panels, social, intercepts | LinkedIn, warm intros, events |
| Success signal | Emotional intensity + workaround behavior | Quantified cost (€/year) + org commitment |
| Commitment currency | Email, pre-order, social share | Meeting with boss, pilot discussion, LOI |
| Kill signal | "That's cool" + no action | "Send me a proposal" + never responds |
| Strongest signal | Pre-order with real money | LOI with budget allocated |

**B2C problem severity matrix:**
```
              │ High frequency       │ Low frequency
──────────────┼──────────────────────┼──────────────────
High emotion  │ UNICORN              │ PREMIUM NICHE
              │ (Uber, Instagram)    │ (Wedding planning)
──────────────┼──────────────────────┼──────────────────
Low emotion   │ VITAMIN              │ DEAD ZONE
              │ (Hard to monetize)   │ (Don't build this)
```

**B2B problem severity matrix:**
```
              │ High revenue impact   │ Low revenue impact
──────────────┼───────────────────────┼───────────────────
Affects many  │ PLATFORM PLAY         │ NICE-TO-HAVE
departments   │ (Salesforce, Slack)   │ (Hard to get budget)
──────────────┼───────────────────────┼───────────────────
Affects one   │ VERTICAL SaaS         │ FEATURE, NOT PRODUCT
department    │ (Veeva, Toast)        │ (Will be built by incumbent)
```

**Proceed criteria:**

B2C:
- 20+ interviews, pattern convergence
- >70% of segment recognizes the problem
- Emotional intensity, workarounds, existing spend
- 5+ commitment signals

B2B:
- 10+ interviews WITH decision-makers or budget holders
- >80% recognize AND quantify the problem
- Cost articulated in €/$/time per year
- 1+ organizational commitment signal
- Problem maps to existing budget line item

---

## Stage 2: Solution Validation Routing

| Experiment | B2C | B2B | Notes |
|-----------|-----|-----|-------|
| Fake Door / Landing Page | ✅ Primary | ⚠️ Limited | B2B buyers don't buy from landing pages |
| Explainer Video | ✅ Viral | ✅ Demo | B2B: show ROI/workflow, not emotional hooks |
| Concierge MVP | ⚠️ Doesn't scale | ✅ Primary | B2B expects white-glove service |
| Wizard of Oz | ✅ | ✅ | Works for both when testing automation |
| Pre-sales / LOI | ⚠️ High-ticket only | ✅ PRIMARY | 3-5 LOIs = strongest B2B signal |
| Crowdfunding | ✅ Excellent | ❌ Rarely | Businesses don't back Kickstarters |
| Pilot program | ❌ | ✅ Essential | 1-3 paid pilots > 100 demo requests |
| Freemium / free trial | ✅ Growth lever | ⚠️ SMB only | Enterprise: use pilots instead |

**B2B Sales Conversation Test** (when no product exists):
1. 20-30 target companies via LinkedIn
2. Cold outreach: problem-first, not product pitch
3. Goal: book 10 discovery calls
4. Present value prop in calls (slides, not product)
5. Ask: "If this existed today, what would next steps look like?"
- Proceed: 10+ calls from 30 outreach; 3+ advance to proposal; 1+ offers to pay
- Kill: <3 calls booked OR all end with "interesting, keep me posted"

**Proceed criteria:**

B2C:
- Fake Door: >5% signup from cold traffic (500+ visitors)
- Or Explainer: >15% CTA click-through
- Or Crowdfunding: funding goal met in first 48h
- Or Pre-orders: 50+ with real payment

B2B:
- 3+ LOIs or signed pilot agreements (SMB: 5+)
- Or 3+ companies willing to pay for pilot
- Or 1 enterprise commits budget + timeline
- >30% of discovery calls advance to proposal
- Champion identified at 1+ target company

---

## Stage 3: Market Validation Routing

| Research Dimension | B2C Focus | B2B Focus |
|-------------------|-----------|-----------|
| Competitors | App stores, Product Hunt, consumer reviews | G2, Capterra, Gartner, analyst reports |
| Market sizing | Population × adoption × ARPU | Company count × ACV × penetration |
| Customer intel | Consumer forums, Reddit, TikTok comments | LinkedIn groups, industry publications |
| Trends | Consumer behavior shifts, social trends | Enterprise tech adoption, regulatory changes |
| Business models | Freemium, subscription, ad-supported | Per-seat SaaS, usage-based, enterprise license |
| Technology | Mobile-first, UX/UI, performance at scale | Integration APIs, SSO/SAML, SOC 2 |
| Regulatory | Consumer protection, GDPR/CCPA | HIPAA, PCI, SOX, industry compliance |

**Competitive matrix axes:**

B2C (pick 2):
- Price vs. Experience quality
- Simplicity vs. Feature depth
- Niche vs. Mass market
- Self-service vs. Guided

B2B (pick 2):
- Price vs. Feature completeness
- Ease of implementation vs. Customizability
- SMB-focused vs. Enterprise-focused
- Point solution vs. Platform

**"Why Now" drivers:**

B2C: Behavioral shifts, technology adoption curves, cultural moments, demographic shifts, platform changes

B2B: Regulatory changes, technology maturity, workforce changes, market consolidation, economic pressure, digital transformation mandates

---

## Stage 4: Business Model Routing

| Metric | B2C | B2B SMB | B2B Mid-Market | B2B Enterprise |
|--------|-----|---------|----------------|----------------|
| Target LTV:CAC | >3:1 | >3:1 | >4:1 | >5:1 |
| CAC payback | <3 months | <6 months | <12 months | <18 months |
| Monthly churn | <5% | <3% | <2% | <1% |
| ACV range | €5-200/yr | €500-5K/yr | €5K-50K/yr | €50K+/yr |
| Sales cycle | Instant-days | 1-4 weeks | 1-3 months | 3-12+ months |
| CAC benchmark | €1-50 | €200-1K | €2K-10K | €10K-50K+ |
| Primary channel | Paid social, SEO, virality | Content, SEO, PLG | Inside sales + content | Field sales + events |
| Pricing model | Freemium, subscription | Per-seat, tiered | Per-seat, usage-based | Enterprise license |

**Unit economics formulas:**

B2C:
```
ARPU = Monthly price × 12
CAC  = Total marketing spend / New customers acquired
LTV  = ARPU / Monthly churn rate
Payback = CAC / (ARPU / 12)
K-factor = Invites sent per user × Conversion rate per invite
```

B2B:
```
ACV     = Annual contract value (weighted average across tiers)
CAC     = (Sales team cost + Marketing spend) / New logos acquired
LTV     = ACV × (1 / Annual churn rate) × Gross margin
Payback = CAC / (ACV × Gross margin / 12)
Expansion = Net revenue retention - 100% (>120% NRR = excellent)
Magic #  = Net new ARR / Sales & Marketing spend (>0.75 = efficient)
```

**Channel budget allocation ($500 test budget):**

B2C:
| Channel | Budget | Measure |
|---------|--------|---------|
| Meta/Instagram | €150 | CPC, CTR, signup conversion |
| Google Ads | €150 | CPC, intent quality, conversion |
| TikTok/Organic | €0 | Views, engagement, profile visits |
| Reddit/Community | €50 | Post engagement, signup conversion |
| Referral program | €50 | K-factor, referral conversion |
| Content/SEO | €100 | Organic traffic trajectory |

B2B:
| Channel | Budget | Measure |
|---------|--------|---------|
| LinkedIn outreach | €0 | Response rate, call booking rate |
| Cold email | €50 | Open, reply, meeting rate |
| Content marketing | €100 | Inbound leads, engagement |
| Industry community | €0 | Discussion engagement, DM requests |
| Partnership/referral | €0 | Warm intro conversion rate |
| LinkedIn Ads | €200 | CPC (expect €5-15), lead quality |
| Webinar/demo event | €150 | Registration, attendance, follow-up |

---

## Kill Criteria Reference

**B2C kill signals:**
- <1% landing page conversion after 3 variants + 500 visitors
- Zero organic sharing / viral coefficient near 0
- >70% churn in first month
- CAC > LTV with no clear path to improvement
- No differentiation from free alternatives

**B2B kill signals:**
- Zero LOIs after approaching 20+ qualified prospects
- All pilot customers churn after free period
- Sales cycle >2x industry average
- Champion leaves and deal dies
- Integration requirements make implementation uneconomical
- Can't articulate ROI in buyer's language
- Product requires team-wide behavior change with no executive mandate

---

## Marketplace / Platform Special Handling

1. Identify supply side and demand side
2. Determine which side is harder to get (usually supply) — validate that side FIRST
3. Then validate the easier side
4. Then validate the matching/transaction mechanism

**Chicken-and-egg strategies to recommend:**
- Single-player mode: build value for one side without the other (OpenTable: reservation book useful without diners)
- Constrain geography: start in one neighborhood/city
- Seed supply: manually onboard supply side
- Fake demand: aggregate existing supply from other platforms

**Marketplace-specific kill signals:**
- Can't get 50 supply-side participants in constrained geography
- Take rate too low to cover CAC for both sides
- Either side has zero switching cost

---

## Hybrid B2B/B2C Handling

If product serves both:

1. Ask: "Is the entry point B2C-first or B2B-first?"
2. **Bottom-up (Slack model):** Validate B2C first → track organic B2B conversion → key metric: viral B2C → B2B rate
3. **Top-down (enterprise):** Validate B2B first → B2C adoption is nice-to-have
4. **Unclear:** Start with B2C (cheaper, faster) → track any organic B2B interest as a signal
