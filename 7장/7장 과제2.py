import ssl
import datetime
import urllib
import discord
import time
import requests
from bs4 import BeautifulSoup
import urllib.request as req
from urllib import parse
from tkinter import *
from weather_forecast import *
from discord_send_message import *
from send_to_discord import *

# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")

discord_url = 'https://discord.com/api/webhooks/1225310655695814746/LlkNFLAt3Y1oDrsD2EEMvn1DMyd0bj9JRJ1y-pE_EaVz6sNdjKPwfAeD_IMC6TUzuPoo'
weather_record = []

print("지금날씨 3.1")
loop = 0
while loop != 1:
    print("원하시는 서비스를 선택해주세요.")
    print(" 1. 서울날씨조회", "\n", "2. 지역날씨조회", "\n",
          "3. 전송된날씨 불러오기", "\n", "4. 날씨기록 삭제하기", "\n", "5. 나가기")
    choose = input()
    if choose == "1":
        print("원하시는 서비스를 선택해주세요.")
        print(" 1. 날씨조회", "\n", "2. 디스코드로 전송",
              "\n", "3. 디스코드 반복전송", "\n", "4. 처음으로 돌아가기")
        choose2 = input()
        if choose2 == "1":
            print("조회하는 중입니다. 잠시만 기다려주세요.")
            print(weather_forecast("서울"))
        if choose2 == "2":
            print("전송하는 중입니다. 잠시만 기다려주세요.")
            send_to_discord(weather_forecast("서울"))
        if choose2 == "3":
            print("반복할 횟수를 지정해주세요.")
            Loop = input()
            print("몇초마다 반복할지 지정해주세요.")
            Delay = input()
            print("전송하는 중입니다. 잠시만 기다려주세요.")
            for a in range(int(Loop)):
                weather_record.append(send_to_discord(weather_forecast("서울")))
                time.sleep(int(Delay))
                weather_record_seoul = open(
                    "weather_record_seoul.txt", "a", encoding="UTF-8")
                for line in weather_record:
                    weather_record_seoul.write(str(line))
                    weather_record_seoul.write("\n")
                weather_record_seoul.close()
        if choose2 == "4":
            loop = 0
    if choose == "2":
        print("원하시는 지역을 입력해주세요.")
        choose_city = input()
        print("원하시는 서비스를 선택해주세요.")
        print(f" 1. {choose_city}날씨조회", "\n", "2. 디스코드로 전송",
              "\n", "3. 디스코드 반복전송", "\n", "4. 처음으로 돌아가기")
        choose2 = input()
        if choose2 == "1":
            print("조회하는 중입니다. 잠시만 기다려주세요.")
            print(weather_forecast(choose_city))
        if choose2 == "2":
            print("전송하는 중입니다. 잠시만 기다려주세요.")
            send_to_discord(weather_forecast(choose_city))
        if choose2 == "3":
            print("반복할 횟수를 지정해주세요.")
            Loop = input()
            print("몇초마다 반복할지 지정해주세요.")
            Delay = input()
            print("전송하는 중입니다. 잠시만 기다려주세요.")
            for a in range(int(Loop)):
                weather_record.append(send_to_discord(
                    weather_forecast(choose_city)))
                time.sleep(int(Delay))
                weather_record_choose_city = open(
                    "weather_record_choose_city.txt", "a", encoding="UTF-8")
                for line in weather_record:
                    weather_record_choose_city.write(str(line))
                    weather_record_choose_city.write("\n")
                weather_record_choose_city.close()
        if choose2 == "4":
            loop = 0
    if choose == "3":
        print("원하시는 서비스를 입력해주세요.")
        print(" 1. 전송된 서울날씨 검색", "\n", "2. 전송된 지역날씨 검색", "\n",
              "3. 전송된 서울 날씨 중 가장 높은 기온", "\n", "4. 전송된 지역 날씨 중 가장 높은 기온", "\n", "5. 나가기")
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
            weather_read = open("weather_record_seoul.txt",
                                "r", encoding="UTF-8")
            for line in weather_read:
                weathergroup.append(line[2:21] + " " + line[31:33])
            for line in weathergroup:
                (day, Time, temperature) = line.split()
                temperatures[temperature] = day + " " + Time
            weather_read.close()
            print("가장 높았던 기온부터 순서대로 불러옵니다.")
            for each_temperatures in sorted(temperatures.keys(), reverse=True):
                print(each_temperatures + "°C")
                print(temperatures[each_temperatures])
                print("--------------------------")
        if choose2 == "4":
            weathergroup = []
            temperatures = {}
            weather_read = open("weather_record_choose_city.txt",
                                "r", encoding="UTF-8")
            for line in weather_read:
                weathergroup.append(
                    line[2:21] + " " + line[23:25] + " " + line[31:33])
            for line in weathergroup:
                (day, Time, choose_town, temperature) = line.split()
                temperatures[temperature] = day + \
                    " " + Time + " " + choose_town
            weather_read.close()
            print("가장 높았던 기온부터 순서대로 불러옵니다.")
            for each_temperatures in sorted(temperatures.keys(), reverse=True):
                print(each_temperatures + "°C")
                print(temperatures[each_temperatures])
                print("--------------------------")
        if choose2 == "5":
            loop = 0
    if choose == "4":
        print("삭제시킬 파일을 선택해주세요." "\n", "1. 서울날씨조회기록", "\n", "2. 지역날씨조회기록")
        choose2 = input()
        if choose2 == "1":
            weather_record_seoul_read = open("weather_record_seoul.txt", "w")
            weather_record_seoul_read.write("")
            weather_record_seoul_read.close()
            print("삭제되었습니다.")
        if choose2 == "2":
            weather_record_choose_city_read = open(
                "weather_record_choose_city.txt", "w")
            weather_record_choose_city_read.write("")
            weather_record_choose_city_read.close()
            print("삭제되었습니다.")
    if choose == "5":
        loop = 1
        print("BYE!")
