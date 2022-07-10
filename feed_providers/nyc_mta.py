import os
import json
from feed_providers.base_provider import BaseProvider
from csv_to_json import make_json
from update import Update
class NycMta(BaseProvider) :
    stops = json.load(open('data/newyork/stops.json'))
    lines = json.load(open('data/newyork/trips.json'))
    routes = json.load(open('data/newyork/routes.json'))

    feeds = {
        "metro_north": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/mnr%2Fgtfs-mnr",
        "g": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g",
        "nqrw": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw",
        "big": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
        "ace":"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
        "si":"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-si",
        "l":"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l",
        "bdfm":"https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm",
        "jz": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz"
    }

    @classmethod
    def load(cls):
        dir = 'data/newyork'
        for filename in os.listdir(dir):
            if (filename.endswith(".csv")):
                f = os.path.join(dir, filename)
                make_json(f, f.replace('csv', 'json'))
    
    def feed(self, name):        
        return self.feeds[name]

    def auth(self):
        self.request.add_header("x-api-key", os.environ.get("MTA_KEY"))

    def format(self, entities):
        for entity in entities:
            # alert, id, trip_update, vehicle
            if entity.HasField("trip_update"):
                trip_update = entity.trip_update
                # id = trip_update.trip.trip_id.split("_")[1]
                # if not (id in next):
                #     # print(trip_update)
                #     next.append(id)

                for update in trip_update.stop_time_update:
                    x = Update(update.stop_id, update.arrival.time, update.departure.time)
                    print(f"{id}.{update.stop_id} - {x}")
                # print(entity.trip_update)
                # print(entity)        
