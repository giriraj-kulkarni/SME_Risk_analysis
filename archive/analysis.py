import pandas as pd

df = pd.read_csv("data/sme_portfolio.csv")

print(df.head())
print(df.shape)

df["Profit_Margin"] = df["Profit_Cr"] / df["Revenue_Cr"]

df["Debt_Ratio"] = df["Debt_Cr"] / df["Assets_Cr"]

df["Asset_Turnover"] = df["Revenue_Cr"] / df["Assets_Cr"]

print(df.head())

def risk_score(row):
    score = 0

    # Low profitability
    if row["Profit_Margin"] < 0.07:
        score += 2

    # High debt
    if row["Debt_Ratio"] > 0.6:
        score += 3

    # Low efficiency
    if row["Asset_Turnover"] < 0.8:
        score += 2

    return score


df["Risk_Score"] = df.apply(risk_score, axis=1)
def risk_label(score):
    if score <= 2:
        return "Low"
    elif score <= 5:
        return "Medium"
    else:
        return "High"

df["Risk_Level"] = df["Risk_Score"].apply(risk_label)
df.to_csv("sme_portfolio_scored.csv", index=False)
print(df["Risk_Level"].value_counts())

print(df.groupby("Year")["Risk_Level"].value_counts())


print("✅ Risk scoring complete")
