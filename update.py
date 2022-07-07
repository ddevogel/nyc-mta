from datetime import datetime
import json
class Update: 

    stops = json.load(open('data/json/stops.json'))
    stop: str
    arrival: str
    departure: str 

    def __init__(self, stop_id: str, arrival: int, departure: int):
        self.stop = "UNKNOWN" if stop_id not in Update.stops else Update.stops[stop_id]['stop_name']
        self.arrival = datetime.fromtimestamp(arrival).strftime("%m/%d/%Y, %H:%M:%S")
        self.departure = datetime.fromtimestamp(departure).strftime("%m/%d/%Y, %H:%M:%S")

    def __repr__(self):
        return f"arrive {self.stop} at {self.arrival} depart at {self.departure}"
