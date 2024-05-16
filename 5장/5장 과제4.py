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

# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")

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
    weather_record.append(str(now.strftime('%Y-%m-%d %H:%M:%S')) + str(msg))
    f = open("weather.txt", "w", encoding="UTF-8")
    f.write(str(weather_now))
    print(weather_now)
    f.close()
    return weather_record


print("지금날씨 3.0")
loop = 0
while loop != 1:
    print("원하시는 서비스를 선택해주세요.")
    print(" 1. 서울날씨조회", "\n", "2. 지역날씨조회", "\n",
          "3. 전송된날씨 불러오기", "\n", "4. 나가기")
    choose = input()
    if choose == "1":
        print("원하시는 서비스를 선택해주세요.")
        print(" 1. 날씨조회", "\n", "2. 디스코드로 전송",
              "\n", "3. 디스코드 반복전송", "\n", "4. 나가기")
        choose2 = input()
        if choose2 == "1":
            print(weather_forecast("서울"))
        if choose2 == "2":
            msg = weather_forecast("서울")
            send_to_discord()
        if choose2 == "3":
            print("반복할 횟수를 지정해주세요.")
            Loop = input()
            print("몇초마다 반복할지 지정해주세요.")
            Delay = input()
            msg = weather_forecast("서울")
            for a in range(int(Loop)):
                send_to_discord()
                time.sleep(int(Delay))
                line_loop = 0
                weather_record_seoul = open(
                    "weather_record_seoul.txt", "w", encoding="UTF-8")
                for line in weather_record:
                    weather_record_seoul.write(str(line))
                    line_loop = line_loop + 1
                    if line_loop % 2 == 0:
                        weather_record_seoul.write("\n")
                weather_record_seoul.close()
        if choose2 == "4":
            loop = 1
            print("BYE!")
    if choose == "2":
        print("원하시는 지역을 입력해주세요.")
        choose_city = input()
        print("원하시는 서비스를 선택해주세요.")
        print(" 1. 날씨조회", "\n", "2. 디스코드로 전송",
              "\n", "3. 디스코드 반복전송", "\n", "4. 나가기")
        choose2 = input()
        if choose2 == "1":
            print(weather_forecast(choose_city))
        if choose2 == "2":
            msg = weather_forecast(choose_city)
            send_to_discord()
        if choose2 == "3":
            print("반복할 횟수를 지정해주세요.")
            Loop = input()
            print("몇초마다 반복할지 지정해주세요.")
            Delay = input()
            msg = weather_forecast(choose_city)
            for a in range(int(Loop)):
                send_to_discord()
                time.sleep(int(Delay))
                line_loop = 0
                weather_record_choose_city = open(
                    "weather_record_choose_city.txt", "w", encoding="UTF-8")
                for line in weather_record:
                    weather_record_choose_city.write(str(line))
                    line_loop = line_loop + 1
                    if line_loop % 2 == 0:
                        weather_record_choose_city.write("\n")
                weather_record_choose_city.close()
        if choose2 == "4":
            loop = 1
            print("BYE!")
    if choose == "3":
        print("원하시는 서비스를 입력해주세요.")
        print(" 1. 전송된 서울날씨 검색", "\n", "2. 전송된 지역날씨 검색", "\n",
              "3. 전송된 날씨 중 가장 높은 기온", "\n", "4. 나가기")
        choose2 = input()
        if choose2 == "1":
            weather_record_seoul_read = open(
                "weather_record_seoul.txt", "r", encoding="UTF-8")
            for line in weather_record_seoul_read:
                print(line)
        if choose2 == "2":
            weather_record_choose_city_read = open(
                "weather_record_choose_city.txt", "r", encoding="UTF-8")
            for line in weather_record_choose_city_read:
                print(line)
            weather_record_choose_city_read.close()
        if choose2 == "3":
            weathergroup = []
            temperatures = {}
            for line in weather_record:
                weathergroup.append(line[:19] + " " + line[29:33])
            for line in weathergroup:
                (day, Time, temperature) = line.split()
                temperatures[temperature] = day + " " + Time
            print("가장 높았던 기온을 불러옵니다.")
            for each_temperatures in sorted(temperatures.keys(), reverse=True):
                print(each_temperatures)
                print(temperatures[each_temperatures] + each_temperatures)

    if choose == "4":
        loop = 1
        print("BYE!")
