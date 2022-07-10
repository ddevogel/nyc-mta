import os
import json
from feed_providers.base_provider import BaseProvider
from csv_to_json import make_json
from simple_types import Vehicle, TripUpdates

class BosMbta(BaseProvider) :
    stops = json.load(open('data/boston/stops.json'))
    lines = json.load(open('data/boston/lines.json'))
    routes = json.load(open('data/boston/routes.json'))

    @classmethod
    def load(cls):
        dir = 'data/boston'
        for filename in os.listdir(dir):
            if (filename.endswith(".txt")):
                f = os.path.join(dir, filename)
                make_json(f, f.replace('txt', 'json'))

    feeds = {
        "vehicle": "https://cdn.mbta.com/realtime/VehiclePositions.pb",
        "trip": "https://cdn.mbta.com/realtime/TripUpdates.pb"
    }

    def feed(self, name):        
        return self.feeds[name]
    
    def format(self, entities):
        result = list()
        for entity in entities:
            if (entity.HasField("vehicle")):
                result.append(Vehicle(entity))
            elif (entity.HasField("trip_update")):
                result.append(TripUpdates(entity))    
        return result  


