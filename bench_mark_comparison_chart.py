# benchmark_comparison.py

import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
nav = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

benchmark = pd.read_csv(
    "data/processed/10_benchmark_indices_cleaned.csv"
)

perf = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

# Convert dates
nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

# Top 5 funds based on 3-year return
top5 = (
    perf
    .sort_values(
        "return_3yr_pct",
        ascending=False
    )
    .head(5)
)

plt.figure(figsize=(14, 7))

# -------------------------------
# Plot Top 5 Funds (Normalized)
# -------------------------------
for fund in top5["amfi_code"]:

    temp = (
        nav[nav["amfi_code"] == fund]
        .sort_values("date")
        .copy()
    )

    # Normalize NAV to 100
    temp["normalized"] = (
        temp["nav"] /
        temp["nav"].iloc[0]
    ) * 100

    fund_name = perf.loc[
        perf["amfi_code"] == fund,
        "scheme_name"
    ].values[0]

    plt.plot(
        temp["date"],
        temp["normalized"],
        label=fund_name
    )

# -------------------------------
# Plot Benchmarks (Normalized)
# -------------------------------
for idx in benchmark["index_name"].unique():

    temp = (
        benchmark[
            benchmark["index_name"] == idx
        ]
        .sort_values("date")
        .copy()
    )

    temp["normalized"] = (
        temp["close_value"] /
        temp["close_value"].iloc[0]
    ) * 100

    plt.plot(
        temp["date"],
        temp["normalized"],
        linestyle="--",
        linewidth=2,
        label=idx
    )

# -------------------------------
# Formatting
# -------------------------------
plt.title(
    "Top 5 Funds vs Benchmarks (Normalized Performance)"
)

plt.xlabel("Date")
plt.ylabel("Normalized Value (Base = 100)")
plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.grid(True, alpha=0.3)

plt.tight_layout()

# Save chart
plt.savefig(
    "reports/charts/benchmark_comparison_chart.png",
    bbox_inches="tight"
)

plt.close()

print("Benchmark Comparison Chart Created Successfully")