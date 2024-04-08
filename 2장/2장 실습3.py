# 20244021, 컴퓨터공학과, 김성준
import urllib.request
print("20244021, 컴퓨터공학과, 김성준")
page = urllib.request.urlopen("http://cs.sch.ac.kr/prices.py")
text = page.read().decode("utf8")
where = text.find(">$")
start_of_price = where + 2
end_of_price = start_of_price + 4
price = text[start_of_price: end_of_price]
print(price)
