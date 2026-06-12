import pandas as pd

perf = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)


def get_recommendations(risk_level):

    temp = perf[
        perf["risk_grade"]
        .str.lower()
        ==
        risk_level.lower()
    ]

    result = (
        temp.sort_values(
            "sharpe_ratio",
            ascending=False
        )
        [
            [
                "scheme_name",
                "fund_house",
                "risk_grade",
                "sharpe_ratio",
                "aum_crore"
            ]
        ]
        .head(3)
    )

    return result


risk = input(
    "Enter Risk Level: "
)

recommendations = get_recommendations(
    risk
)

print("\nTop 3 Recommended Funds\n")

print(
    recommendations
)

recommendations.to_csv(
    "reports/recommendation_table.csv",
    index=False
)