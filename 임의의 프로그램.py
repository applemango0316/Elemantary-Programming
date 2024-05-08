import ssl
import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
from urllib import parse


def weather_forecast(city):
    town = parse.quote(city + "날씨")
    context = ssl._create_unverified_context()
    webpage = urllib.request.urlopen(
        f'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query={town}', context=context)
    soup = BeautifulSoup(webpage, 'html.parser')
    temps = soup.find('div', 'temperature_text')
    summary = soup.find('p', 'summary')
    print(city + " " + temps.text.strip())
    print(summary.text.strip())

print("지금날씨 3.0")
loop = 0
while loop != 1:
    loop == 0
    choose = input("원하시는 서비스를 선택해주세요 (1. 서울날씨조회, 2. 지역날씨조회, 3.나가기)")
    if choose == "1":
        choose2 = input("원하시는 서비스를 선택해주세요 (1. 날씨조회, 2. 디스코드로 전송, 3. 나가기)")
        if choose2 == "1":
            choose_city = "서울"
            print(weather_forecast(choose_city))
        if choose2 == "3":
            loop == 1
    if choose == "2":
        choose_city = input("원하시는 지역를 입력해주세요.")
        choose2 = input("원하시는 서비스를 선택해주세요 (1. 날씨조회, 2. 디스코드로 전송, 3. 나가기)")
        if choose2 == "1":
            print(weather_forecast(choose_city))
        if choose2 == "3":
            loop == 1
    if choose == "3":
        loop == 1
