from promotion import Promotion
from airport import Airport, System
from aircraft import Aircraft,SeatBook
from flight import Flight, FlightInstance
from booking import Booking

class Adminlist:
    def __init__(self):
        self._admin_list = []
    
    def add_admin(self, admin):
        if isinstance(admin,Admin):
            self._admin_list.append(admin)
    def get_list_admin(self):
        return self._admin_list
    
    def login(self,username,password):
        for i in self._admin_list:
            if username == i.username and password == i.password:
                return i
            
    def check(self,username,password):
        for i in self._admin_list:
            if username == i.username and password == i.password:
                return True
            else:
                return False

class Admin:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password

    def create_flight(self,name,flight_duration,international,depart_airport,arrive_airport,system):
        if isinstance(name,str) and isinstance(flight_duration,int) and isinstance(international,bool) and isinstance(depart_airport,Airport) and isinstance(arrive_airport,Airport) and isinstance(system,System):
            system.flight_list.append(Flight(name,flight_duration,international,depart_airport,arrive_airport))
        else:
            raise TypeError("Parameter type not correct")

    def create_flight_instance(self,depart_airport,flight_name,date_depart,time_depart,time_arrive,aircraft,price,system):
        if isinstance(flight_name,str) and isinstance(date_depart,str) and isinstance(time_arrive,str) and isinstance(time_depart,str) and isinstance(aircraft,Aircraft) and isinstance(price,float) and isinstance(depart_airport,Airport) and isinstance(system,System):
            for f in system._flight_list:
                if f.name == flight_name:
                    flight = f
                    break
            system.flight_instance_list.append(FlightInstance(flight.name,flight.flight_duration,flight.international,flight.depart_airport,flight.arrive_airport,date_depart,time_arrive,time_depart,aircraft,price))
        else:
            raise TypeError("Parameter type not correct")

    def edit_flight_instance(self,flight_instance,edit_date_depart,edit_time_arrive,edit_time_depart,edit_price):
        if isinstance(flight_instance,FlightInstance) and isinstance(edit_date_depart,str) and isinstance(edit_time_arrive,str) and isinstance(edit_time_depart,str) and isinstance(edit_price,float):
            flight_instance.date_depart = edit_date_depart
            flight_instance.time_arrive = edit_time_arrive
            flight_instance.time_depart = edit_time_depart
            flight_instance.price = edit_price
        else:
            raise TypeError("Parameter type not correct")

    def cancel_flight_instance(self,system,flight_instance):
        if isinstance(system,System) and isinstance(flight_instance,FlightInstance):
            system.flight_instance_list.remove(flight_instance)
        else:
            raise TypeError("Parameter type not correct")

    def change_seat(self,booking,seat_row,seat_column,edit_seat_row,edit_seat_column):
        if isinstance(booking,Booking) and isinstance(seat_row,int) and isinstance(seat_column,str) and isinstance(edit_seat_row,int) and isinstance(edit_seat_column,str):
            for seatbook in booking.seat_book:
                if seat_row == seatbook.seat_row and seat_column == seatbook.seat_column:
                    book = seatbook
                    break
            seat_list = booking._flight.aircraft.seat_list
            for i in seat_list:
                if edit_seat_row == i.seat_row and edit_seat_column == i.seat_column:
                    new = SeatBook(False,i.seat_row,i.seat_column,i.seat_type)
                    break
            booking.seat_book.remove(book)
            booking.seat_book.append(new)

            for ticket in booking.ticket:
                if seatbook == ticket.seatbook:
                    tk = ticket
                    break
            tk.seatbook = new
        else:
            raise TypeError("Parameter type not correct")
        
        
    def add_promotion(self,promotion_code,discount,promotioncatalog):
        if isinstance(promotion_code,str) and isinstance(discount,int) :
                promotioncatalog.promotion_list.append(Promotion(promotion_code,discount))
        else:
            raise TypeError("Parameter type is not correct")
