import pandas as pd
import random

companies = [
"FANUC India Pvt. Ltd.","Kelvion India Pvt. Ltd.","Tenneco Automotive India Pvt. Ltd.",
"Prowess Engineering Pvt. Ltd.","Mercedes-Benz India","Endurance","Sidel India Pvt. Ltd.",
"Sun Electro Devices Pvt. Ltd.","Badve Autocomps Pvt. Ltd.","ZF India Pvt. Ltd.",
"Schindler India Pvt. Ltd.","JBM MA Automotive Pvt. Ltd.","ATS Conveyors India Pvt. Ltd.",
"Hyundai Construction Equipment Pvt. Ltd.","Horiba India Pvt. Ltd.","Geberit India",
"Atlas Copco","Volkswagen Motorsport India","Bridgestone India","Bosch Chassis Systems",
"Mitsubishi Electric","Lumax Auto Technologies","Frontline Electronics Ltd",
"Bharat Automotive Pressings India Pvt. Ltd.","KTR Couplings India Pvt. Ltd.",
"Asian Paints","Wipro PARI","Piaggio Vehicles Pvt. Ltd.","Ferrero India Pvt. Ltd.",
"POSCO Maharashtra Pvt. Ltd."
]

years = [2019, 2020, 2021, 2022, 2023, 2024]

rows = []

for company in companies:

    segment = random.choice(["Small","Medium","Large"])

    if segment == "Small":
        revenue = random.uniform(5, 25)
    elif segment == "Medium":
        revenue = random.uniform(25, 120)
    else:
        revenue = random.uniform(120, 500)

    for year in years:

        if year in [2020, 2021]:
            revenue *= random.uniform(0.7, 0.9)
        else:
            revenue *= random.uniform(1.05, 1.12)

        profit = revenue * random.uniform(0.05, 0.15)
        debt = revenue * random.uniform(0.4, 0.7)
        assets = revenue * random.uniform(1.2, 1.6)
        employees = int(revenue * 10)

        rows.append([
            company, year, segment,
            round(revenue,2), round(profit,2),
            round(debt,2), round(assets,2), employees
        ])

df = pd.DataFrame(rows, columns=[
    "Company","Year","Segment",
    "Revenue_Cr","Profit_Cr","Debt_Cr","Assets_Cr","Employees"
])

df.to_csv("../data/sme_portfolio.csv", index=False)

print("✅ Dataset created successfully")
print(df.head())
