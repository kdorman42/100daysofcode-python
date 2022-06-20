# ---- API Requests ---- #

# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# location = (latitude, longitude)
# print(location)

# # Response codes
# 1XX = hold on
# 2XX = here you go
# 3XX = go away
# 4XX = you screwed up
# 5XX = i screwed up


# ---- API Parameters ----#
# Sunrise Sunset times API

import requests

MY_LAT = 30.267153
MY_LONG = -97.743057

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
# Returns a 404 without latitude and longitude specified

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)


# Day 34
# def greeting(name: str) -> str:  # declare variable type with : and return type with ->
#     return 'Hello' + name