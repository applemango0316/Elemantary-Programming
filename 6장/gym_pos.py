# 20244021, 컴퓨터공학과, 김성준
from transactions import *
print("20244021, 컴퓨터공학과, 김성준")

items = ["WORKOUT", "WEIGHTS", "BIKES"]
prices = [35.0, 10.0, 8.0]
running = True

while running:
    option = 1
    for choice in items:
        print(str(option) + "." + choice)
        option = option + 1
    print(str(option) + ".QUIT")
    choice = int(input("Choose an option:"))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number:")
        save_transaction(prices[choice-1], credit_card, items[choice - 1])
