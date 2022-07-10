from urllib.request import Request, urlopen

from google.transit.gtfs_realtime_pb2 import FeedMessage

class BaseProvider:
    request: Request
    # line: str


    # def __init__(self):
    #     # self.line = line
    #     self.request = Request()

    def get(self, feed):
        url = self.feeds[feed]
        self.request = Request(url)
        self.auth()
        response = urlopen(self.request)
        feed = FeedMessage()
        feed.ParseFromString(response.read())
        return self.format(feed.entity)

    def auth(self):
        pass

    def format(self, entity):
        pass