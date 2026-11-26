# Data Dictionary — Used Car Price Intelligence (Phase 1)

| Column | Meaning / Calculation | Unit / Type |
| :--- | :--- | :--- |
| `car_name` | Full raw vehicle listing title | Text |
| `brand` | Manufacturer extracted from `car_name` (2nd token) | Category |
| `registration_year` | Original registration month/year | Text |
| `manufacturing_year` | Validated 4-digit year of manufacture (2007–2023) | Integer (Year) |
| `car_age` | Engineered feature: `2026 - manufacturing_year` | Integer (Years) |
| `insurance_validity` | Standardized insurance status | Category |
| `fuel_type` | Vehicle fuel category (`Petrol`, `Diesel`, `CNG`) | Category |
| `seats` | Seating capacity (4–8) | Integer |
| `kms_driven` | Total odometer distance driven | Integer (km) |
| `km_per_year` | Engineered usage rate: `kms_driven / car_age` | Float (km/yr) |
| `ownership` | Ownership sequence (`First`, `Second`, `Third Owner`) | Category |
| `transmission` | Gearbox type (`Manual`, `Automatic`) | Category |
| `mileage_kmpl` | Validated & median-imputed fuel efficiency (5–40 km/l) | Float (km/l) |
| `engine_cc` | Validated & median-imputed engine displacement (600–6000 cc) | Float (cc) |
| `price_lakhs` | Target variable: used-car resale price | Float (₹ Lakhs) |
