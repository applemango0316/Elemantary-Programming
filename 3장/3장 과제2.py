#20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")
import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    t = text.find(">P")
    TS = t + 10
    TE = TS + 24
    return float(text[start_of_price: end_of_price]), text[TS: TE]

def get_price1():
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price: end_of_price])

price_now = input("Do you want to see the price now (Y/N)? ")
if price_now == "Y":
    print(get_price1())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(1)
        price = get_price1()
    print(get_price())
    print("Buy!")