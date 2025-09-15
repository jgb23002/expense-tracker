from datetime import date
from dateutil import parser as dateparser

def parse_date(s: str) -> date:
    if s is None:
        return date.today()
    s = s.strip().lower()
    if s in {"today", "now"}:
        return date.today()
    return dateparser.parse(s).date()
