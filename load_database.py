from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# =====================================
# DIM FUND
# =====================================

fund = pd.read_csv(
    "data/processed/01_fund_master_cleaned.csv"
)

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund loaded")


# =====================================
# FACT NAV
# =====================================

nav = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded")


# =====================================
# FACT AUM
# =====================================

aum = pd.read_csv(
    "data/processed/03_aum_by_fund_house_cleaned.csv"
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("fact_aum loaded")


# =====================================
# FACT PERFORMANCE
# =====================================

perf = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded")


# =====================================
# FACT TRANSACTIONS
# =====================================

txn = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded")


# =====================================
# FACT PORTFOLIO
# =====================================

portfolio = pd.read_csv(
    "data/processed/09_portfolio_holdings_cleaned.csv"
)

portfolio.to_sql(
    "fact_portfolio",
    engine,
    if_exists="replace",
    index=False
)

print("fact_portfolio loaded")


print("\nDatabase Created Successfully")