import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
import os

ORIG = "LON"
CURR = "GBP"
TEQUILA_AFFIL_ID = os.environ['TEQUILA_AFFIL_ID']
TEQUILA_API_KEY = os.environ['TEQUILA_API_KEY']

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self, stop_overs=0, via_city=''):
        self.location_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.tequila_AffillID = TEQUILA_AFFIL_ID
        self.tequila_api_key = TEQUILA_API_KEY
        self.tequila_headers = {
            "apikey": self.tequila_api_key
        }
        self.city_code = None

    def get_city_code(self, city):
        tequila_body = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1
        }
        r = requests.get(url=self.location_endpoint, headers=self.tequila_headers, params=tequila_body)
        data = r.json()["locations"]
        city_code = data[0]["code"]
        return city_code

    def search_prices(self, dest_code, max_stops=0, max_sector_stops=0):
        today = dt.date.today()
        tomorrow = today + dt.timedelta(days=1)
        six_months = today + relativedelta(months=6)
        search_body = {
            "fly_from": ORIG,
            "fly_to": dest_code,
            "date_from": tomorrow.strftime('%d/%m/%Y'),
            "date_to": six_months.strftime('%d/%m/%Y'),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": CURR,
            "sort": "price",
            "asc": 1,
            "limit": 1,
            "max_stopovers": max_stops,
            "max_sector_stopovers": max_sector_stops
        }
        r = requests.get(url=self.search_endpoint, headers=self.tequila_headers, params=search_body)
        data = r.json()
        return data







