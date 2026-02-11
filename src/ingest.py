import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Load the raw SME portfolio data from CSV.
    """
    return pd.read_csv(path)
