import requests


API_KEY = 'baff3d7005600d597c7afd426fc8d8e0'
URL = 'https://api.openweathermap.org/data/2.5/onecall'
LAT = 52.229675
LON = 21.012230
EXCLUDE = "current,minutely,daily"


response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={EXCLUDE}"
                            f"&appid={API_KEY}")
response.raise_for_status()
data = response.json()
weather_slice = data['hourly'][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        print('Bring an umbrella')
        break
