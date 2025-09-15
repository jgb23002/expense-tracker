import pandas as pd

def monthly_report(df: pd.DataFrame, month: int, year: int) -> str:
    if df.empty:
        return "No expenses recorded yet."
    mdf = df[(df["year"] == year) & (df["month"] == month)]
    if mdf.empty:
        return f"No expenses found for {year}-{month:02d}."
    total = mdf["amount"].sum()
    by_cat = mdf.groupby("category")["amount"].sum().sort_values(ascending=False)
    top_merchants = (
        mdf.groupby("description")["amount"].sum().sort_values(ascending=False).head(5)
    )
    lines = []
    lines.append("\N{SPIRAL CALENDAR} Monthly Report: {0}-{1:02d}".format(year, month))
    lines.append(f"• Total spend: ${total:,.2f}")
    lines.append("• By category:")
    for cat, amt in by_cat.items():
        pct = (amt / total) * 100 if total else 0
        lines.append(f"   - {cat}: ${amt:,.2f} ({pct:.1f}%)")
    if not top_merchants.empty:
        lines.append("• Top merchants/descriptions:")
        for desc, amt in top_merchants.items():
            lines.append(f"   - {desc}: ${amt:,.2f}")
    return "\n".join(lines)

def summary_report(df: pd.DataFrame) -> str:
    if df.empty:
        return "No expenses recorded yet."
    total = df["amount"].sum()
    by_month = df.groupby("ym")["amount"].sum().sort_index()
    by_cat = df.groupby("category")["amount"].sum().sort_values(ascending=False)

    lines = []
    lines.append("\N{RECEIPT} Expense Summary (All Time)")
    lines.append(f"• Total spend: ${total:,.2f}")
    lines.append("• Monthly totals:")
    for ym, amt in by_month.items():
        lines.append(f"   - {ym}: ${amt:,.2f}")
    lines.append("• By category:")
    for cat, amt in by_cat.items():
        pct = (amt / total) * 100 if total else 0
        lines.append(f"   - {cat}: ${amt:,.2f} ({pct:.1f}%)")
    return "\n".join(lines)
