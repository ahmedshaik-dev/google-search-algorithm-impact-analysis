# SEO Analytics Engine — Complete Guide

Professional SEO performance analysis tool that transforms Google Search Console exports into comprehensive Excel reports in seconds.

---

## What It Does

### Automated Data Processing
- **Imports** Google Search Console (GSC) comparison exports
- **Analyzes** performance metrics across 6 data dimensions
- **Generates** formatted, multi-sheet Excel reports with visualizations
- **Exports** ready-to-present client reports

### Key Capabilities

#### 1. **Comprehensive Keyword Analysis**
- Compare keyword performance across two date ranges
- Track changes in clicks, impressions, CTR, and position
- Identify winners (gained impressions) and losers (lost visibility)
- Sort keywords by impact score (business value)
- Calculate trend direction: IMPROVED, DECLINED, FLAT, GAINED, LOST

#### 2. **URL Performance Tracking**
- Analyze page-level metrics
- Track which pages are winning/losing
- Identify underperforming content
- Monitor position changes by page

#### 3. **Geographic Breakdown**
- Performance by country/region
- Identify geographic trends
- Market-specific insights
- Regional opportunity identification

#### 4. **Device Analysis**
- Compare Mobile vs Desktop vs Tablet performance
- Mobile-first ranking signals
- Device-specific optimization opportunities
- Identify platform-specific issues

#### 5. **Rich Results & Search Appearance**
- Track featured snippets, rich results, AMP
- Monitor SERP feature performance
- Identify search appearance opportunities
- Measure featured snippet gains/losses

#### 6. **Algorithm Update Detection**
- Measure impact of Google core updates
- Compare metrics before/after update date
- Quantify traffic loss/gain from algorithm changes
- Create algorithm impact reports
- Track recovery post-update

#### 7. **Smart Metrics**
Built-in calculations:
- **Impact Score** — prioritizes keywords by business value (clicks × position change)
- **CTR Trends** — click-through rate changes
- **Position Change** — ranking movement
- **Impression Trends** — visibility changes
- **Win Rate** — percentage of improved vs declined keywords

#### 8. **Professional Reporting**
- Multi-sheet Excel workbooks
- Formatted headers and styling
- Color-coded categories (green = gained, red = lost, yellow = stable)
- Client-ready formatting
- Summary dashboards
- Sortable data tables

---

## What You Can Achieve

### For SEO Specialists
✓ Monthly/quarterly performance reports
✓ Algorithm update impact analysis
✓ Competitive benchmarking (by country/device)
✓ Content gap identification
✓ Quick client presentations
✓ Automated reporting pipeline

### For Agencies
✓ Client deliverables in seconds
✓ Consistent report formatting
✓ White-label ready
✓ Batch processing multiple accounts
✓ Historical comparison tracking

### For Marketing Teams
✓ Stakeholder-ready dashboards
✓ Executive summaries
✓ Search performance metrics
✓ Trend analysis
✓ Data-driven decisions

### For Content Teams
✓ Identify underperforming pages
✓ Find content improvement opportunities
✓ Track content updates' impact
✓ Discover emerging keywords
✓ Measure organic search ROI

---

## How It Works

### Input
```
Google Search Console Export (.xlsx)
├── Queries Tab        (keywords + metrics)
├── Pages Tab          (URLs + metrics)
├── Countries Tab      (geographic breakdown)
├── Devices Tab        (mobile/desktop/tablet)
├── Search Appearance  (rich results data)
└── Filters Tab        (date range labels)
```

### Processing
```
1. Read all 6 tabs from GSC export
2. Parse dynamic column headers (dates vary per export)
3. Calculate impact scores and metrics
4. Classify keywords (GAINED/LOST/IMPROVED/DECLINED/FLAT)
5. Detect algorithm impacts (optional)
6. Generate formatted output sheets
7. Apply professional styling & colors
```

### Output
```
Multi-sheet Excel Report (.xlsx)
├── Summary_Dashboard          (KPIs & health score)
├── Queries_Analysis           (keywords with changes)
├── Pages_Analysis             (URL performance)
├── Countries_Analysis         (geographic data)
├── Devices_Analysis           (mobile/desktop breakdown)
├── Search_Appearance_Analysis (rich results data)
└── Algorithm_Impact           (optional, if --mode algo_update)
```

---

## Use Cases

### Monthly Client Reports
```bash
python -m seo_analysis \
  --input "client_gsc_export.xlsx" \
  --output "client_report_may_2026.xlsx" \
  --client "your-client-name"
```
**Delivers:** Executive summary + 6 detailed analysis sheets

### Competitive Algorithm Impact Analysis
```bash
python -m seo_analysis \
  --input "gsc_export.xlsx" \
  --output "algo_impact_march_2026.xlsx" \
  --mode algo_update \
  --update-date "2026-03-15"
```
**Delivers:** Algorithm impact quantification + recovery tracking

### Multi-Market Performance Review
```bash
python -m seo_analysis \
  --input "global_gsc_export.xlsx" \
  --output "market_analysis.xlsx" \
  --client "multi-country-site"
```
**Delivers:** Country-level performance breakdown

### Quarterly SEO Health Check
```bash
python -m seo_analysis \
  --input "q2_comparison.xlsx" \
  --output "seo_health_q2_2026.xlsx"
```
**Delivers:** Comprehensive performance dashboard

---

## Output Report Sheets Explained

### Summary_Dashboard
- **Portfolio Health Score** — 0-100 overall performance metric
- **Key Performance Indicators:**
  - Total clicks & impressions
  - Average CTR & position
  - Keyword gains/losses
  - Win rate (% improved)
- **Trending data** — visualizes performance direction
- **Client info** — header with date ranges

### Queries_Analysis
- **All keywords** from GSC export
- **Columns:**
  - Keyword (search term)
  - Clicks (before & after)
  - Impressions (before & after)
  - CTR changes
  - Position changes
  - Category (GAINED/LOST/IMPROVED/DECLINED/FLAT)
  - Impact Score (business value ranking)
- **Sorted by Impact Score** — highest value opportunities first
- **Color-coded** — green for wins, red for losses, yellow for stable

### Pages_Analysis
- **URL performance** breakdown
- Shows which pages are winning/losing
- Tracks traffic distribution
- Identifies top performers

### Countries_Analysis
- **Geographic performance** metrics
- Country-level comparisons
- Identify strong/weak markets
- Regional opportunity gaps

### Devices_Analysis
- **Mobile vs Desktop vs Tablet** comparison
- Device-specific trends
- Mobile-first ranking signals
- Platform-specific optimizations

### Search_Appearance_Analysis
- **Rich result types** (featured snippets, rich results, AMP, etc.)
- Track which search appearances are performing
- Identify missing opportunities
- Monitor featured snippet rankings

### Algorithm_Impact (Optional)
- **Only generated with `--mode algo_update`**
- Compares metrics before/after update date
- Quantifies traffic impact
- Shows recovery rate
- Identifies winners/losers in algorithm shift

---

## Key Features

| Feature | Benefit |
|---------|---------|
| **Zero Setup** | No API keys, no login, works offline |
| **Fast Processing** | Generates reports in seconds |
| **Accurate Analysis** | Handles dynamic GSC export formats |
| **Professional Output** | Excel formatting + color coding |
| **Flexible Input** | Works with any date range comparison |
| **Algorithm Tracking** | Measure core update impacts |
| **Client-Ready** | White-label ready reports |
| **Batch Processing** | Process multiple exports |
| **Impact Scoring** | AI-weighted keyword prioritization |
| **Trend Detection** | Automatic winner/loser classification |

---

## Installation & Setup

### Requirements
- Python 3.8+
- pip (Python package manager)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Export from Google Search Console
1. Go to Google Search Console
2. Select your property
3. Go to **Performance** → **Comparison mode**
4. Select two date ranges (e.g., This Month vs Last Month)
5. Click **Export** → Download as .xlsx

### Step 3: Run Analysis
```bash
python -m seo_analysis \
  --input "your_gsc_export.xlsx" \
  --output "report.xlsx" \
  --client "your-site-name"
```

Report is ready in seconds!

---

## Command Reference

### Basic Report
```bash
python -m seo_analysis --input "data.xlsx" --output "report.xlsx"
```

### With Client Name
```bash
python -m seo_analysis \
  --input "gsc_export.xlsx" \
  --output "report.xlsx" \
  --client "client-name"
```

### Algorithm Update Analysis
```bash
python -m seo_analysis \
  --input "gsc_export.xlsx" \
  --output "algo_report.xlsx" \
  --mode algo_update \
  --update-date "2026-05-10"
```

### All Arguments
| Argument | Required | Example | Purpose |
|----------|----------|---------|---------|
| `--input` | Yes | `data.xlsx` | GSC export file path |
| `--output` | Yes | `report.xlsx` | Output report file path |
| `--client` | No | `my-site` | Client name in report |
| `--mode` | No | `algo_update` | `standard` or `algo_update` |
| `--update-date` | Only for algo mode | `2026-05-10` | Algorithm update date |

---

## Real-World Examples

### Monthly Agency Report
```bash
python -m seo_analysis \
  --input "~/Downloads/may_gsc.xlsx" \
  --output "~/Desktop/may_report_client.xlsx" \
  --client "aha.video"
```
**Result:** Professional May performance report delivered to client

### Measure March 2026 Core Update Impact
```bash
python -m seo_analysis \
  --input "gsc_export.xlsx" \
  --output "march_core_update_impact.xlsx" \
  --mode algo_update \
  --update-date "2026-03-12"
```
**Result:** Quantified traffic impact from core update

### Quarterly Performance Review
```bash
python -m seo_analysis \
  --input "q2_comparison.xlsx" \
  --output "q2_2026_seo_summary.xlsx" \
  --client "company-name"
```
**Result:** Comprehensive quarterly dashboard with trends

---

## Troubleshooting

**"Module not found" error**
- Make sure you're in the `seo-analytics-engine` folder
- Run: `cd seo-analytics-engine`

**"Input file not found"**
- Use full path: `~/Downloads/gsc_export.xlsx`
- Not just: `gsc_export.xlsx`

**Empty sheets in report**
- GSC sheet names must match exactly: `Queries`, `Pages`, `Countries`, `Devices`, `Search appearance`
- If a sheet is missing, that analysis will be skipped with a warning

**Algorithm Impact sheet missing**
- Only generated when using `--mode algo_update`
- Must also provide `--update-date`

---

## Testing

Run the test suite:
```bash
pytest tests/ -v
```

This validates:
- Data reading and parsing
- Metric calculations
- Keyword classification
- Excel output generation
- Algorithm detection logic

---

## What Makes This Different

### vs Manual Analysis
- ✓ Seconds instead of hours
- ✓ Consistent formatting
- ✓ No copy/paste errors
- ✓ Automatic impact scoring

### vs Google Sheets
- ✓ Offline processing
- ✓ No API quotas
- ✓ Custom metrics
- ✓ Professional formatting

### vs Other Tools
- ✓ Free (no subscription)
- ✓ No API keys needed
- ✓ Works locally
- ✓ Full source code available

---

## Tech Stack

- **Language:** Python 3.8+
- **Data Processing:** Pandas, NumPy
- **Excel Export:** openpyxl
- **Testing:** pytest
- **No external dependencies:** Works fully offline

---

## License

MIT — Free to use, modify, and distribute

---

## Quick Start (60 seconds)

1. **Download your GSC export** (Performance → Comparison mode)
2. **Run:** `python -m seo_analysis --input "export.xlsx" --output "report.xlsx"`
3. **Open report.xlsx** in Excel
4. **Share with stakeholders**

That's it. Instant professional SEO analysis.

---

## Next Steps

- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Export your GSC data (comparison mode)
- [ ] Generate your first report
- [ ] Check the output report
- [ ] Customize for your clients/sites
- [ ] Automate in your workflow

---

**Questions?** Check the README.md for installation details or run `pytest tests/ -v` to validate your setup.
