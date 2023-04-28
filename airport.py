from flight import Flight,FlightInstance
from aircraft import Aircraft
class AirportCatalog:
    def __init__(self):
        self._airport_list = []
    
    @property
    def airport_list(self):
        return self._airport_list
    
    def add_airport(self,airport):
        if isinstance(airport,Airport):
            self._airport_list.append(airport)

    def search_arrive_airport_list(self,origin_airport):
        for i in self.airport_list:
            if i.name == origin_airport:
                return i.get_arrive_airport_list()
            
    def search_date_list(self,origin_airport,destination_airport):
        for i in self.airport_list:
            if i.name == destination_airport:
                arrive_airport = i
                break
        for i in self.airport_list:
            if i.name == origin_airport:
                return i.get_date_list(arrive_airport)
    
    def search_flight_instance_list(self,origin_airport,destination_airport,date_depart):
        for i in self.airport_list:
            if i.name == destination_airport:
                arrive_airport = i
                break
        for i in self.airport_list:
            if i.name == origin_airport:
                return i.get_flight_instance_list(arrive_airport,date_depart)
            
    def search_flight_instance(self,origin_airport,date_depart,flight_name):
        for i in self.airport_list:
            if i.name == origin_airport:
                return i. get_flight_instance(date_depart,flight_name)
            
    def search_airport(self,depart_airport):
        for i in self.airport_list:
            if i.name == depart_airport:
                return i
            
    def search_booking(self,origin_airport,date_depart,flight_name,booking_id):
        for i in self.airport_list:
            if i.name == origin_airport:
                flight_instance = i.get_flight_instance(date_depart,flight_name)
                break
        return flight_instance.get_booking(booking_id)

class Airport:
    def __init__(self,name):
        self._name = name
        self._flight_list = []
        self._flight_instance_list = []

    @property
    def name(self):
        return self._name
    
    @property
    def flight_list(self):
        return self._flight_list
    
    @property
    def flight_instance_list(self):
        return self._flight_instance_list
    
    def get_arrive_airport_list(self):
        arrive_airport_list = []
        for flight in self._flight_list:
            if flight.arrive_airport not in arrive_airport_list:
                arrive_airport_list.append(flight.arrive_airport)
        return arrive_airport_list

    def get_date_list(self,arrive_airport):
        date_list = []
        for flight_instance in self._flight_instance_list:
            if flight_instance.arrive_airport == arrive_airport and flight_instance.date_depart not in date_list:
                date_list.append(flight_instance.date_depart)
        return date_list
    
    def get_flight_instance_list(self,arrive_airport,date_depart):
        flight_instance_list = []
        for flight_instance in self._flight_instance_list:
            if flight_instance.arrive_airport == arrive_airport and flight_instance.date_depart == date_depart and flight_instance not in flight_instance_list:
                flight_instance_list.append(flight_instance)
        return flight_instance_list
    
    def get_flight_instance(self,date_depart,flight_name):
        for flight_instance in self._flight_instance_list:
            if flight_instance.date_depart == date_depart and flight_instance.name == flight_name:
                return flight_instance