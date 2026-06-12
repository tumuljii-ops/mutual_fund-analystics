import pandas as pd
import os

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

# ==========================================
# 01 FUND MASTER
# ==========================================

fund_master = pd.read_csv(f"{RAW}/01_fund_master.csv")

fund_master = fund_master.drop_duplicates()

fund_master.to_csv(
    f"{PROCESSED}/01_fund_master_cleaned.csv",
    index=False
)

print("Fund Master Cleaned")


# ==========================================
# 02 NAV HISTORY
# ==========================================

nav = pd.read_csv(f"{RAW}/02_nav_history.csv")

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav = nav.dropna(subset=["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    f"{PROCESSED}/02_nav_history_cleaned.csv",
    index=False
)

print("NAV History Cleaned")

# ==========================================
# 03 AUM
# ==========================================

aum = pd.read_csv(f"{RAW}/03_aum_by_fund_house.csv")

aum = aum.drop_duplicates()

aum.to_csv(
    f"{PROCESSED}/03_aum_by_fund_house_cleaned.csv",
    index=False
)

print("AUM Cleaned")


# ==========================================
# 04 SIP INFLOWS
# ==========================================

sip = pd.read_csv(f"{RAW}/04_monthly_sip_inflows.csv")

sip = sip.drop_duplicates()

sip.to_csv(
    f"{PROCESSED}/04_monthly_sip_inflows_cleaned.csv",
    index=False
)

print("SIP Cleaned")


# ==========================================
# 05 CATEGORY INFLOWS
# ==========================================

cat = pd.read_csv(f"{RAW}/05_category_inflows.csv")

cat = cat.drop_duplicates()

cat.to_csv(
    f"{PROCESSED}/05_category_inflows_cleaned.csv",
    index=False
)

print("Category Inflows Cleaned")


# ==========================================
# 06 INDUSTRY FOLIO
# ==========================================

folio = pd.read_csv(f"{RAW}/06_industry_folio_count.csv")

folio = folio.drop_duplicates()

folio.to_csv(
    f"{PROCESSED}/06_industry_folio_count_cleaned.csv",
    index=False
)

print("Industry Folio Cleaned")


# ==========================================
# 07 SCHEME PERFORMANCE
# ==========================================

perf = pd.read_csv(f"{RAW}/07_scheme_performance.csv")

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense ratio validation
perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

perf = perf.drop_duplicates()

perf.to_csv(
    f"{PROCESSED}/07_scheme_performance_cleaned.csv",
    index=False
)

print("Scheme Performance Cleaned")


# ==========================================
# 08 INVESTOR TRANSACTIONS
# ==========================================

txn = pd.read_csv(
    f"{RAW}/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

txn = txn[
    txn["transaction_type"]
    .isin(
        [
            "Sip",
            "Lumpsum",
            "Redemption"
        ]
    )
]

txn = txn[
    txn["amount_inr"] > 0
]

txn = txn.drop_duplicates()

txn.to_csv(
    f"{PROCESSED}/08_investor_transactions_cleaned.csv",
    index=False
)

print("Investor Transactions Cleaned")


# ==========================================
# 09 PORTFOLIO HOLDINGS
# ==========================================

portfolio = pd.read_csv(
    f"{RAW}/09_portfolio_holdings.csv"
)

portfolio = portfolio.drop_duplicates()

portfolio.to_csv(
    f"{PROCESSED}/09_portfolio_holdings_cleaned.csv",
    index=False
)

print("Portfolio Holdings Cleaned")


# ==========================================
# 10 BENCHMARK
# ==========================================

benchmark = pd.read_csv(
    f"{RAW}/10_benchmark_indices.csv"
)

benchmark = benchmark.drop_duplicates()

benchmark.to_csv(
    f"{PROCESSED}/10_benchmark_indices_cleaned.csv",
    index=False
)

print("Benchmark Cleaned")

print("\nAll 10 datasets cleaned successfully.")