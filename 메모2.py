import ssl
import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
from urllib import parse

city = "서울날씨"
town = parse.quote(city)
context = ssl._create_unverified_context()
webpage = urllib.request.urlopen(
    f'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query={town}', context=context)
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div', 'temperature_text')
summary = soup.find('p', 'summary')
print(temps)
print(city + " " + temps.text.strip())
# print(summary)
print(summary.text.strip())
