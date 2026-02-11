import pandas as pd

def add_behavioral_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add behavioral features based on company behavior over time.
    """
    # Example: Flag companies with declining revenue
    df["Revenue_Decline"] = df["Revenue_Growth"] < 0

    # Flag companies with high employee growth but low profit
    df["Inefficient_Growth"] = (df["Employee_Growth"] > 0.1) & (df["Profit_Margin"] < 0.05)

    return df

def add_macro_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add macroeconomic features based on year.
    """
    # Example: Higher risk during COVID years (2020-2021)
    df["COVID_Impact"] = df["Year"].isin([2020, 2021])

    # Example: Post-COVID recovery (2022-2024)
    df["Recovery_Period"] = df["Year"] >= 2022

    return df

def calculate_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate risk score based on financial, behavioral, and macro features.
    """
    def risk_score(row):
        score = 0

        # Financial risks
        if row["Profit_Margin"] < 0.07:
            score += 2
        if row["Debt_Ratio"] > 0.6:
            score += 3
        if row["Asset_Turnover"] < 0.8:
            score += 2

        # Behavioral risks
        if row["Revenue_Decline"]:
            score += 1
        if row["Inefficient_Growth"]:
            score += 2

        # Macro risks
        if row["COVID_Impact"]:
            score += 1
        if not row["Recovery_Period"]:
            score += 1

        return score

    df["Risk_Score"] = df.apply(risk_score, axis=1)

    def risk_label(score):
        if score <= 3:
            return "Low"
        elif score <= 6:
            return "Medium"
        else:
            return "High"

    df["Risk_Level"] = df["Risk_Score"].apply(risk_label)

    return df
