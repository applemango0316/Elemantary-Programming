#20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")
import urllib.request

def get_price():
    page = urllib.request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return text[start_of_price: end_of_price]

price = get_price()
print(price)