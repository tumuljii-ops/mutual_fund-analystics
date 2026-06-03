# Data Dictionary

## dim_fund

| Column | Description |
|----------|----------|
| amfi_code | Unique scheme identifier |
| fund_house | AMC name |
| scheme_name | Mutual fund scheme |
| category | Fund category |
| sub_category | Detailed category |
| benchmark | Benchmark index |
| fund_manager | Fund manager |
| risk_category | Risk classification |

---

## fact_nav

| Column | Description |
|----------|----------|
| amfi_code | Scheme code |
| date | NAV date |
| nav | Net Asset Value |

---

## fact_transactions

| Column | Description |
|----------|----------|
| investor_id | Investor ID |
| transaction_date | Transaction date |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction amount |
| state | Investor state |
| city | Investor city |

---

## fact_performance

| Column | Description |
|----------|----------|
| return_1yr_pct | 1 year return |
| return_3yr_pct | 3 year return |
| return_5yr_pct | 5 year return |
| alpha | Alpha |
| beta | Beta |
| sharpe_ratio | Sharpe Ratio |

---

## fact_aum

| Column | Description |
|----------|----------|
| fund_house | AMC |
| aum_crore | Assets under management |

---

## fact_portfolio

| Column | Description |
|----------|----------|
| stock_symbol | Stock ticker |
| sector | Sector |
| weight_pct | Portfolio weight |