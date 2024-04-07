# 20244021, 컴퓨터공학과, 김성준
import time
import urllib.request
import requests
import datetime
import discord
print("20244021, 컴퓨터공학과, 김성준")


# 날씨함수정의

def weather():
    # 서울날씨사이트조회
    page = urllib.request.urlopen(
        "https://119.seoul.go.kr/asims/wether/selectWetherList.do")
    text = page.read().decode("utf8")

    # 온도
    wheret = text.find("<li class=\"t\"><strong>")
    TS = wheret + 22
    TE = TS + 5
    T = text[TS: TE]

    TS15 = wheret + 27
    TE15 = TS15 + 1
    T15 = text[TS15: TE15]
    if T15 == "&":
        TE = TS + 5
        T = text[TS: TE]

    TS14 = wheret + 26
    TE14 = TS14 + 1
    T14 = text[TS14: TE14]
    if T14 == "&":
        TE = TS + 4
        T = text[TS: TE]

    TS13 = wheret + 25
    TE13 = TS13 + 1
    T13 = text[TS13: TE13]
    if T13 == "&":
        TE = TS + 3
        T = text[TS: TE]

    TS12 = wheret + 24
    TE12 = TS12 + 1
    T12 = text[TS12: TE12]
    if T12 == "&":
        TE = TS + 2
        T = text[TS: TE]

    TS11 = wheret + 23
    TE11 = TS11 + 1
    T11 = text[TS11: TE11]
    if T11 == "&":
        TE = TS + 1
        T = text[TS: TE]

    # 습도
    wherew = text.find("습도 <strong>")
    WS = wherew + 11
    WE = WS + 4
    W = text[WS: WE]

    WS5 = wherew + 16
    WE5 = WS5 + 1
    W5 = text[WS5: WE5]
    if W5 == "<":
        WE = WS + 5
        W = text[WS: WE]

    WS4 = wherew + 15
    WE4 = WS4 + 1
    W4 = text[WS4: WE4]
    if W4 == "<":
        WE = WS + 4
        W = text[WS: WE]

    WS3 = wherew + 14
    WE3 = WS3 + 1
    W3 = text[WS3: WE3]
    if W3 == "<":
        WE = WS + 3
        W = text[WS: WE]

    WS2 = wherew + 13
    WE2 = WS2 + 1
    W2 = text[WS2: WE2]
    if W2 == "<":
        WE = WS + 2
        W = text[WS: WE]

    WS1 = wherew + 12
    WE1 = WS1 + 1
    W1 = text[WS1: WE1]
    if W1 == "<":
        WE = WS + 1
        W = text[WS: WE]

    # 강수량(시간)
    whererh = text.find("<li>강수량 1시간 <span class=\"txt_cold\"><strong>")
    RHS = whererh + 43
    RHE = RHS + 4
    RH = text[RHS: RHE]

    RHS4 = whererh + 47
    RHE4 = RHS4 + 1
    RH4 = text[RHS4: RHE4]
    if RH4 == "<":
        RHE = RHS + 4
        RH = text[RHS: RHE]

    RHS3 = whererh + 46
    RHE3 = RHS3 + 1
    RH3 = text[RHS3: RHE3]
    if RH3 == "<":
        RHE = RHS + 3
        RH = text[RHS: RHE]

    RHS2 = whererh + 45
    RHE2 = RHS2 + 1
    RH2 = text[RHS2: RHE2]
    if RH2 == "<":
        RHE = RHS + 2
        RH = text[RHS: RHE]

    RHS1 = whererh + 44
    RHE1 = RHS1 + 1
    RH1 = text[RHS1: RHE1]
    if RH1 == "<":
        RHE = RHS + 1
        RH = text[RHS: RHE]

    # 강수량(하루)
    whererd = text.find("<li>강수량 1일 <span class=\"txt_cold\"><strong>")
    RDS = whererd + 42
    RDE = RDS + 4
    RD = text[RDS: RDE]

    RDS4 = whererd + 46
    RDE4 = RDS4 + 1
    RD4 = text[RDS4: RDE4]
    if RD4 == "<":
        RDE = RDS + 4
        RD = text[RDS: RDE]

    RDS3 = whererd + 45
    RDE3 = RDS3 + 1
    RD3 = text[RDS3: RDE3]
    if RD3 == "<":
        RDE = RDS + 3
        RD = text[RDS: RDE]

    RDS2 = whererd + 44
    RDE2 = RDS2 + 1
    RD2 = text[RDS2: RDE2]
    if RD2 == "<":
        RDE = RDS + 2
        RD = text[RDS: RDE]

    RDS1 = whererd + 43
    RDE1 = RDS1 + 1
    RD1 = text[RDS1: RDE1]
    if RD1 == "<":
        RDE = RDS + 1
        RD = text[RDS: RDE]

    # 기상상태
    wherec = text.find("<li>강수량 1일 <span class=\"txt_cold\"><strong>")
    CS = wherec + 85
    CE = CS + 6
    CD = text[CS: CE]

    CS11 = wherec + 86
    CE11 = CS11 + 1
    CD11 = text[CS11: CE11]
    if CD11 == ">":
        CS = wherec + 87
        CE = CS + 6
        CD = text[CS: CE]

    CS12 = wherec + 87
    CE12 = CS12 + 1
    CD12 = text[CS12: CE12]
    if CD12 == ">":
        CS = wherec + 88
        CE = CS + 6
        CD = text[CS: CE]

    CS13 = wherec + 88
    CE13 = CS13 + 1
    CD13 = text[CS13: CE13]
    if CD13 == ">":
        CS = wherec + 89
        CE = CS + 6
        CD = text[CS: CE]

    CS14 = wherec + 89
    CE14 = CS13 + 1
    CD14 = text[CS14: CE14]
    if CD14 == ">":
        CS = wherec + 90
        CE = CS + 6
        CD = text[CS: CE]

    CS8 = wherec + 93
    CE8 = CS8 + 1
    CD8 = text[CS8: CE8]
    if CD8 == "<":
        CE = CS + 8
        CD = text[CS: CE]

    CS7 = wherec + 92
    CE7 = CS7 + 1
    CD7 = text[CS7: CE7]
    if CD7 == "<":
        CE = CS + 7
        CD = text[CS: CE]

    CS6 = wherec + 91
    CE6 = CS6 + 1
    CD6 = text[CS6: CE6]
    if CD6 == "<":
        CE = CS + 6
        CD = text[CS: CE]

    CS5 = wherec + 90
    CE5 = CS5 + 1
    CD5 = text[CS5: CE5]
    if CD5 == "<":
        CE = CS + 5
        CD = text[CS: CE]

    CS4 = wherec + 89
    CE4 = CS4 + 1
    CD4 = text[CS4: CE4]
    if CD4 == "<":
        CE = CS + 4
        CD = text[CS: CE]

    CS3 = wherec + 88
    CE3 = CS3 + 1
    CD3 = text[CS3: CE3]
    if CD3 == "<":
        CE = CS + 3
        CD = text[CS: CE]

    CS2 = wherec + 87
    CE2 = CS2 + 1
    CD2 = text[CS2: CE2]
    if CD2 == "<":
        CE = CS + 2
        CD = text[CS: CE]

    CS1 = wherec + 86
    CE1 = CS1 + 1
    CD1 = text[CS1: CE1]
    if CD1 == "<":
        CE = CS + 1
        CD = text[CS: CE]
    return ("서울날씨 " + T + "℃ " + " 습도 " + W + "% " + "시간당 강수량 " + RH + "mm " + "하루 총 강수량 " + RD + "mm " + CD)


discord_url = 'https://discord.com/api/webhooks/1225310655695814746/LlkNFLAt3Y1oDrsD2EEMvn1DMyd0bj9JRJ1y-pE_EaVz6sNdjKPwfAeD_IMC6TUzuPoo'

# 디스코드 채널로 메세지 전송


def discord_send_message(text):
    now = datetime.datetime.now()
    message = {"content": f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {str(text)}"}
    requests.post(discord_url, data=message)
    return (message)


msg = weather()
loop = 0

# 1시간동안 5분마다 반복전송
while loop < 12:
    discord_send_message(msg)
    time.sleep(300)
    loop = loop + 1
