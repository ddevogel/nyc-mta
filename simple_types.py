from google.transit.gtfs_realtime_pb2 import FeedEntity, VehiclePosition, TripUpdate, TripDescriptor

class Trip:
    route_id: int
    direction_id: int
    start_time: str

    def __init__(self, trip: TripDescriptor):
        self.route_id = trip.route_id
        self.direction_id = trip.direction_id
        self.start_time = trip.start_time

 
class StopUpdate:
    stop_sequence: int
    stop_id: int
    arrival: int
    departure: int
    # vehicle_id: int
    # time: int

    def __init__(self, update : TripUpdate.StopTimeUpdate):
        self.stop_id = update.stop_id
        self.stop_sequence = update.stop_sequence
        self.arrival = update.arrival.time
        self.departure = update.departure.time

class TripUpdates:
    trip: Trip
    vehicle_id: str
    timestamp: int
    updates: list[StopUpdate]

    def __init__(self, update : TripUpdate):
        update = update.trip_update
        self.trip = Trip(update.trip)
        self.vehicle_id = update.vehicle.id
        self.timestamp = update.timestamp
        self.updates = list[StopUpdate]()
        
        for u in update.stop_time_update:
            self.updates.append(StopUpdate(u))


class Position:
    latitude : float
    longitude: float
    bearing: float

    def __init__(self, position: VehiclePosition ):
        self.latitude = position.latitude
        self.longitude = position.longitude
        self.bearing = position.bearing

class Vehicle:
    id: str
    position: Position
    trip: Trip
    current_stop_sequence: int
    occupancy_percentage: int

    def __init__(self, entity: FeedEntity):
        vehicle = entity.vehicle
        self.id = entity.id
        self.position = Position(vehicle.position)
        self.trip = Trip(vehicle.trip)
        self.current_stop_sequence = vehicle.current_stop_sequence
        self.occupancy_percentage = vehicle.occupancy_percentage



# trip {
#   trip_id: "51918601"
#   start_time: "13:20:00"
#   start_date: "20220710"
#   route_id: "31"
#   direction_id: 1
# }
# stop_time_update {
#   stop_sequence: 1
#   departure {
#     time: 1657473634
#   }
#   stop_id: "18511"
# }
# stop_time_update {
#   stop_sequence: 2
#   arrival {
#     time: 1657473766
#   }
#   departure {
#     time: 1657473766
#   }
#   stop_id: "1722"
# }
# stop_time_update {
#   stop_sequence: 3
#   arrival {
#     time: 1657473802
#   }
#   departure {
#     time: 1657473802
#   }
#   stop_id: "1723"
# }
# stop_time_update {
#   stop_sequence: 4
#   arrival {
#     time: 1657473833
#   }
#   departure {
#     time: 1657473833
#   }
#   stop_id: "1724"
# }
# stop_time_update {
#   stop_sequence: 5
#   arrival {
#     time: 1657473888
#   }
#   departure {
#     time: 1657473888
#   }
#   stop_id: "1725"
# }
# stop_time_update {
#   stop_sequence: 6
#   arrival {
#     time: 1657473915
#   }
#   departure {
#     time: 1657473915
#   }
#   stop_id: "1726"
# }
# stop_time_update {
#   stop_sequence: 7
#   arrival {
#     time: 1657473995
#   }
#   departure {
#     time: 1657473995
#   }
#   stop_id: "1728"
# }
# stop_time_update {
#   stop_sequence: 8
#   arrival {
#     time: 1657474053
#   }
#   departure {
#     time: 1657474053
#   }
#   stop_id: "1730"
# }
# stop_time_update {
#   stop_sequence: 9
#   arrival {
#     time: 1657474126
#   }
#   departure {
#     time: 1657474126
#   }
#   stop_id: "543"
# }
# stop_time_update {
#   stop_sequence: 10
#   arrival {
#     time: 1657474214
#   }
#   departure {
#     time: 1657474214
#   }
#   stop_id: "9406"
# }
# stop_time_update {
#   stop_sequence: 11
#   arrival {
#     time: 1657474264
#   }
#   departure {
#     time: 1657474264
#   }
#   stop_id: "545"
# }
# stop_time_update {
#   stop_sequence: 12
#   arrival {
#     time: 1657474326
#   }
#   departure {
#     time: 1657474326
#   }
#   stop_id: "546"
# }
# stop_time_update {
#   stop_sequence: 13
#   arrival {
#     time: 1657474378
#   }
#   departure {
#     time: 1657474378
#   }
#   stop_id: "11522"
# }
# stop_time_update {
#   stop_sequence: 14
#   arrival {
#     time: 1657474433
#   }
#   departure {
#     time: 1657474433
#   }
#   stop_id: "547"
# }
# stop_time_update {
#   stop_sequence: 15
#   arrival {
#     time: 1657474526
#   }
#   stop_id: "875"
# }
# vehicle {
#   id: "y1644"
# }
# timestamp: 1657471570