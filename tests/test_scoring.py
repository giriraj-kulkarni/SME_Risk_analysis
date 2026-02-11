import unittest
import pandas as pd
from src.ingest import load_data
from src.features import add_financial_features, add_trend_features
from src.scoring import add_behavioral_features, add_macro_features, calculate_risk_score

class TestScoring(unittest.TestCase):

    def setUp(self):
        self.df = load_data('data/raw/sme_portfolio_raw.csv')
        self.df = add_financial_features(self.df)
        self.df = add_trend_features(self.df)

    def test_add_behavioral_features(self):
        df = add_behavioral_features(self.df.copy())
        self.assertIn('Revenue_Decline', df.columns)
        self.assertIn('Inefficient_Growth', df.columns)
        # Check Revenue_Decline
        decline_rows = df[df['Revenue_Growth'] < 0]
        for _, row in decline_rows.iterrows():
            self.assertTrue(row['Revenue_Decline'])
        # Check Inefficient_Growth
        inefficient = df[(df['Employee_Growth'] > 0.1) & (df['Profit_Margin'] < 0.05)]
        for _, row in inefficient.iterrows():
            self.assertTrue(row['Inefficient_Growth'])

    def test_add_macro_features(self):
        df = add_macro_features(self.df.copy())
        self.assertIn('COVID_Impact', df.columns)
        self.assertIn('Recovery_Period', df.columns)
        # Check COVID_Impact
        covid_years = df[df['Year'].isin([2020, 2021])]
        for _, row in covid_years.iterrows():
            self.assertTrue(row['COVID_Impact'])
        non_covid = df[~df['Year'].isin([2020, 2021])]
        for _, row in non_covid.iterrows():
            self.assertFalse(row['COVID_Impact'])
        # Check Recovery_Period
        recovery = df[df['Year'] >= 2022]
        for _, row in recovery.iterrows():
            self.assertTrue(row['Recovery_Period'])
        non_recovery = df[df['Year'] < 2022]
        for _, row in non_recovery.iterrows():
            self.assertFalse(row['Recovery_Period'])

    def test_calculate_risk_score(self):
        df = add_behavioral_features(self.df.copy())
        df = add_macro_features(df)
        df = calculate_risk_score(df)
        self.assertIn('Risk_Score', df.columns)
        self.assertIn('Risk_Level', df.columns)
        # Check risk levels
        low = df[df['Risk_Score'] <= 3]
        for _, row in low.iterrows():
            self.assertEqual(row['Risk_Level'], 'Low')
        medium = df[(df['Risk_Score'] > 3) & (df['Risk_Score'] <= 6)]
        for _, row in medium.iterrows():
            self.assertEqual(row['Risk_Level'], 'Medium')
        high = df[df['Risk_Score'] > 6]
        for _, row in high.iterrows():
            self.assertEqual(row['Risk_Level'], 'High')
        # Manual check for first row
        row = df.iloc[0]
        score = 0
        if row['Profit_Margin'] < 0.07: score += 2
        if row['Debt_Ratio'] > 0.6: score += 3
        if row['Asset_Turnover'] < 0.8: score += 2
        if row['Revenue_Decline']: score += 1
        if row['Inefficient_Growth']: score += 2
        if row['COVID_Impact']: score += 1
        if not row['Recovery_Period']: score += 1
        self.assertEqual(row['Risk_Score'], score)

if __name__ == '__main__':
    unittest.main()
