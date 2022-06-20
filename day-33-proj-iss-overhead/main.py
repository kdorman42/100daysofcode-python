import requests
from datetime import datetime
import smtplib
import time
import os

MY_LAT = 30.267153
MY_LONG = -97.743057
MY_SMTP = 'smtp.gmail.com'
MY_EMAIL = os.environ['MY_TEST_GMAIL']
MY_PASSWORD = os.environ['TEST_GMAIL_APP_PW']
TO_EMAIL = os.environ['MY_TEST_YMAIL']
SUBJECT = 'Look up!'
MESSAGE = 'The ISS is above you in the sky.'

#Your position is within +5 or -5 degrees of the ISS position.


def is_iss_overhead(my_lat, my_long):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_long - 5 <= iss_longitude <= my_long + 5:
        return True


def is_dark_outside():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    time.sleep(60)
    if is_iss_overhead(MY_LAT, MY_LONG) and is_dark_outside():
        with smtplib.SMTP(MY_SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"{SUBJECT}\n\n{MESSAGE}"
            )


