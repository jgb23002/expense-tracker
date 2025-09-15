import pandas as pd
import matplotlib.pyplot as plt

def plot_monthly(df: pd.DataFrame) -> None:
    if df.empty:
        print("No data to plot.")
        return
    monthly = df.groupby("ym")["amount"].sum().sort_index()
    plt.figure()
    monthly.plot(kind="line", marker="o")
    plt.title("Monthly Spending Over Time")
    plt.xlabel("Month")
    plt.ylabel("Amount ($)")
    plt.tight_layout()
    plt.show()

def plot_categories(df: pd.DataFrame, month=None, year=None, pie=False) -> None:
    if df.empty:
        print("No data to plot.")
        return
    title_suffix = " — All Time"
    if month and year:
        df = df[(df["year"] == year) & (df["month"] == month)]
        title_suffix = f" — {year}-{month:02d}"
    if df.empty:
        print("No matching data to plot.")
        return
    by_cat = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    plt.figure()
    if pie:
        plt.pie(by_cat.values, labels=by_cat.index, autopct="%1.1f%%")
        plt.title("Spending by Category" + title_suffix)
    else:
        by_cat.plot(kind="bar")
        plt.title("Spending by Category" + title_suffix)
        plt.xlabel("Category")
        plt.ylabel("Amount ($)")
    plt.tight_layout()
    plt.show()
