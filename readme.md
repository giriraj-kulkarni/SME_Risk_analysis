## Dashboard Preview

![SME Risk Dashboard](dashboard\example_dashboard.png)

# SME Risk Assessment Project

This project analyzes the risk levels of Small and Medium Enterprises (SMEs) based on financial and operational data.

## Project Structure

- `main.py`: Main script to run the entire pipeline
- `generate_data.py`: Generates synthetic SME data
- `src/`: Source code modules
  - `ingest.py`: Data loading
  - `features.py`: Feature engineering
  - `scoring.py`: Risk scoring logic
- `data/`: Data directories
  - `raw/`: Raw input data
  - `processed/`: Processed features
  - `final/`: Final scored dataset
- `archive/`: Archived code
- `notebooks/`: Jupyter notebooks for analysis
- `reports/`: Generated reports
- `sql/`: Database schema

## Features

### Financial Ratios
- Profit Margin
- Debt Ratio
- Asset Turnover

### Trend Features
- Revenue Growth
- Employee Growth

### Behavioral Features
- Revenue Decline flag
- Inefficient Growth flag

### Macro Features
- COVID Impact (2020-2021)
- Recovery Period (2022+)

## Risk Scoring Methodology

### Feature Calculations

#### Financial Ratios
- **Profit Margin** = Profit_Cr / Revenue_Cr
- **Debt Ratio** = Debt_Cr / Assets_Cr
- **Asset Turnover** = Revenue_Cr / Assets_Cr

#### Trend Features
- **Revenue Growth** = Percentage change in Revenue_Cr by company (year-over-year)
- **Employee Growth** = Percentage change in Employees by company (year-over-year)

#### Behavioral Features
- **Revenue Decline** = True if Revenue_Growth < 0 (declining revenue)
- **Inefficient Growth** = True if (Employee_Growth > 0.1) AND (Profit_Margin < 0.05)

#### Macro Features
- **COVID Impact** = True for years 2020-2021 (higher risk period)
- **Recovery Period** = True for years 2022+ (post-COVID recovery)

### Risk Score Calculation

The risk score is calculated by summing points from various risk factors:

#### Financial Risk Points
- Profit_Margin < 0.07: +2 points
- Debt_Ratio > 0.6: +3 points
- Asset_Turnover < 0.8: +2 points

#### Behavioral Risk Points
- Revenue_Decline = True: +1 point
- Inefficient_Growth = True: +2 points

#### Macro Risk Points
- COVID_Impact = True: +1 point
- Recovery_Period = False: +1 point

### Risk Level Classification
- **Low Risk**: Score ≤ 3
- **Medium Risk**: Score 4-6
- **High Risk**: Score > 6

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download the project** to your local machine.

2. **Navigate to the project directory**:
   ```bash
   cd /path/to/sme-risk-project
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The main dependency is `pandas` for data manipulation.

## How to Run the Project

### Step 1: Prepare Data

The project comes with pre-generated sample data in `data/raw/sme_portfolio_raw.csv`. If you want to generate new synthetic data:

```bash
python generate_data.py
```

This will create a new dataset in `data/raw/sme_portfolio.csv` (note: the script saves to a different path than the default raw file).

### Step 2: Run the Risk Analysis

Execute the main analysis pipeline:

```bash
python main.py
```

This script will:
- Load data from `data/raw/sme_portfolio_raw.csv`
- Calculate financial ratios and trend features
- Add behavioral and macro features
- Compute risk scores and levels
- Save processed data to `data/processed/sme_portfolio_features.csv`
- Save final scored data to `data/final/sme_portfolio_scored.csv`

### Step 3: View Results

- **Processed features**: Open `data/processed/sme_portfolio_features.csv`
- **Final scored dataset**: Open `data/final/sme_portfolio_scored.csv`

The final file contains all original columns plus:
- Financial ratios (Profit_Margin, Debt_Ratio, Asset_Turnover)
- Trend features (Revenue_Growth, Employee_Growth)
- Behavioral flags (Revenue_Decline, Inefficient_Growth)
- Macro flags (COVID_Impact, Recovery_Period)
- Risk_Score and Risk_Level

### Optional: Explore in Notebooks

If you have Jupyter installed, you can explore the data in the `notebooks/` directory:

```bash
jupyter notebook notebooks/
```

### Optional: View Reports

Check the `reports/` directory for any generated analysis reports.

## Troubleshooting

- **ModuleNotFoundError**: Ensure all dependencies are installed with `pip install -r requirements.txt`
- **FileNotFoundError**: Verify the data file exists in `data/raw/sme_portfolio_raw.csv`
- **PermissionError**: Ensure write permissions for the `data/` directories
- **Data issues**: Check that the CSV file has the correct column names and data types

## Dependencies

- pandas >= 1.0.0

Install with:
```bash
pip install -r requirements.txt
