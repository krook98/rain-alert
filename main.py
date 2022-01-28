import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


API_KEY = os.environ.get('API_KEY')
URL = 'https://api.openweathermap.org/data/2.5/onecall'
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
LAT = 52.229675
LON = 21.012230
EXCLUDE = "current,minutely,daily"

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")


response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude={EXCLUDE}"
                            f"&appid={API_KEY}")
response.raise_for_status()
data = response.json()
weather_slice = data['hourly'][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}

        client = Client(account_sid, auth_token, http_client=proxy_client)

        message = client.messages \
                        .create(
                            body="It's going to rain today. Remember to bring an umbrella ☂.",
                            from_=os.environ.get('NOTIFICATION_NUMBER'),
                            to=PHONE_NUMBER
                        )

        print(message.sid)
        break


