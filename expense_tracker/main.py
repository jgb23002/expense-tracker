import argparse
from expense_tracker.models import Expense
from expense_tracker.utils import parse_date
from expense_tracker.categorize import auto_categorize
from expense_tracker.storage import append_row, load_df
from expense_tracker.reports import monthly_report, summary_report
from expense_tracker.plots import plot_monthly, plot_categories

def valid_month(s: str) -> int:
    m = int(s)
    if not 1 <= m <= 12:
        raise argparse.ArgumentTypeError("month must be 1..12")
    return m

def build_cli():
    p = argparse.ArgumentParser(description="Expense Tracker (CSV + Pandas + Matplotlib)")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="Add a new expense")
    p_add.add_argument("--desc", "--description", required=True, dest="desc", help="Description / merchant")
    p_add.add_argument("--amount", required=True, type=float, help="Amount (e.g., 12.34)")
    p_add.add_argument("--date", dest="date", default="today", help='Date (e.g., "2025-09-15" or "today")')
    p_add.add_argument("--category", dest="category", help="Optional category (overrides auto-categorizer)")

    p_rep = sub.add_parser("report", help="Print monthly report")
    p_rep.add_argument("--month", type=valid_month, required=True)
    p_rep.add_argument("--year", type=int, required=True)

    sub.add_parser("summary", help="Print all-time summary")
    sub.add_parser("plot-monthly", help="Show monthly spending line chart")

    p_cat = sub.add_parser("plot-categories", help="Show spending by category (bar or pie)")
    p_cat.add_argument("--month", type=valid_month)
    p_cat.add_argument("--year", type=int)
    p_cat.add_argument("--pie", action="store_true", help="Render a pie chart instead of bar")

    return p

def cmd_add(args):
    the_date = parse_date(args.date)
    category = args.category or auto_categorize(args.desc)
    append_row([the_date.isoformat(), args.desc.strip(), f"{float(args.amount):.2f}", category])
    print(f"Added: {the_date.isoformat()} | {args.desc.strip()} | ${float(args.amount):.2f} | {category}")

def main(argv=None):
    parser = build_cli()
    args = parser.parse_args(argv)

    if args.cmd == "add":
        cmd_add(args)
    elif args.cmd == "report":
        df = load_df()
        print(monthly_report(df, args.month, args.year))
    elif args.cmd == "summary":
        df = load_df()
        print(summary_report(df))
    elif args.cmd == "plot-monthly":
        df = load_df()
        plot_monthly(df)
    elif args.cmd == "plot-categories":
        df = load_df()
        plot_categories(df, args.month, args.year, args.pie)

if __name__ == "__main__":
    main()
