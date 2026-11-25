import numpy as np
import pandas as pd


def clean_used_car_data(raw_df: pd.DataFrame, ref_year: int = 2026) -> pd.DataFrame:
    """Clean raw used-car listings and engineer Phase 1 features."""
    df = raw_df.copy()
    df = df.drop(columns=['Unnamed: 0']).rename(columns={'ownsership': 'ownership'})
    df = df.drop_duplicates().reset_index(drop=True)

    valid_mask = (
        df['manufacturing_year'].astype(str).str.match(r'^\d{4}$') &
        df['fuel_type'].isin(['Petrol', 'Diesel', 'CNG']) &
        df['transmission'].isin(['Manual', 'Automatic'])
    )
    df = df[valid_mask].copy().reset_index(drop=True)
    df['manufacturing_year'] = df['manufacturing_year'].astype(int)

    df['insurance_validity'] = df['insurance_validity'].replace({
        'Third Party insurance': 'Third Party'
    })

    # Convert Rupee-entered prices to Lakhs
    df.loc[df['price(in lakhs)'] > 1000, 'price(in lakhs)'] /= 100000.0

    # Drop source-corrupted / redundant specification columns
    df = df.drop(columns=['max_power(bhp)', 'torque(Nm)'])

    # Median-impute missing or impossible mileage / engine values
    df.loc[(df['mileage(kmpl)'] < 5) | (df['mileage(kmpl)'] > 40), 'mileage(kmpl)'] = np.nan
    df.loc[(df['engine(cc)'] < 600) | (df['engine(cc)'] > 6000), 'engine(cc)'] = np.nan
    for col in ['mileage(kmpl)', 'engine(cc)']:
        df[col] = df[col].fillna(df[col].median())

    # Feature engineering
    df['car_age'] = ref_year - df['manufacturing_year']
    df['km_per_year'] = (df['kms_driven'] / df['car_age']).round(1)
    tokens = df['car_name'].str.strip().str.split()
    df['brand'] = tokens.apply(
        lambda t: 'Land Rover' if len(t) > 2 and t[1] == 'Land' and t[2] == 'Rover' else t[1]
    )

    return df.rename(columns={
        'mileage(kmpl)': 'mileage_kmpl',
        'engine(cc)': 'engine_cc',
        'price(in lakhs)': 'price_lakhs'
    })
