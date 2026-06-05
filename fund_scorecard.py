# fund_scorecard.py

import pandas as pd

perf = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

perf["rank_return"] = perf["return_3yr_pct"].rank(
    ascending=False
)

perf["rank_sharpe"] = perf["sharpe_ratio"].rank(
    ascending=False
)

perf["rank_alpha"] = perf["alpha"].rank(
    ascending=False
)

perf["rank_expense"] = perf["expense_ratio_pct"].rank(
    ascending=True
)

perf["rank_drawdown"] = perf["max_drawdown_pct"].rank(
    ascending=True
)


perf["score"] = (
      0.30 * perf["rank_return"]
    + 0.25 * perf["rank_sharpe"]
    + 0.20 * perf["rank_alpha"]
    + 0.15 * perf["rank_expense"]
    + 0.10 * perf["rank_drawdown"]
)

perf = perf.sort_values(
    "score"
)

perf[
    [
        "amfi_code",
        "scheme_name",
        "score"
    ]
].to_csv(
    "reports/fund_scorecard.csv",
    index=False
)

print("fund_scorecard.csv created")