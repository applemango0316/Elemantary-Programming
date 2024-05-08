import datetime
import discord
import requests
from discord_send_message import *


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
