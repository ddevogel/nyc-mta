from email import header
from urllib.request import Request, urlopen
from google.transit import gtfs_realtime_pb2
import os
from update import Update


feed = gtfs_realtime_pb2.FeedMessage()
req = Request('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace')
req.add_header('x-api-key', os.environ.get('MTA_KEY'))
response = urlopen(req)
feed.ParseFromString(response.read())
for entity in feed.entity:
    if entity.HasField('trip_update'):
        print(entity.trip_update.trip)

        for update in entity.trip_update.stop_time_update:
            x = Update(update.stop_id, update.arrival.time, update.departure.time)
            print(x)
        # print(entity.trip_update)
        # print(entity)