import ssl
import datetime
import urllib
import discord
import time
from bs4 import BeautifulSoup
import urllib.request as req
from urllib import parse
from discord_send_message import *
from send_to_discord import *
from weather_forecast import *

discord_url = 'https://discord.com/api/webhooks/1225310655695814746/LlkNFLAt3Y1oDrsD2EEMvn1DMyd0bj9JRJ1y-pE_EaVz6sNdjKPwfAeD_IMC6TUzuPoo'
weather_record = []
msg = text


def discord_send_message(text):
    now = datetime.datetime.now()
    message = {"content": f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {str(text)}"}
    requests.post(discord_url, data=message)
    return (message)


def send_to_discord():
    weather_now = []
    discord_send_message(msg)
    now = datetime.datetime.now()
    weather_now.append(str(now.strftime('%Y-%m-%d %H:%M:%S')))
    weather_now.append(str(msg))
    weather_record.append(str(now.strftime('%Y-%m-%d %H:%M:%S')))
    weather_record.append(str(msg))
    f = open("weather.txt", "w", encoding="UTF-8")
    f.write(str(weather_now))
    print(weather_now)
    f.close()
    return weather_record


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
        if choose2 == "2":
            msg = weather_forecast(choose_city)
            send_to_discord(msg)
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
