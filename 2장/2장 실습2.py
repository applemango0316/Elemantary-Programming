# 20244021, 컴퓨터공학과, 김성준
import urllib.request
print("20244021, 컴퓨터공학과, 김성준")
page = urllib.request.urlopen("http://cs.sch.ac.kr/prices.py")
text = page.read().decode("utf8")
price = text[172:176]
print(price)
