import unittest
import pandas as pd
from src.ingest import load_data

class TestIngest(unittest.TestCase):

    def test_load_data_success(self):
        df = load_data('data/raw/sme_portfolio_raw.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (180, 8))
        self.assertIn('Company', df.columns)
        self.assertIn('Year', df.columns)
        self.assertIn('Revenue_Cr', df.columns)

    def test_load_data_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_data('nonexistent.csv')

if __name__ == '__main__':
    unittest.main()
