import requests
import os
# from pprint import pprint

SHEETY_FLIGHTS_URL = os.environ['SHEETY_FLIGHTS_URL']
SHEETY_FLIGHTS_TOKEN = ['SHEETY_FLIGHTS_TOKEN']


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = SHEETY_FLIGHTS_URL
        self.sheety_token = SHEETY_FLIGHTS_TOKEN
        self.sheety_headers = {
            "Authorization": self.sheety_token
        }
        self.sheet_data = self.get_data()

    def get_data(self):
        r = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        r.raise_for_status()
        sheet_data = r.json()["prices"]
        return sheet_data

    def fill_row(self, row_id, row_code):
        row_endpoint = f"{self.sheety_endpoint}/{row_id}"
        row_data = {
            "price": {
                "iataCode": row_code
            }
        }
        p = requests.put(url=row_endpoint, headers=self.sheety_headers, json=row_data)
        p.raise_for_status()

