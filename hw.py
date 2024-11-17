from datetime import datetime

def get_days_from_today(date):
    iso_date = date
    dfi = datetime.fromisoformat(iso_date)
    current_day = datetime.today()
    return current_day - dfi


print(get_days_from_today("2025-02-11"))


import random

def get_numbers_ticket(min, max, quantity):
    num = range(min, max)
    win = random.choices(num, k=quantity)
    return win


print(get_numbers_ticket(4, 10, 7))


import re

def normalize_phone(phone_number):
    nume = phone_number
    pattern = r"[\D]"
    # pattern = r"[;,\-:!\.()\\t\\n\r\s\\]"
    replacement = ""
    modified_text = re.sub(pattern, replacement, nume)
    if len(modified_text) < 12:
        modified_text =  "+38" + modified_text
    elif len(modified_text)  == 12:
        modified_text = "+" + modified_text
    return modified_text


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


