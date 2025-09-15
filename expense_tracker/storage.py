from pathlib import Path
import csv
import pandas as pd

COLUMNS = ["date", "description", "amount", "category"]

# CSV path inside the package's data folder
DATA_PATH = Path(__file__).resolve().parent / "data" / "expenses.csv"

def ensure_csv_exists() -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_PATH.exists():
        with DATA_PATH.open("w", newline="", encoding="utf-8") as f:
            f.write(",".join(COLUMNS) + "\n")

def append_row(row):
    ensure_csv_exists()
    with DATA_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

def load_df() -> pd.DataFrame:
    ensure_csv_exists()
    df = pd.read_csv(DATA_PATH)
    if df.empty:
        df = pd.DataFrame(columns=COLUMNS)
    # Normalize types
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["date", "amount"])
    # Convenience columns
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["ym"] = df["date"].dt.to_period("M").astype(str)
    if "category" not in df.columns:
        df["category"] = "Misc"
    return df
