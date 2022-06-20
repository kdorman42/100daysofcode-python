import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
OWM_API_KEY = os.environ['OWM_API_KEY']

twilio_account_sid = os.environ['TWILIO_ACCT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
my_twilio_phone = os.environ['MY_TWILIO_PHONE']
my_verified_phone = os.environ['MY_VERIFIED_PHONE']
message = "Bring an umbrella (ella, ella, ay) ☔️"

weather_params = {
    'appid': OWM_API_KEY,
    'lat': 30.267153,
    'lon': -97.743057,
    'exclude': 'current,minutely,daily,alerts'
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

hourly_forecast = response.json()['hourly'][:12]
hourly_weather = [i["weather"][0]["id"] for i in hourly_forecast if i["weather"][0]["id"] < 700]

if len(hourly_weather) > 0:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(twilio_account_sid, twilio_auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body=message,
        from_=my_twilio_phone,
        to=my_verified_phone
    )

    print(message.status)






