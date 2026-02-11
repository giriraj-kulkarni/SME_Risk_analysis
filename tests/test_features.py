import unittest
import pandas as pd
from src.ingest import load_data
from src.features import add_financial_features, add_trend_features

class TestFeatures(unittest.TestCase):

    def setUp(self):
        self.df = load_data('data/raw/sme_portfolio_raw.csv')

    def test_add_financial_features(self):
        df = add_financial_features(self.df.copy())
        self.assertIn('Profit_Margin', df.columns)
        self.assertIn('Debt_Ratio', df.columns)
        self.assertIn('Asset_Turnover', df.columns)
        # Check calculations for first row
        row = df.iloc[0]
        self.assertAlmostEqual(row['Profit_Margin'], row['Profit_Cr'] / row['Revenue_Cr'], places=6)
        self.assertAlmostEqual(row['Debt_Ratio'], row['Debt_Cr'] / row['Assets_Cr'], places=6)
        self.assertAlmostEqual(row['Asset_Turnover'], row['Revenue_Cr'] / row['Assets_Cr'], places=6)

    def test_add_trend_features(self):
        df = add_trend_features(self.df.copy())
        self.assertIn('Revenue_Growth', df.columns)
        self.assertIn('Employee_Growth', df.columns)
        # Check that first year growth is 0
        first_years = df.groupby('Company').head(1)
        for _, row in first_years.iterrows():
            self.assertEqual(row['Revenue_Growth'], 0)
            self.assertEqual(row['Employee_Growth'], 0)
        # Check growth calculation for a sample company
        company_df = df[df['Company'] == df['Company'].iloc[0]].sort_values('Year')
        if len(company_df) > 1:
            for i in range(1, len(company_df)):
                prev_rev = company_df.iloc[i-1]['Revenue_Cr']
                curr_rev = company_df.iloc[i]['Revenue_Cr']
                expected_growth = (curr_rev - prev_rev) / prev_rev if prev_rev != 0 else 0
                self.assertAlmostEqual(company_df.iloc[i]['Revenue_Growth'], expected_growth, places=6)
                prev_emp = company_df.iloc[i-1]['Employees']
                curr_emp = company_df.iloc[i]['Employees']
                expected_emp_growth = (curr_emp - prev_emp) / prev_emp if prev_emp != 0 else 0
                self.assertAlmostEqual(company_df.iloc[i]['Employee_Growth'], expected_emp_growth, places=6)

if __name__ == '__main__':
    unittest.main()
