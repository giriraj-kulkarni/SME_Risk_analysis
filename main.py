import os

from src.ingest import load_data
from src.features import add_financial_features, add_trend_features
from src.scoring import (
    add_behavioral_features,
    add_macro_features,
    calculate_risk_score
)


RAW_PATH = "data/raw/sme_portfolio_raw.csv"
PROCESSED_PATH = "data/processed/sme_portfolio_features.csv"
FINAL_PATH = "data/final/sme_portfolio_scored.csv"


def main():

    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("data/final", exist_ok=True)

    df = load_data(RAW_PATH)

    df = add_financial_features(df)
    df = add_trend_features(df)

    df.to_csv(PROCESSED_PATH, index=False)
    print("Saved processed features")

    df = add_behavioral_features(df)
    df = add_macro_features(df)
    df = calculate_risk_score(df)

    df.to_csv(FINAL_PATH, index=False)
    print("Saved final scored dataset")


if __name__ == "__main__":
    main()
