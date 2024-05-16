import datetime
import discord
import requests
from weather_forecast import *
from discord_send_message import *

discord_url = 'https://discord.com/api/webhooks/1225310655695814746/LlkNFLAt3Y1oDrsD2EEMvn1DMyd0bj9JRJ1y-pE_EaVz6sNdjKPwfAeD_IMC6TUzuPoo'


def discord_send_message(text):
    now = datetime.datetime.now()
    message = {"content": f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {str(text)}"}
    requests.post(discord_url, data=message)
    return (message)
