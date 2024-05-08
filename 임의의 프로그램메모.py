from bs4 import BeautifulSoup
import urllib.request
import requests

html = requests.get(
    'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp').text

root = BeautifulSoup(html, 'html.parser')
city = root.find('city')
weather = root.find('wf')
loc = root.find_all('location')
for i in loc:
    print(i.city.get_text())
    d = i.find_all('data')
    for j in d:
        print(j.tmef.string, ':', j.wf.string, ',',
              j.tmn.string, '~', j.tmx.string, '도')


http: // apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst
?serviceKey = S1yrQhETGG4laPYA0hrZNosb12FoetI % 2FDxSfhnFkqxdq5kosBa % 2FTYPV7PLNymkneSfNh3w7AmCeD9RfXTUm7eQ % 3D % 3D & numOfRows = 10 & pageNo = 1
&base_date = 20210628 & base_time = 0600 & nx = 55 & ny = 127
