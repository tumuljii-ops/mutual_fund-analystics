-- 1 Top 5 Funds by AUM

SELECT scheme_name,
       aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2 Average NAV

SELECT AVG(nav) AS avg_nav
FROM fact_nav;


-- 3 NAV Records per Fund

SELECT amfi_code,
       COUNT(*) AS nav_records
FROM fact_nav
GROUP BY amfi_code;


-- 4 Transactions by State

SELECT state,
       COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;


-- 5 Funds with Expense Ratio < 1%

SELECT scheme_name,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 6 Average Transaction Amount

SELECT AVG(amount_inr)
FROM fact_transactions;


-- 7 Top Fund Houses by AUM

SELECT fund_house,
       MAX(aum_crore)
FROM fact_aum
GROUP BY fund_house
ORDER BY MAX(aum_crore) DESC;


-- 8 Average Sharpe Ratio

SELECT AVG(sharpe_ratio)
FROM fact_performance;


-- 9 Risk Category Distribution

SELECT risk_category,
       COUNT(*)
FROM dim_fund
GROUP BY risk_category;


-- 10 Top Sectors in Portfolio

SELECT sector,
       COUNT(*) AS holdings
FROM fact_portfolio
GROUP BY sector
ORDER BY holdings DESC;