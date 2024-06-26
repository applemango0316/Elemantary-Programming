# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


class Transactions():
    print = 0.0
    credit_card = 0
    item = 0

    def __init__(self, cost, card, itm):
        self.price = cost
        self.credit_card = card
        self.item = itm

    def save(self):
        file = open("transactions.txt", "a")
        file.write("%07d%16s%16s\n" %
                   (self.price * 100, self.credit_card, self.item))
        file.close()


class Discount_trans(Transactions):
    def __init__(self, cost, card, itm):
        Transactions.__init__(self, cost, card, itm)

    def save(self):
        file = open("transactions.txt", "a")
        file.write("%07d%16s%16s\n" %
                   (self.price * 100 * 0.9, self.credit_card, self.item))
        file.close()


items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
price = [1.50, 2.20, 1.80, 1.20]
running = True

while running:
    option = 1
    for choice in items:
        print(str(option) + "." + choice)
        option = option + 1
    print(str(option) + ". QUIT")
    choice = int(input("Choose an option:"))
    if choice == option:
        running = False
    else:
        card = input("Credit card number:")
        if input("Starbuzz card? ") == "Y":
            trans = Discount_trans(price[choice-1], card, items[choice - 1])
            trans.save()
        else:
            trans = Transactions(price[choice-1], card, items[choice - 1])
            trans.save()
