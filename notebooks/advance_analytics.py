import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


nav = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

risk_results = []

for fund in nav["amfi_code"].unique():

    temp = (
        nav[
            nav["amfi_code"] == fund
        ]
        .sort_values("date")
    )

    returns = (
        temp["nav"]
        .pct_change()
        .dropna()
    )

    var95 = np.percentile(
        returns,
        5
    )

    cvar95 = returns[
        returns <= var95
    ].mean()

    risk_results.append(
        [
            fund,
            var95,
            cvar95
        ]
    )

risk_df = pd.DataFrame(
    risk_results,
    columns=[
        "amfi_code",
        "VaR_95",
        "CVaR_95"
    ]
)

risk_df.to_csv(
    "reports/var_cvar_report.csv",
    index=False
)

risk_df.head()



perf = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

top5 = (
    perf
    .sort_values(
        "aum_crore",
        ascending=False
    )
    .head(5)
)

plt.figure(figsize=(12,6))

for fund in top5["amfi_code"]:

    temp = (
        nav[
            nav["amfi_code"] == fund
        ]
        .sort_values("date")
    )

    returns = temp["nav"].pct_change()

    sharpe = (
        returns.rolling(90).mean()
        /
        returns.rolling(90).std()
    ) * np.sqrt(252)

    plt.plot(
        temp["date"],
        sharpe,
        label=str(fund)
    )

plt.legend()

plt.title(
    "Rolling 90 Day Sharpe Ratio"
)

plt.savefig(
    "reports/rolling_sharpe_chart.png",
    bbox_inches="tight"
)

plt.show()

txn = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

first_txn = (
    txn.groupby("investor_id")
    ["transaction_date"]
    .min()
)

cohort_map = first_txn.dt.year

txn["cohort_year"] = txn[
    "investor_id"
].map(cohort_map)

cohort_summary = (
    txn.groupby("cohort_year")
    .agg(
        avg_sip_amount=(
            "amount_inr",
            "mean"
        ),
        total_invested=(
            "amount_inr",
            "sum"
        )
    )
)

cohort_summary

top_funds = (
    txn.groupby(
        [
            "cohort_year",
            "amfi_code"
        ]
    )
    .size()
    .reset_index(name="count")
)

top_funds = (
    top_funds.sort_values(
        "count",
        ascending=False
    )
    .groupby("cohort_year")
    .head(1)
)

top_funds

sip = txn[
    txn["transaction_type"]
    .str.lower()
    == "sip"
].copy()

risk_investors = []

for inv,group in sip.groupby(
    "investor_id"
):

    if len(group) < 6:
        continue

    group = group.sort_values(
        "transaction_date"
    )

    gaps = (
        group["transaction_date"]
        .diff()
        .dt.days
    )

    avg_gap = gaps.mean()

    risk_flag = (
        "At Risk"
        if avg_gap > 35
        else "Healthy"
    )

    risk_investors.append(
        [
            inv,
            avg_gap,
            risk_flag
        ]
    )

sip_continuity = pd.DataFrame(
    risk_investors,
    columns=[
        "investor_id",
        "avg_gap_days",
        "status"
    ]
)

sip_continuity.head()

holdings = pd.read_csv(
    "data/processed/09_portfolio_holdings_cleaned.csv"
)

hhi = (
    holdings
    .groupby("amfi_code")
    ["weight_pct"]
    .apply(
        lambda x:
        ((x/100)**2).sum()
    )
)

hhi = hhi.reset_index()

hhi.columns = [
    "amfi_code",
    "HHI"
]

hhi.sort_values(
    "HHI",
    ascending=False
).head()

cohort_summary.to_csv(
    "reports/cohort_analysis.csv",
    index=True
)

top_funds.to_csv(
    "reports/cohort_top_funds.csv",
    index=False
)

sip_continuity.to_csv(
    "reports/sip_continuity_report.csv",
    index=False
)

hhi.to_csv(
    "reports/hhi_report.csv",
    index=False
)

print(
    perf["risk_grade"]
    .value_counts()
)

highest_var = risk_df.loc[
    risk_df["VaR_95"].idxmin()
]

highest_cvar = risk_df.loc[
    risk_df["CVaR_95"].idxmin()
]

highest_hhi = hhi.loc[
    hhi["HHI"].idxmax()
]

lowest_hhi = hhi.loc[
    hhi["HHI"].idxmin()
]

at_risk_count = (
    sip_continuity["status"]
    ==
    "At Risk"
).sum()

print("\n===== ADVANCED INSIGHTS =====\n")

print(
    f"1. Highest VaR Fund: {highest_var['amfi_code']}"
)

print(
    f"2. Highest CVaR Fund: {highest_cvar['amfi_code']}"
)

print(
    f"3. Most Concentrated Portfolio: {highest_hhi['amfi_code']}"
)

print(
    f"4. Most Diversified Portfolio: {lowest_hhi['amfi_code']}"
)

print(
    f"5. At-Risk Investors: {at_risk_count}"
)