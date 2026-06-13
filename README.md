# SEO Analytics Automation Engine

Generate a complete SEO performance report from any Google Search Console comparison export — in seconds, from the terminal.

---

## Requirements

- Python 3.8 or higher
- Windows / Mac / Linux

---

## Installation

**Step 1 — Open terminal and go to this folder:**

```
cd path/to/seo-analytics-engine
```

**Step 2 — Install dependencies:**

```
pip install -r requirements.txt
```

That's it. No API keys, no login, works fully offline.

---

## How to Run

### Standard Analysis (most common)

```
python -m seo_analysis --input "path\to\your\gsc_export.xlsx" --output "path\to\report.xlsx"
```

**With client name in the report header:**

```
python -m seo_analysis --input "gsc_export.xlsx" --output "report.xlsx" --client "example.com"
```

### Algorithm Update Detection

Use this when Google announces a core update and you want to measure impact:

```
python -m seo_analysis --input "gsc_export.xlsx" --output "algo_report.xlsx" --mode algo_update --update-date "2025-05-10" --client "example.com"
```

---

## Input File

Export from Google Search Console with **Compare mode on** — any two date ranges work.

The tool reads all 6 tabs automatically:
- Queries
- Pages
- Countries
- Devices
- Search appearance
- Filters (for date labels)

No manual setup needed — just export from GSC and pass the file.

---

## Output Report

The tool generates a formatted Excel workbook with these sheets:

| Sheet | What's in it |
|---|---|
| `Summary_Dashboard` | KPIs, win rate, avg position, portfolio health score |
| `Queries_Analysis` | All keywords with changes, sorted by impact |
| `Pages_Analysis` | URL-level performance |
| `Countries_Analysis` | Geographic breakdown |
| `Devices_Analysis` | Mobile vs Desktop vs Tablet |
| `Search_Appearance_Analysis` | Rich result types (dynamic per client) |
| `Algorithm_Impact` | Only when using `--mode algo_update` |

---

## All Arguments

| Argument | Required | Example | Description |
|---|---|---|---|
| `--input` | Yes | `data.xlsx` | Path to your GSC export |
| `--output` | Yes | `report.xlsx` | Where to save the report |
| `--client` | No | `example.com` | Client name shown in report header |
| `--mode` | No | `algo_update` | `standard` (default) or `algo_update` |
| `--update-date` | Only for algo mode | `2025-05-10` | Date of the algorithm update |

---

## Real Examples

**Monthly SEO report:**
```
python -m seo_analysis --input "gsc_export.xlsx" --output "seo_report.xlsx" --client "my-client"
```

**Algorithm impact after core update:**
```
python -m seo_analysis --input "gsc_export.xlsx" --output "algo_impact.xlsx" --mode algo_update --update-date "2026-05-10" --client "my-client"
```

---

## Run Tests

```
pip install pytest
pytest tests/ -v
```

---

## Troubleshooting

**"Module not found" error:**
Make sure you're inside the `seo-analytics-engine` folder when running the command.

**"Input file not found":**
Use the full path to your file instead of just the filename: `"~/Downloads/gsc_export.xlsx"`

**Empty sheets in the report:**
The GSC export sheet names must match exactly: `Queries`, `Pages`, `Countries`, `Devices`, `Search appearance`. If a sheet is missing, that tab will be skipped with a warning.
