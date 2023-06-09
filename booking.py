from ticket import Ticket
from aircraft import SeatBook
from payment import Payment,PaymentStatus

class Booking:
    ID = 1

    def __init__(self,flight_instance,package,adult,child,infant):
        self._id = Booking.ID
        self._flight = flight_instance
        self._package = package
        self._adult_num = adult
        self._kid_num = child
        self._infant_num = infant
        self._phone_number = None 
        self._email = None
        self._payment = None
        self._passenger_list = []
        self._ticket = []
        self._seat_book = []
        
        Booking.ID +=1

    @property
    def id(self):
        return self._id
    @property
    def flight(self):
        return self._flight 
    @property
    def flight_international_status(self):
        return self._flight.international
    @property
    def package(self):
        return self._package 
    @property
    def total_passenger_num(self):
        return self._adult_num+self._kid_num+self._infant_num
    @property
    def passenger_list(self):
        return self._passenger_list
    @property
    def get_adult_list(self):
        adult_list = []
        for passenger in self._passenger_list:
            if passenger.type == "ADULT":
                adult_list.append(str(passenger.name+" "+passenger.last_name))
        return adult_list
    @property
    def get_kid_list(self):
        kid_list = []
        for passenger in self._passenger_list:
            if passenger.type == "CHILD":
                kid_list.append(str(passenger.name+" "+passenger.last_name))
        return kid_list
    @property
    def get_infant_list(self):
        INFANT_list = []
        for passenger in self._passenger_list:
            if passenger.type == "INFANT":
                INFANT_list.append(str(passenger.name+" "+passenger.last_name))
        return INFANT_list
    @property
    def payment(self):
        return self._payment
    @payment.setter
    def payment(self,new_payment):
        self._payment = new_payment
    @property
    def adult_num(self):
        return self._adult_num
    @property
    def kid_num(self):
        return self._kid_num
    @property
    def infant_num(self):
        return self._infant_num
    @property
    def seat_book(self):
        return self._seat_book
    @property
    def ticket(self):
        return self._ticket
        
    def add_passenger(self,passenger):
        self._passenger_list.append(passenger)
        return self._passenger_list
        
    def main_passenger_info(self,phone_number,email):
        self._phone_number = phone_number
        self._email = email
    
    def create_ticket(self, passenger, seatbook, extraservice, baggage, meal, specialbaggage,specialAssistance):
            self._ticket.append(Ticket(self._flight, passenger, seatbook, extraservice, baggage, meal, specialbaggage,specialAssistance))

    def create_seatbook(self,row,column):
        seat_list = self._flight.aircraft.seat_list
        for seat in seat_list:
            if row == seat.seat_row and column == seat.seat_column:
                seat.seat_type.value
                book_seat = SeatBook(False,row,column,seat.seat_type)
                self._seat_book.append(book_seat)
                return book_seat 

    def search_ticket(self,flight,aircraftseat):
        for i in self.ticket:
            if i.flight == flight and i.aircraft_seat == aircraftseat:
                return i
 

    def flight_sum_price(self):
        adult_price = round(float(self._flight.sum_price(self._package) * self._adult_num),2)
        child_price = round(float(self._flight.sum_price(self._package) * self._kid_num),2)
        infant_price = round(float((self._flight.sum_price(self._package) * self._infant_num)/2),2)
        return [adult_price,child_price,infant_price]
    
    def seat_sum_price(self):
        seat_price_list = []
        for seat in self._seat_book:
            seat_price_list.append(round(float(seat._seat_type.value),2))
        return seat_price_list
    
    def add_on_sum_price(self):
        ticket_list = []
        for ticket in self._ticket:
            addon_price = ticket.sum_price(self._package)
            ticket_price = [0.0]
            if addon_price.get("Bagage") != None:
                ticket_price.append(addon_price.get("Bagage"))
            if addon_price.get("Meal") != None:
                ticket_price.append(addon_price.get("Meal"))
            if addon_price.get("Special Bagage") != None:
                ticket_price.append(addon_price.get("Special Bagage"))
            if addon_price.get("Extra service") != None:
                ticket_price.append(addon_price.get("Extra service"))
            ticket_list.append(round(float(sum(ticket_price)),2))
        return ticket_list
    
    def create_payment(self):
        payment = Payment(self._id,PaymentStatus.WAITING)
        payment.add_booking(self)
        self._payment = payment
        return self._payment

