# 20244021, 컴퓨터공학과, 김성준
from urllib import request
from pprint import pprint
import json
print("20244021, 컴퓨터공학과, 김성준")

token = 'ZQAAAetVFY8SCwqS0X8ehM6pefGTHyrxvHBRfcOewD9x4gGHstxAYAL7qcSxfmhkNjuKEAofDRB2YibQu6DvmXbJaabNeMrq4gcYiarJ54q4EfYO'


def get_bands():
    url = f'https://openapi.band.us/v2.1/bands?access_token={token}'
    req = request.Request(url)
    res = request.urlopen(req)
    text = res.read().decode("utf8")
    json_dict = json.loads(text)
    return json_dict


pprint(get_bands())
