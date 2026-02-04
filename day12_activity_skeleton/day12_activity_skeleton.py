"""
Day 12 Activity: String & Date Cleaning
Tasks:
1) Clean city strings (strip, lower, remove punctuation)
2) Map synonyms to canonical values
3) Parse mixed-format timestamps and localize to UTC
"""

import pandas as pd

# TODO: Load data from data/day12_users.csv
df12 = pd.read_csv('day12_users.csv')


# TODO: Implement standardize_city(df)
df12["city_clean_basic"] = (
 df12["city"].str.strip().str.lower()
)

df12["city_clean_sep"] = (
    df12["city_clean_basic"]
    .str.replace("-", " ", regex=False) 
    .str.replace(r"[^a-z\s]", "", regex=True) 
    .str.replace(r"\s+", " ", regex=True).str.strip() )

# TODO: Implement parse_and_localize(df)

canonical_map = {"new york": "new york", "nyc": "new york", "ny": "new york",
 "san francisco": "san francisco", "sanfrancisco": "san francisco"}
df12["city_token"] = df12["city_clean_sep"].str.replace(" ", "", regex=False)
df12["city_canonical"] = df12["city_token"].map(canonical_map).fillna(df12["city_clean_sep"])
# TODO: Print cleaned columns for inspection
df12["signup_dt_raw"] = pd.to_datetime(df12["signup_time"], errors="coerce", infer_datetime_format=True)

print(df12)
print("NaT count:", df12["signup_dt_raw"].isna().sum())