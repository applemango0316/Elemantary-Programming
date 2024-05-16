weathergroup = []
temperatures = {}
weather_read = open("weather_record_choose_city.txt", "r", encoding="UTF-8")
for line in weather_read:
    weathergroup.append(line[2:21] + " " + line[23:25] + " " + line[31:33])
for line in weathergroup:
    (day, Time, choose_town, temperature) = line.split()
    temperatures[temperature] = day + " " + Time + " " + choose_town
weather_read.close()
print("가장 높았던 기온부터 순서대로 불러옵니다.")
for each_temperatures in sorted(temperatures.keys(), reverse=True):
    print(each_temperatures + "°C")
    print(temperatures[each_temperatures])
    print("--------------------------")
