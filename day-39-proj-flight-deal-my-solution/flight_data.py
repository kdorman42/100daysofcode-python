from datetime import datetime

CURR = "GBP"

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, raw_data, stop_overs=0, via_city=None):
        flight_info = raw_data["data"][0]
        self.orig_city = flight_info["cityFrom"]
        self.orig_code = flight_info["flyFrom"]
        self.dest_city = flight_info["cityTo"]
        self.dest_code = flight_info["flyTo"]
        depart_datetime_raw = flight_info["route"][0]["local_departure"]
        self.depart_date = datetime.strptime(depart_datetime_raw, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d')
        # self.depart_date = depart_datetime.strftime('%Y-%m-%d')
        return_datetime_raw = flight_info["route"][len(flight_info["route"]) - 1]["local_arrival"]
        self.return_date = datetime.strptime(return_datetime_raw, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d')
        # self.return_date = return_datetime.strftime('%Y-%m-%d')
        self.price = flight_info['price']
        self.currency = 'GBP'
        self.duration = flight_info["nightsInDest"]
        self.stop_overs = stop_overs
        if via_city:
            self.stopover_city = flight_info["route"][0]["cityTo"]



# .strftime('%Y-%m-%d')
# '2022-10-03T12:25:00.000Z'