# 20244021, 컴퓨터공학과, 김성준
import urllib.request
print("20244021, 컴퓨터공학과, 김성준")

price = 99.99
while price > 4.74:
    page = urllib.request.urlopen("http://cs.sch.ac.kr./prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    price = float(text[start_of_price: end_of_price])
print("Buy!")
