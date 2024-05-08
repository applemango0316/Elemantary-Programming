import ssl
import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
from urllib import parse

city = input("원하시는 지역를 입력해주세요.")
town = parse.quote(city + "날씨")
context = ssl._create_unverified_context()
webpage = urllib.request.urlopen(
    f'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query={town}', context=context)
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div', 'temperature_text')
summary = soup.find('p', 'summary')
temperture = temps.text.strip()
cloud = summary.text.strip()
print(city + " " + temperture)
# print(summary)
print(cloud)

print(temps)
