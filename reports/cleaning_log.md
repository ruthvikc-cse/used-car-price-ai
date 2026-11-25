# Cleaning Decision Log — Used Car Dataset

- **Raw dataset:** `1,553 rows × 15 columns` (preserved untouched in `data/raw/`)
- **Cleaned dataset:** `1,108 rows × 15 columns` · **0 nulls (0%)**

| Column | Issue Found | Action Taken | Affected Rows |
| :--- | :--- | :--- | :--- |
| `Unnamed: 0` | Redundant row-index counter | Dropped column | 1,553 |
| All columns | Hidden duplicate listings once index ignored | Removed duplicate rows | 420 |
| `manufacturing_year` / `fuel_type` / `transmission` | Shifted columns (e.g., `Power Steering` in year, `5 Seats` in fuel) | Removed corrupted rows | 25 |
| `ownsership` | Spelling typo in raw header | Renamed to `ownership` | 1,108 |
| `insurance_validity` | Inconsistent label (`Third Party insurance`) | Standardized to `Third Party` | 337 |
| `price(in lakhs)` | Entered in Rupees (`70000`, `95000`) instead of Lakhs | Divided by `100,000` | 2 |
| `max_power(bhp)` | 100% identical to `engine(cc)` (scraping bug) | Dropped redundant column | 1,553 |
| `torque(Nm)` | Stripped decimals (`>1000 Nm` in >56% rows) | Dropped unreliable column | 1,553 |
| `mileage_kmpl` | Missing or impossible (`<5` or `>40 kmpl`) | Median imputed | 136 |
| `engine_cc` | Missing or impossible (`<600` or `>6000 cc`) | Median imputed | 107 |
| `car_age`, `km_per_year`, `brand` | Raw year & mixed `car_name` string | Engineered 3 features (Ref 2026) | 1,108 |
