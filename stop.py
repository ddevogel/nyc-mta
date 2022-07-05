import decimal
from typing import List
# select json_group_object(stop_id, 
#   json_object(
#       'id', stop_id, 
#       'name', stop_name, 
#       'lat', stop_lat, 
#       'long', stop_lon, 
#       'url', stop_url, 
#       'parent', parent_station is null)
#   ) as json_result 
# from stops 

class Stop:
    id: str
    name: str
    lat: decimal
    long: decimal
    url: str
    parent: bool

    def __init__(self, id: str, name: str, lat: decimal, long: decimal, url: str, parent: bool):
        self.id = id
        self.name = name
        self.lat = lat
        self.long = long
        self.url = url
        self.parent = parent

class Stops:
    list: List[Stop] = list()