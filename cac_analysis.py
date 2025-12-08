"""
Financial Services CAC Analysis - 2024

This script:
1. Loads quarterly CAC data from cac_2024.csv
2. Computes key statistics including the average CAC
3. Compares CAC with an industry benchmark target
4. Creates visualizations:
   - Line chart of CAC by quarter
   - Bar chart showing each quarter vs target
5. Saves charts as PNG files for use in README.md

Student email (for verification):
23f2001288@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# Configuration
# -----------------------------
DATA_PATH = Path("cac_2024.csv")
INDUSTRY_TARGET = 150
OUTPUT_TREND_FIG = Path("cac_trend_2024.png")
OUTPUT_COMPARISON_FIG = Path("cac_vs_target_2024.png")


def main():
    # 1. Load data
    df = pd.read_csv(DATA_PATH)

    # Ensure proper ordering of quarters
    quarter_order = ["Q1", "Q2", "Q3", "Q4"]
    df["Quarter"] = pd.Categorical(df["Quarter"], categories=quarter_order, ordered=True)
    df = df.sort_values("Quarter")

    # 2. Compute summary stats
    avg_cac = df["CAC"].mean()
    max_cac = df["CAC"].max()
    min_cac = df["CAC"].min()

    print("=== Customer Acquisition Cost (CAC) - 2024 Summary ===")
    print(df)
    print(f"\nAverage CAC (2024): {avg_cac:.2f}")
    print(f"Minimum CAC: {min_cac:.2f}")
    print(f"Maximum CAC: {max_cac:.2f}")
    print(f"Industry Target CAC: {INDUSTRY_TARGET:.2f}")
    print(f"Gap to target: {avg_cac - INDUSTRY_TARGET:.2f}")
    print(f"Gap to target: {avg_cac - INDUSTRY_TARGET:.2f}")

    # 3. Line chart – CAC trend by quarter
    plt.figure(figsize=(8, 5))
    plt.plot(df["Quarter"], df["CAC"], marker="o")
    plt.axhline(INDUSTRY_TARGET, linestyle="--", label=f"Industry target ({INDUSTRY_TARGET})")

    plt.title("Customer Acquisition Cost (CAC) – 2024 Quarterly Trend")
    plt.xlabel("Quarter")
    plt.ylabel("CAC")
    plt.legend()
    plt.grid(True, axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(OUTPUT_TREND_FIG, dpi=150)
    plt.close()

    # 4. Bar chart – each quarter vs target
    plt.figure(figsize=(8, 5))
    plt.bar(df["Quarter"], df["CAC"])
    plt.axhline(INDUSTRY_TARGET, linestyle="--", label=f"Industry target ({INDUSTRY_TARGET})")

    plt.title("CAC vs Industry Target by Quarter – 2024")
    plt.xlabel("Quarter")
    plt.ylabel("CAC")
    plt.legend()
    plt.grid(True, axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(OUTPUT_COMPARISON_FIG, dpi=150)
    plt.close()

    print(f"\nSaved figures:")
    print(f" - {OUTPUT_TREND_FIG}")
    print(f" - {OUTPUT_COMPARISON_FIG}")


if __name__ == "__main__":
    main()
