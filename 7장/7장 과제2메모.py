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

app = Tk()
app.title("지금날씨4.0")
app.geometry('300x150+200+100')


def switch_widgets(widget_to_hide, widget_to_show):
    widget_to_hide.grid_forget()
    widget_to_show.grid()


def change(variable):

    variable = variable + 1
    return variable


loop = 0
loop1 = 0

b1 = Button(app, text="서울날씨조회", command=change(loop1))
b1.grid(row=1, column=1, padx=10, pady=10)

b2 = Button(app, text="지역날씨조회")
b2.grid(row=1, column=2, padx=10, pady=10)

b3 = Button(app, text="전송된날씨 불러오기")
b3.grid(row=2, column=1, padx=10, pady=10)

b4 = Button(app, text="날씨기록 삭제하기")
b4.grid(row=2, column=2, padx=10, pady=10)

b5 = Button(app, text="나기기", command=app.destroy)
b5.grid(row=3, column=1, padx=10, pady=10)

first_look = b1, b2, b3, b4, b5

b6 = Button(app, text="날씨조회", command=change(loop))
b6.grid_forget(row=3, column=2, padx=10, pady=10)

second_look = b6


if loop1 == 1:
    switch_widgets(first_look, second_look)

app.mainloop()
