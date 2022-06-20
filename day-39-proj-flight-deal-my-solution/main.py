#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
notification_manager = NotificationManager()


for row in data_manager.sheet_data:
    if row["iataCode"] == '':
        city_search = FlightSearch().get_city_code(city=row["city"])
        row["iataCode"] = city_search.city_code
        data_manager.fill_row(row_id=row["id"], row_code=row["iataCode"])

for row in data_manager.sheet_data:
    flight_info_raw = FlightSearch().search_prices(dest_code=row["iataCode"])
    if flight_info_raw["_results"] == 0:
        flight_info_raw = FlightSearch().search_prices(dest_code=row["iataCode"], max_stops=2, max_sector_stops=1)
        if flight_info_raw["_results"] == 0:
            continue
        stop_overs = 1
        via_city = True

    flight_info_clean = FlightData(raw_data=flight_info_raw)
    if flight_info_clean.price <= row["lowestPrice"]:
        notification_manager.notify_via_sms(trip=flight_info_clean)

