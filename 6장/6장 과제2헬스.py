# 20244021, 컴퓨터공학과, 김성준
from transactions import *
import promotion
import starbuzz
from menu_list import *
print("20244021, 컴퓨터공학과, 김성준")

items = ["WORKOUT", "WEIGHTS", "BIKES"]
prices = [35.0, 10.0, 8.0]
running = True

while running:
    choice = menu_list(items)
    if choice == len(items) + 1:
        running = False
    else:
        credit_card = input("Credit card number:")
        price = promotion.discount(prices[choice-1])
        if input("Starbuzz card? ") == "Y":
            price = starbuzz.discount(price)
        save_transaction(price, credit_card, items[choice - 1])
