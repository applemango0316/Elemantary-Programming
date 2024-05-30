import datetime
import discord
import requests
import urllib
from weather_forecast import *
from discord_send_message import *


def send_to_discord(msg):
    weather_now = []
    weather = []
    discord_send_message(msg)
    now = datetime.datetime.now()
    weather_now.append(str(now.strftime('%Y-%m-%d %H:%M:%S')))
    weather_now.append(str(msg))
    weather.append(
        str(now.strftime('%Y-%m-%d %H:%M:%S')) + str(msg))
    print(weather_now)
    return weather
