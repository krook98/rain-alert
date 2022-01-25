import requests


API_KEY = 'baff3d7005600d597c7afd426fc8d8e0'
URL = 'https://api.openweathermap.org/data/2.5/onecall'
LAT = 52.229675
LON = 21.012230


response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&appid={API_KEY}")
response.raise_for_status()
data = response.json()