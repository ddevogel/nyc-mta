from typing import List
# select json_group_object(route_id, 
#   json_object(
#       'id', route_id, 
#       'short_name', route_short_name, 
#       'long_name', route_long_name, 
#       'description', route_desc, 
#       'url', route_url, 
#       'color', route_color)
#   ) as json_result 
# from  routes 
class Route:
    id: str
    short_name: str
    long_name: str
    description: str
    url: str

    def __init__(self, id: str, short_name: str, long_name: str, description: str, url: str):
        self.id = id
        self.short_name = short_name
        self.long_name = long_name
        self. description = description
        self.url = url

class Routes:
    list: List[Route] = list()