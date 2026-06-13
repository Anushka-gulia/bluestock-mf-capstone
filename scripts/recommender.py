def recommend_funds(risk_appetite, recommender_df):

    return (
        recommender_df[
            recommender_df["risk_grade"] == risk_appetite
        ]
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )