from urllib.request import Request, urlopen
from google.transit import gtfs_realtime_pb2
import os
from update import Update

# from csv_to_json import make_json
# dir = 'data/csv'
# for filename in os.listdir(dir):
#     f = os.path.join(dir, filename)
#     make_json(f, f.replace('csv', 'json'))

feed = gtfs_realtime_pb2.FeedMessage()
req = Request('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace')
req.add_header('x-api-key', os.environ.get('MTA_KEY'))
response = urlopen(req)
feed.ParseFromString(response.read())
next = list()
for entity in feed.entity:
    if entity.HasField('trip_update'):
        trip_update = entity.trip_update 
        id = trip_update.trip.trip_id.split('_')[1]
        if not(id in next):
            # print(trip_update)
            next.append(id)


            for update in trip_update.stop_time_update:
                x = Update(update.stop_id, update.arrival.time, update.departure.time)
                print(f"{id} - {x}")
        # print(entity.trip_update)
        # print(entity)