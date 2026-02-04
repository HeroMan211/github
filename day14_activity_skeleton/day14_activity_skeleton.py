"""
Day 14 Activity: Full Cleaning Pipeline
Tasks:
1) Build clean_data() that orchestrates type, missing, outliers, strings/dates
2) Add basic validation checks
3) Run end-to-end and inspect
"""

import pandas as pd
import numpy as np

df = pd.read_csv("day14_users_raw.csv")



# TODO: Implement clean_types(df)
def clean_types(df):
    out = df.copy()
    out["age"] = pd.to_numeric(out["age"], errors="coerce")
    out["income"] = pd.to_numeric(out["income"], errors="coerce")
    return out

# TODO: Implement clean_missing(df)
def clean_missing(df):
    out = df.copy()
    out["age"] = out["age"].fillna(out["age"].median())
    return out

# TODO: Implement handle_outliers(df)
def handle_outliers(df):
    upper_99 = df["income"].quantile(0.99)
    mask_keep = df["income"] <= upper_99
    df_removed = df[mask_keep].copy()
    return df_removed

# TODO: Implement clean_strings_and_dates(df)
def clean_strings_and_dates(df):
    out = df.copy()
    mapping = {
        "ny" : "new york",
        "sf" : "south fransisco",
        "la" : "los angeles",
    }

    out["city"] = out["city"].str.strip().str.lower()
    out["city"] = (out["city"].str.replace("-", " ", regex=False).str.replace(r"[^a-z\s]", "", regex=True).str.replace(r"\s+", " ", regex=True).str.strip()) 
    out["city"] = out["city"].map(mapping)
    out["signup_time"] = pd.to_datetime(out["signup_time"], errors="coerce")
    return out


# TODO: Implement validate_cleaned(df)
def validate_cleaned(df):
    assert df["age"].min() >= 0, "Negative ages found"
    assert df["income"].notna().all(), "Income still has NaN"

# TODO: Implement clean_data(df) that calls the above in order
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = clean_types(df)
    df = clean_missing(df)
    df = handle_outliers(df)
    df = clean_strings_and_dates(df)
    validate_cleaned(df)  
    return df

print(clean_data(df))
