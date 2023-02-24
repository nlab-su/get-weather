import requests
import time

cur_datetime = time.strftime("%Y%m%d-%H%M%S")
response = "weather-"+cur_datetime+".json"
s_city_name = "Dolgoprudny,RU"
appid = "2bf41ac9bba68c3ca0f588256dfbcc8d"
res = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city_name, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
with open(response, "w") as f:
    f.write(res.text)

# data = res.json()
# print(data)