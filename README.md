# CAC Analysis — 2024

**Student verification email:** 23f2001288@ds.study.iitm.ac.in

## Summary
This repository contains a short analysis of Customer Acquisition Cost (CAC) for 2024. The average CAC computed from quarterly data is **230.42**, compared to an industry target of **150**.

## Data
File: `cac_2024.csv`

```
Quarter,CAC
Q1,229.69
Q2,228.38
Q3,229.54
Q4,234.07
```

**Average CAC (2024):** 230.42

## Analysis & Visuals
- `cac_analysis.py` — Python script that:
  - Loads `cac_2024.csv`
  - Computes average, min, max CAC
  - Produces charts: `cac_trend_2024.png`, `cac_vs_target_2024.png`
- Charts are saved to the repository when you run the script locally.

## Findings (short)
- Average CAC for 2024 = **230.42**, well above industry target (150).
- All quarters exceed the target; Q4 is the worst (234.07).
- Immediate risk: poor unit economics; recommendation is to **optimize digital marketing channels** (channel-level decomposition, CRO, better attribution, reallocate budget).

## LLM / Codex Evidence (verification)
This PR and supporting code were generated / assisted using Jules (ChatGPT Codex).  
Task executed via: https://chatgpt.com/codex/tasks

Verification email: 23f2001288@ds.study.iitm.ac.in

## How to reproduce
```bash
pip install pandas matplotlib
python cac_analysis.py
```

## Files in this PR
- cac_2024.csv
- cac_analysis.py
- README.md
- (generated images) cac_trend_2024.png, cac_vs_target_2024.png
- (generated images) cac_trend_2024.png, cac_vs_target_2024.png
- (generated images) cac_trend_2024.png, cac_vs_target_2024.png
