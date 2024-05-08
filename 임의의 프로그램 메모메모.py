import ssl
import datetime
import urllib
import discord
import time
import requests
from bs4 import BeautifulSoup
import urllib.request as req
from urllib import parse
from weather_forecast import *

discord_url = 'https://discord.com/api/webhooks/1225310655695814746/LlkNFLAt3Y1oDrsD2EEMvn1DMyd0bj9JRJ1y-pE_EaVz6sNdjKPwfAeD_IMC6TUzuPoo'
weather_record = []


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
    choose = input("원하시는 서비스를 선택해주세요 (1. 서울날씨조회, 2. 지역날씨조회, 3.나가기)")
    if choose == "1":
        choose2 = input(
            "원하시는 서비스를 선택해주세요 (1. 날씨조회, 2. 디스코드로 전송, 3, 디스코드 반복전송, 4. 나가기)")
        if choose2 == "1":
            print(weather_forecast("서울"))
        if choose2 == "2":
            msg = weather_forecast("서울")
            send_to_discord()
        if choose2 == "3":
            Loop = input("반복할 횟수를 지정해주세요.")
            Delay = input("몇초마다 반복할지 지정해주세요.")
            msg = weather_forecast("서울")
            for a in range(int(Loop)):
                send_to_discord()
                time.sleep(int(Delay))
                line_loop = 0
                weather_record_seoul = open(
                    "weather_record_seoul.txt", "w", encoding="UTF-8")
                for line in weather_record:
                    weather_record_seoul.write(str(line))
                    weather_record_seoul.write("\n")
                    line_loop = line_loop + 1
                    if line_loop % 2 == 0:
                        weather_record_seoul.write("\n")
                weather_record_seoul.close()
        if choose2 == "4":
            loop = 1
            print("BYE!")
    if choose == "2":
        choose_city = input("원하시는 지역를 입력해주세요.")
        choose2 = input(
            "원하시는 서비스를 선택해주세요 (1. 날씨조회, 2. 디스코드로 전송, 3. 디스코드 반복전송, 4. 나가기)")
        if choose2 == "1":
            print(weather_forecast(choose_city))
        if choose2 == "2":
            msg = weather_forecast(choose_city)
            send_to_discord()
        if choose2 == "3":
            Loop = input("반복할 횟수를 지정해주세요.")
            Delay = input("몇초마다 반복할지 지정해주세요.")
            msg = weather_forecast(choose_city)
            for a in range(int(Loop)):
                send_to_discord()
                time.sleep(int(Delay))
                line_loop = 0
                weather_record_choose_city = open(
                    "weather_record_choose_city.txt", "w", encoding="UTF-8")
                for line in weather_record:
                    weather_record_choose_city.write(str(line))
                    weather_record_choose_city.write("\n")
                    line_loop = line_loop + 1
                    if line_loop % 2 == 0:
                        weather_record_choose_city.write("\n")
                weather_record_choose_city.close()
        if choose2 == "3":
            loop = 1
            print("BYE!")
    if choose == "3":
        loop = 1
        print("BYE!")
