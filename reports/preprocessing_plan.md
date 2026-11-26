# Phase 2 Preprocessing Plan & Dataset Limitations

## 1. Feature & Target Setup
- **Target (`y`):** `price_lakhs` (Continuous — Regression task)
- **Numerical Features (`X`):** `car_age`, `kms_driven`, `mileage_kmpl`, `engine_cc`, `seats`, `km_per_year`
- **Categorical Features:** `brand`, `fuel_type`, `transmission`, `ownership`, `insurance_validity`

## 2. Planned Transformations (Semester IV)
- **Numerical:** Median imputation + `StandardScaler` (for Linear/Ridge models; tree models use raw scale).
- **Categorical:** Group rare brands into `Other`, then apply One-Hot Encoding.
- **Data Leakage Prevention:** Run `train_test_split` **first**, then fit all imputers, encoders, and scalers strictly on `X_train` via a Scikit-learn `Pipeline` and `ColumnTransformer`.

## 3. Dataset Limitations & Baseline
- No city/location column exists in the Kaggle CSV, so location-wise pricing cannot be analysed from this file.
- `max_power(bhp)` duplicated `engine(cc)` and `torque(Nm)` had stripped decimals, so both were excluded.
- **Phase 1 Baseline (Mean Predictor):** MAE = `₹11.70 Lakhs` (1-feature NumPy least-squares MAE = `₹10.85 Lakhs`).
