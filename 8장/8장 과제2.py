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
from tkinter import scrolledtext
from tkinter import ttk
from PIL import Image, ImageTk

app = Tk()
app.title("지금날씨4.0")
app.geometry('500x300+200+100')
country = []

Icon = Image.open('찌삐찌삐사진.jpg')
photo = ImageTk.PhotoImage(Icon)
app.wm_iconphoto(False, photo)

# 메뉴 스위칭 함수


def seoul_button():
    a1.grid_remove()
    a2.grid_remove()
    a3.grid_remove()
    a4.grid_remove()
    a5.grid_remove()
    b1.grid()
    b2.grid()
    b3.grid()
    b4.grid()
    b5.grid()
    b_text.grid()


def seoul_button_back():
    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    b5.grid_remove()
    b_text.grid_remove()
    a1.grid()
    a2.grid()
    a3.grid()
    a4.grid()
    a5.grid()


def seoul_repeat_button1():
    b1.grid_remove()
    b2.grid_remove()
    b3.grid_remove()
    b4.grid_remove()
    b5.grid_remove()
    b_text.grid_remove()
    seoul_repeat_input1.grid()
    seoul_repeat_submit_button1.grid()
    choose_repeat.grid()


def seoul_repeat_button2():
    seoul_repeat_input1.grid_remove()
    seoul_repeat_submit_button1.grid_remove()
    choose_repeat.grid_remove()
    seoul_repeat_input2.grid()
    seoul_repeat_submit_button2.grid()
    choose_delay.grid()


def seoul_repeat_button_back():
    seoul_repeat_input2.grid_remove()
    seoul_repeat_submit_button2.grid_remove()
    choose_delay.grid_remove()
    b1.grid()
    b2.grid()
    b3.grid()
    b4.grid()
    b5.grid()
    b_text.grid()


def country_button1():
    a1.grid_remove()
    a2.grid_remove()
    a3.grid_remove()
    a4.grid_remove()
    a5.grid_remove()
    country_input.grid()
    submit_button.grid()
    choose_country.grid()


def country_button2():
    country_input.grid_remove()
    submit_button.grid_remove()
    choose_country.grid_remove()
    c1.grid()
    c2.grid()
    c3.grid()
    c4.grid()
    c5.grid()
    c_text.grid()


def country_button_back():
    c1.grid_remove()
    c2.grid_remove()
    c3.grid_remove()
    c4.grid_remove()
    c5.grid_remove()
    c_text.grid_remove()
    a1.grid()
    a2.grid()
    a3.grid()
    a4.grid()
    a5.grid()


def country_repeat_button1():
    c1.grid_remove()
    c2.grid_remove()
    c3.grid_remove()
    c4.grid_remove()
    c5.grid_remove()
    c_text.grid_remove()
    country_repeat_input1.grid()
    country_repeat_submit_button1.grid()
    choose_repeat.grid()


def country_repeat_button2():
    country_repeat_input1.grid_remove()
    country_repeat_submit_button1.grid_remove()
    choose_repeat.grid_remove()
    country_repeat_input2.grid()
    country_repeat_submit_button2.grid()
    choose_delay.grid()


def country_repeat_button_back():
    country_repeat_input2.grid_remove()
    country_repeat_submit_button2.grid_remove()
    choose_delay.grid_remove()
    c1.grid()
    c2.grid()
    c3.grid()
    c4.grid()
    c5.grid()
    c_text.grid()


def submit_button_command():
    show_input()
    country_button2()


def record_button():
    a1.grid_remove()
    a2.grid_remove()
    a3.grid_remove()
    a4.grid_remove()
    a5.grid_remove()
    d1.grid()
    d2.grid()
    d3.grid()
    d4.grid()
    d5.grid()
    d6.grid()
    d_text.grid()


def record_button_back():
    d1.grid_remove()
    d2.grid_remove()
    d3.grid_remove()
    d4.grid_remove()
    d5.grid_remove()
    d6.grid_remove()
    d_text.grid_remove()
    a1.grid()
    a2.grid()
    a3.grid()
    a4.grid()
    a5.grid()


def remove_button():
    a1.grid_remove()
    a2.grid_remove()
    a3.grid_remove()
    a4.grid_remove()
    a5.grid_remove()
    e1.grid()
    e2.grid()
    e3.grid()
    e4.grid()
    e_text.grid()


def remove_button_back():
    e1.grid_remove()
    e2.grid_remove()
    e3.grid_remove()
    e4.grid_remove()
    e_text.grid_remove()
    a1.grid()
    a2.grid()
    a3.grid()
    a4.grid()
    a5.grid()


# 인풋값 함수

def show_input():
    user_input = country_input.get()
    country.append(user_input)
    c1_name = str(user_input) + " 날씨조회"
    c1.config(text=c1_name)
    global input_country
    input_country = user_input
    return input_country


def country_repeat_submit_button1_command():
    country_repeat_button2()
    global country_repeat_input_text1
    country_repeat_input_text1 = country_repeat_input1.get()
    return country_repeat_input_text1


def seoul_repeat_submit_button1_command():
    seoul_repeat_button2()
    global seoul_repeat_input_text1
    seoul_repeat_input_text1 = seoul_repeat_input1.get()
    return seoul_repeat_input_text1

# 날씨 조회 함수


def weather_seoul_():
    seoul_now = weather_forecast("서울")
    b_text.insert(END, seoul_now)
    b_text.insert(END, "\n")


def weather_country_():
    country_now = weather_forecast(input_country)
    c_text.insert(END, country_now)
    c_text.insert(END, "\n")

# 디스코드 전송 함수


def weather_seoul():
    seoul_now = send_to_discord(weather_forecast("서울"))
    seoul_record = open("weather_record_seoul.txt", "a", encoding="UTF-8")
    seoul_record.write(str(seoul_now))
    seoul_record.write("\n")
    b_text.insert(END, seoul_now)
    b_text.insert(END, "\n전송되었습니다.\n")
    seoul_record.close()


def weather_country():
    country_now = send_to_discord(weather_forecast(input_country))
    country_record = open(
        "weather_record_choose_city.txt", "a", encoding="UTF-8")
    country_record.write(str(country_now))
    country_record.write("\n")
    c_text.insert(END, country_now)
    c_text.insert(END, "\n전송되었습니다.\n")
    country_record.close()

# 디스코드 반복 전송 함수


def seoul_repeat_submit_button2_command():
    seoul_repeat_input_text2 = seoul_repeat_input2.get()
    seoul_repeat_button_back()
    i = 0
    for loop in range(int(seoul_repeat_input_text1)):
        i = i + 1
        text = "전송되었습니다.", i, f"/{seoul_repeat_input_text1}\n"
        seoul_record = open("weather_record_seoul.txt", "a", encoding="UTF-8")
        seoul_record.write(str(send_to_discord(weather_forecast("서울"))))
        seoul_record.write("\n")
        time.sleep(int(seoul_repeat_input_text2))
        b_text.insert(END, weather_forecast("서울"))
        b_text.insert(END, text)
        seoul_record.close()


def country_repeat_submit_button2_command():
    country_repeat_input_text2 = country_repeat_input2.get()
    country_repeat_button_back()
    i = 0
    for loop in range(int(country_repeat_input_text1)):
        i = i + 1
        text = "전송되었습니다.", i, f"/{country_repeat_input_text1}\n"
        country_record = open(
            "weather_record_choose_city.txt", "a", encoding="UTF-8")
        country_record.write(
            str(send_to_discord(weather_forecast(input_country))))
        country_record.write("\n")
        time.sleep(int(country_repeat_input_text2))
        c_text.insert(END, weather_forecast(str(input_country)))
        c_text.insert(END, text)
        country_record.close()

# 불러오기 함수


def seoul_record_read():
    seoul_record = open("weather_record_seoul.txt", "r", encoding="UTF-8")
    i = 0
    for line in seoul_record:
        i = i + 1
        d_text.insert(END, i)
        d_text.insert(END, ". ")
        d_text.insert(END, line)
        d_text.insert(END, "\n")
    seoul_record.close()


def country_record_read():
    country_record = open(
        "weather_record_choose_city.txt", "r", encoding="UTF-8")
    i = 0
    for line in country_record:
        i = i + 1
        d_text.insert(END, i)
        d_text.insert(END, ". ")
        d_text.insert(END, line)
        d_text.insert(END, "\n")
    country_record.close()

# 순서대로 불러오기 함수


def seoul_record_line():
    weathergroup = []
    temperatures = {}
    seoul_record = open("weather_record_seoul.txt", "r", encoding="UTF-8")
    for line in seoul_record:
        (a, b, c, d, e) = line.split("'")
        weathergroup.append(line[2:21] + " " + b[:2] + " " + b[8:-1])
    for line in weathergroup:
        (day, Time, trash, temperature) = line.split()
        temperatures[temperature] = day + " " + Time
    seoul_record.close()
    for each_temperatures in sorted(temperatures.keys(), reverse=True):
        each_temperatures_ = each_temperatures + "°C\n"
        temperatures_ = temperatures[each_temperatures] + " 서울\n"
        d_text.insert(END, each_temperatures_)
        d_text.insert(END, temperatures_)
        d_text.insert(END, "--------------------------\n")


def country_record_line():
    weathergroup = []
    temperatures = {}
    country_record = open(
        "weather_record_choose_city.txt", "r", encoding="UTF-8")
    for line in country_record:
        (a, b, c, d, e) = line.split("'")
        weathergroup.append(line[2:21] + " " + b[:2] + " " + b[8:-1])
    for line in weathergroup:
        (day, Time, choose_town, temperature) = line.split()
        temperatures[temperature] = day + " " + Time + " " + choose_town
    country_record.close()
    for each_temperatures in sorted(temperatures.keys(), reverse=True):
        each_temperatures_ = each_temperatures + "°C\n"
        temperatures_ = temperatures[each_temperatures] + "\n"
        d_text.insert(END, each_temperatures_)
        d_text.insert(END, temperatures_)
        d_text.insert(END, "--------------------------\n")

# 삭제 함수


def seoul_record_remove():
    seoul_record = open("weather_record_seoul.txt", "w")
    seoul_record.write("")
    seoul_record.close()
    e_text.insert(END, "삭제되었습니다.\n")


def country_record_remove():
    country_record = open("weather_record_choose_city.txt", "w")
    country_record.write("")
    country_record.close()
    e_text.insert(END, "삭제되었습니다.\n")

# 지우기 함수


def seoul_delete():
    b_text.delete(1.0, END)


def country_delete():
    c_text.delete(1.0, END)


def record_delete():
    d_text.delete(1.0, END)


def remove_delete():
    e_text.delete(1.0, END)

# 기본화면 위젯구성


a1 = Button(app, text="서울날씨조회", command=seoul_button)
a1.grid(row=1, column=1, padx=10, pady=10)

a2 = Button(app, text="지역날씨조회", command=country_button1)
a2.grid(row=1, column=2, padx=10, pady=10)

a3 = Button(app, text="전송된날씨 불러오기", command=record_button)
a3.grid(row=2, column=1, padx=10, pady=10)

a4 = Button(app, text="날씨기록 삭제하기", command=remove_button)
a4.grid(row=2, column=2, padx=10, pady=10)

a5 = Button(app, text="나가기", command=app.destroy)
a5.grid(row=3, column=1, padx=10, pady=10)

# 서울날씨조회 위젯구성

b1 = Button(app, text="날씨조회", command=weather_seoul_)
b1.grid(row=4, column=1, padx=10, pady=10)
b1.grid_remove()

b2 = Button(app, text="디스코드로 전송", command=weather_seoul)
b2.grid(row=4, column=2, padx=10, pady=10)
b2.grid_remove()

b3 = Button(app, text="디스코드 반복전송", command=seoul_repeat_button1)
b3.grid(row=5, column=2, padx=10, pady=10)
b3.grid_remove()

seoul_repeat_input1 = Entry(app)
seoul_repeat_input1.grid(row=2, column=2, padx=10, pady=10)
seoul_repeat_input1.grid_remove()

seoul_repeat_submit_button1 = Button(
    app, text="Submit", command=seoul_repeat_submit_button1_command)
seoul_repeat_submit_button1.grid(row=3, column=2, pady=10)
seoul_repeat_submit_button1.grid_remove()

seoul_repeat_input2 = Entry(app)
seoul_repeat_input2.grid(row=2, column=2, padx=10, pady=10)
seoul_repeat_input2.grid_remove()

seoul_repeat_submit_button2 = Button(
    app, text="Submit", command=seoul_repeat_submit_button2_command)
seoul_repeat_submit_button2.grid(row=3, column=2, pady=10)
seoul_repeat_submit_button2.grid_remove()

b4 = Button(app, text="처음으로 돌아가기", command=seoul_button_back)
b4.grid(row=5, column=1, padx=10, pady=10)
b4.grid_remove()

b5 = Button(app, text="지우기", command=seoul_delete)
b5.grid(row=4, column=3, padx=10, pady=10)
b5.grid_remove()

b_text = scrolledtext.ScrolledText(app, wrap=WORD, width=30, height=10)
b_text.grid(row=0, column=2, padx=10, pady=10)
b_text.grid_remove()

# 지역날씨조회 위젯구성

country_input = Entry(app)
country_input.grid(row=2, column=2, padx=10, pady=10)
country_input.grid_remove()

submit_button = Button(app, text="Submit", command=submit_button_command)
submit_button.grid(row=3, column=2, pady=10)
submit_button.grid_remove()

country_repeat_input1 = Entry(app)
country_repeat_input1.grid(row=10, column=2, padx=10, pady=10)
country_repeat_input1.grid_remove()

country_repeat_submit_button1 = Button(
    app, text="Submit", command=country_repeat_submit_button1_command)
country_repeat_submit_button1.grid(row=11, column=2, pady=10)
country_repeat_submit_button1.grid_remove()

country_repeat_input2 = Entry(app)
country_repeat_input2.grid(row=10, column=2, padx=10, pady=10)
country_repeat_input2.grid_remove()

country_repeat_submit_button2 = Button(
    app, text="Submit", command=country_repeat_submit_button2_command)
country_repeat_submit_button2.grid(row=11, column=2, pady=10)
country_repeat_submit_button2.grid_remove()

c1 = Button(app, text="날씨조회", command=weather_country_)
c1.grid(row=4, column=1, padx=10, pady=10,)
c1.grid_remove()

c2 = Button(app, text="디스코드로 전송", command=weather_country)
c2.grid(row=4, column=2, padx=10, pady=10)
c2.grid_remove()

c3 = Button(app, text="디스코드 반복전송", command=country_repeat_button1)
c3.grid(row=5, column=2, padx=10, pady=10)
c3.grid_remove()

c4 = Button(app, text="처음으로 돌아가기", command=country_button_back)
c4.grid(row=5, column=1, padx=10, pady=10)
c4.grid_remove()

c5 = Button(app, text="지우기", command=country_delete)
c5.grid(row=4, column=3, padx=10, pady=10)
c5.grid_remove()

c_text = scrolledtext.ScrolledText(app, wrap=WORD, width=30, height=10)
c_text.grid(row=0, column=2, padx=10, pady=10)
c_text.grid_remove()

# 전송된날씨 불러오기 위젯구성

d1 = Button(app, text="전송된 서울날씨 검색", command=seoul_record_read)
d1.grid(row=4, column=2, padx=10, pady=10)
d1.grid_remove()

d2 = Button(app, text="전송된 지역날씨 검색", command=country_record_read)
d2.grid(row=4, column=3, padx=10, pady=10)
d2.grid_remove()

d3 = Button(app, text="전송된 서울 날씨 중 가장 높은 기온", command=seoul_record_line)
d3.grid(row=5, column=2, padx=10, pady=10)
d3.grid_remove()

d4 = Button(app, text="전송된 지역 날씨 중 가장 높은 기온", command=country_record_line)
d4.grid(row=5, column=3, padx=10, pady=10)
d4.grid_remove()

d5 = Button(app, text="처음으로 돌아가기", command=record_button_back)
d5.grid(row=6, column=2, padx=10, pady=10)
d5.grid_remove()

d6 = Button(app, text="지우기", command=record_delete)
d6.grid(row=6, column=3, padx=10, pady=10)
d6.grid_remove()

d_text = scrolledtext.ScrolledText(app, wrap=WORD, width=30, height=10)
d_text.grid(row=0, column=2, padx=10, pady=10)
d_text.grid_remove()

# 날씨기록 삭제하기 위젯구성

e1 = Button(app, text="서울 날씨 조회 기록", command=seoul_record_remove)
e1.grid(row=3, column=1, padx=10, pady=10)
e1.grid_remove()

e2 = Button(app, text="지역 날씨 조회 기록", command=country_record_remove)
e2.grid(row=3, column=2, padx=10, pady=10)
e2.grid_remove()

e_text = scrolledtext.ScrolledText(app, wrap=WORD, width=30, height=10)
e_text.grid(row=0, column=2, padx=10, pady=10)
e_text.grid_remove()

e3 = Button(app, text="처음으로 돌아가기", command=remove_button_back)
e3.grid(row=4, column=1, padx=10, pady=10)
e3.grid_remove()

e4 = Button(app, text="지우기", command=remove_delete)
e4.grid(row=4, column=2, padx=10, pady=10)
e4.grid_remove()

# 인풋 설명 라벨


choose_country = Label(app, text="조회하실 지역의 이름을 입력해주세요.", font=("Arial", 10))
choose_country.grid(row=0, column=2, padx=20, pady=20)
choose_country.grid_remove()

choose_repeat = Label(app, text="반복하실 횟수를 입력해주세요.", font=("Arial", 10))
choose_country.grid(row=0, column=2, padx=20, pady=20)
choose_country.grid_remove()

choose_delay = Label(app, text="전송 지연 시간(초)를 입력해주세요.", font=("Arial", 10))
choose_country.grid(row=0, column=2, padx=20, pady=20)
choose_country.grid_remove()


app.mainloop()
