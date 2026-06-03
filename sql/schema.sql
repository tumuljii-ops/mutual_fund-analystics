-- Dimension Table

CREATE TABLE dim_fund(
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date TEXT,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    fund_manager TEXT,
    risk_category TEXT
);

-- NAV Fact

CREATE TABLE fact_nav(
    amfi_code INTEGER,
    date TEXT,
    nav REAL,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

-- Performance Fact

CREATE TABLE fact_performance(
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    expense_ratio_pct REAL,
    aum_crore REAL,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

-- AUM Fact

CREATE TABLE fact_aum(
    date TEXT,
    fund_house TEXT,
    aum_lakh_crore REAL,
    aum_crore REAL,
    num_schemes INTEGER
);

-- Transactions Fact

CREATE TABLE fact_transactions(
    investor_id TEXT,
    transaction_date TEXT,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

-- Portfolio Fact

CREATE TABLE fact_portfolio(
    amfi_code INTEGER,
    stock_symbol TEXT,
    stock_name TEXT,
    sector TEXT,
    weight_pct REAL,
    market_value_cr REAL,
    current_price_inr REAL,
    portfolio_date TEXT,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);