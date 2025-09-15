from typing import Dict, List

# Keys = category; values = list of lowercase keywords to match in description
CATEGORY_RULES: Dict[str, List[str]] = {
    "Groceries": ["grocery", "supermarket", "trader joe", "whole foods", "aldi", "kroger", "stop & shop"],
    "Dining": ["restaurant", "dining", "chipotle", "mcdonald", "subway", "pizza", "cafe", "coffee", "starbucks"],
    "Transport": ["uber", "lyft", "bus", "subway", "metro", "train", "gas", "fuel", "toll", "parking"],
    "Shopping": ["amazon", "target", "walmart", "best buy", "mall", "clothes", "apparel"],
    "Health": ["pharmacy", "cvs", "walgreens", "doctor", "dentist", "copay", "med", "gym"],
    "Utilities": ["electric", "water", "gas bill", "internet", "wifi", "phone bill"],
    "Entertainment": ["movie", "netflix", "spotify", "hulu", "game", "concert"],
    "Education": ["tuition", "book", "course", "udemy", "coursera", "textbook"],
    "Rent": ["rent", "landlord", "lease"],
    "Travel": ["airbnb", "hotel", "flight", "airline", "delta", "united", "american airlines", "southwest"],
    "Misc": [],
}

def auto_categorize(description: str) -> str:
    d = (description or "").lower()
    for cat, keywords in CATEGORY_RULES.items():
        if any(k in d for k in keywords):
            return cat
    return "Misc"
