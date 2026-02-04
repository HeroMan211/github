import pandas as pd
import time

CITY_MAP = {
    "NY": "new york",
    "LA": "los angeles",
    "SF": "san francisco",
}

def clean_chunk(df):
    df = df.copy()

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["income"] = pd.to_numeric(df["income"], errors="coerce")
    df["city"] = df["city"].map(CITY_MAP)

    df = df.dropna()
    return df


def process_large_file(path_in, path_out, chunksize=500):
    start_time = time.time()
    total_rows = 0
    first_chunk = True

    for chunk in pd.read_csv(path_in, chunksize=chunksize):
        cleaned = clean_chunk(chunk)
        total_rows += len(cleaned)

        cleaned.to_csv(
            path_out,
            mode="w" if first_chunk else "a",
            index=False,
            header=first_chunk
        )
        first_chunk = False

    elapsed = time.time() - start_time

    print("Processing complete")
    print(f"Rows written: {total_rows}")
    print(f"Time elapsed: {elapsed:.2f} seconds")


process_large_file(
    path_in="day13_large_users.csv",
    path_out="day13_large_users_cleaned.csv",
    chunksize=500
)
