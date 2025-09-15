from dataclasses import dataclass
from datetime import date

@dataclass
class Expense:
    date: date
    description: str
    amount: float
    category: str
