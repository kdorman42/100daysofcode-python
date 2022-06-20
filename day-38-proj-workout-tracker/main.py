import requests
import datetime as dt
import os

nutritionix_app_id = os.environ['NUTRITIONIX_APP_ID']
nutritionix_api_key = os.environ['NUTRITIONIX_API_KEY']

sheety_api_url = os.environ['SHEETY_WORKOUT_URL']
sheety_bearer_token = os.environ['SHEETY_WORKOUT_TOKEN']
USER_GENDER_STR = "female"
USER_WEIGHT_LBS = 155
USER_HEIGHT_IN = 64
USER_AGE_YEARS = 38


def get_workout_data(gender, weight, height, age):

    nutritionix_api_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
    app_user_id = "0"

    nutritionix_headers = {
        "x-app-id": nutritionix_app_id,
        "x-app-key": nutritionix_api_key,
        "x-remote-user-id": app_user_id
    }

    user_query_str = input("What workout did you do today?  ")

    nutritionix_params = {
        "query": user_query_str,
        "gender": gender,
        "weight_kg": weight / 2.205,
        "height_cm": height / 2.54,
        "age": age
    }

    r = requests.post(url=nutritionix_api_url, headers=nutritionix_headers, json=nutritionix_params)
    r.raise_for_status()

    data = r.json()["exercises"][0]
    workout_data = {
        "exercise": data["name"].title(),
        "duration": round(data["duration_min"]),
        "calories": round(data["nf_calories"])
    }
    return workout_data


def insert_record(workout_data):

    now = dt.datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M:%S")

    sheety_headers = {
        "Authorization": sheety_bearer_token
    }

    sheety_params = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": workout_data["exercise"],
            "duration": round(workout_data["duration"]),
            "calories": round(workout_data["calories"])
        }
    }

    r = requests.post(url=sheety_api_url, headers=sheety_headers, json=sheety_params)
    r.raise_for_status()


insert_record(
    get_workout_data(
        USER_GENDER_STR,
        USER_WEIGHT_LBS,
        USER_HEIGHT_IN,
        USER_AGE_YEARS
    )
)

