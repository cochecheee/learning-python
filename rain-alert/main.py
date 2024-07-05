import requests

LAT = 21.027763
LON = 105.834160
API_KEY = "9d34896e89752ca2d662e03a3ea0eb83"
# https://openweathermap.org/forecast5
URL = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat" : LAT,
    "lon" : LON,
    "appid" : API_KEY,
    "cnt" : 4,
}

response = requests.get(URL,params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for item in weather_data['list']:
    consition_code = item['weather'][0]['id']
    if int(consition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")