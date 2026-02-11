import pandas as pd


# Financial Ratios

def add_financial_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create core financial risk ratios used in credit analysis.
    """

    df["Profit_Margin"] = df["Profit_Cr"] / df["Revenue_Cr"]
    df["Debt_Ratio"] = df["Debt_Cr"] / df["Assets_Cr"]
    df["Asset_Turnover"] = df["Revenue_Cr"] / df["Assets_Cr"]

    return df


# Trend / Time-series Features

def add_trend_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create growth indicators to capture business momentum.
    """

    df = df.sort_values(["Company", "Year"])

    df["Revenue_Growth"] = (
        df.groupby("Company")["Revenue_Cr"].pct_change()
    )

    df["Employee_Growth"] = (
        df.groupby("Company")["Employees"].pct_change()
    )

    # first year will be NaN → replace with 0
    df.fillna(0, inplace=True)

    return df


