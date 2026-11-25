# Used Car Price Intelligence & Prediction System (Phase 1)

**BMS College of Engineering, Bengaluru — AI & ML Skill Lab (Semester III · HCL GUVI)**

## Team: Apex Mind's
| Name | USN |
| :--- | :--- |
| Thriveni G B | 1BM26CS464-T |
| Varsha P G | 1WN25CS292 |
| Sushma Kurugodappanavar | 1BM26CS420-T |
| Ruthvik C | 1WN25CS208 |

## Problem Statement
Buyers and sellers in the Indian used-car market struggle to judge fair resale value because pricing depends on age, kilometres driven, brand, fuel type, transmission, ownership, and engine capacity. Phase 1 establishes trustworthy cleaned data, statistical evidence, and a NumPy baseline before training regression models in Semester IV.

## Dataset & Cleaning Summary
- **Source:** Kaggle — Used Car Prices (India) (`Used Car Dataset.csv`)
- **Raw Data:** 1,553 rows × 15 columns (4 columns with missing values; 420 hidden duplicate listings; 25 column-shifted rows; 2 Rupee-entered prices)
- **Cleaned Data:** 1,108 rows × 15 columns · **0 nulls (0%)**
- **Key Transformations:** Removed duplicates & shifted rows, fixed INR-entered prices to ₹ Lakhs, dropped corrupted/redundant columns (`max_power(bhp)` duplicated `engine(cc)`; `torque(Nm)` had stripped decimals), median-imputed invalid mileage/engine values, and engineered `car_age` (Ref 2026), `km_per_year`, and `brand`.
- **Model-Ready Arrays:** `X: (1108, 6)` · `y: (1108,)` (standardized via NumPy broadcasting)

## Key Phase 1 Findings
- **Mean / Median Price:** ₹13.74 Lakhs / ₹6.73 Lakhs (Std: ₹17.18 Lakhs)
- **Empirical Probability:** `P(price < 10 Lakhs) = 67.7%`
- **Correlations:** `r(car_age, price) = -0.357` (Spearman `-0.543`), `r(engine_cc, price) = +0.489`
- **Baseline MAE (Mean Predictor):** ₹11.70 Lakhs (`1-feature NumPy lstsq MAE = ₹10.85 Lakhs`)
- **Hypothesis Test (Diesel vs Petrol):** Diesel median ₹11.82 L vs Petrol ₹5.77 L (Mann–Whitney U, `p = 1.68e-27`)

## Repository Structure
```text
used-car-price-ai/
├── data/
│   ├── raw/Used Car Dataset.csv
│   └── processed/
│       ├── cleaned_used_cars.csv
│       └── cleaned_used_cars.xlsx
├── notebooks/
│   └── Phase1_Used_Car_Price_Intelligence.ipynb
├── src/
│   └── preprocessing.py
├── reports/
│   ├── phase1_eda_dashboard.png
│   └── phase1_eda_extended.png
├── requirements.txt
├── .gitignore
└── README.md
