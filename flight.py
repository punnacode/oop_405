from add_on import Package
from booking import Booking
from datetime import date

class Flight:
    def __init__(self,name,flight_duration,international,depart_airport,arrive_airport):
        self._name = name
        self._flight_duration = flight_duration
        self._international = international
        self._depart_airport = depart_airport
        self._arrive_airport = arrive_airport
        
    
    @property
    def name(self):
        return self._name
    @property
    def flight_duration(self):
        return self._flight_duration
    @property
    def international(self):
        return self._international
    @property
    def depart_airport(self):
        return self._depart_airport
    @property
    def arrive_airport(self):
        return self._arrive_airport

class FlightInstance(Flight):
    day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    def __init__(self,name,flight_duration,international,depart_airport,arrive_airport,date_depart,time_arrive,time_depart,aircraft,price):
        super().__init__(name,flight_duration,international,depart_airport,arrive_airport)
        self._date_depart = date_depart
        self._time_arrive = time_arrive
        self._time_depart = time_depart
        self._aircraft = aircraft
        self._price = price
        self._booking = []
        self.day_in_month

    @property
    def date_depart(self):
        return self._date_depart
    
    @date_depart.setter
    def date_depart(self, new_date_depart):
        if isinstance(new_date_depart, str):
            self._date_depart = new_date_depart
    @property
    def time_arrive(self):
        return self._time_arrive
    @time_arrive.setter
    def time_arrive(self, new_time_arrive):
        if isinstance(new_time_arrive, str):
            self._time_arrive = new_time_arrive
    @property
    def time_depart(self):
        return self._time_depart
    @time_depart.setter
    def time_depart(self, new_time_depart):
        if isinstance(new_time_depart, str):
            self._time_depart = new_time_depart
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float):
            self._price = new_price
    @property
    def aircraft(self):
        return self._aircraft
    @aircraft.setter
    def aircraft(self, new_aircraft):
        if isinstance(new_aircraft, str):
            self._aircraft = new_aircraft
    @property
    def booking(self):
        return self._booking

    def get_price(self):
        days = self.date_diff(str(date.today()),self.date_depart)
        if days > 30:
            return self.price
        else:
            return round(float(self.price*(1.02**(31-days))), 2)
        
    def sum_price(self,package):
        if isinstance(package,Package):
            return round(package.price + self.get_price(),2)
        else:
            raise TypeError("Parameter type not correct")

    def get_seatbook_list(self):
        seat_book_list = []
        for booking in self._booking:
            if booking.payment.payment_status.value == 3:
                for seatbook in booking.seat_book:
                    if seatbook not in seat_book_list:
                        seat_book_list.append(seatbook)
        return seat_book_list

    def create_booking(self,flight_instance,package,adult,child,infant):
        if isinstance(flight_instance,FlightInstance) and isinstance(package,Package) and isinstance(adult,int) and isinstance(child,int) and isinstance(infant,int):
            booking = Booking(flight_instance,package,adult,child,infant)
            payment = booking.create_payment()
            #payment.add_booking(booking)
            self._booking.append(booking)
        else:
            raise TypeError("please check payment status")
        return booking.id
        
    def get_booking(self,booking_id):
        for booking in self._booking:
            if booking.id == booking_id:
                return booking
    
    ## Date difference system
    def is_leap(self,year):
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            return 29
        else:
            return 28

    def day_of_year(self,day,month,year):
        self.day_in_month[2] = self.is_leap(year)
        num = sum(self.day_in_month[x] for x in range(month)) + day
        return num

    def day_in_year(self,year):
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            return 366
        else:
            return 365

    def month_date_call(self,month,year):
        self.day_in_month[2] = self.is_leap(year)
        return self.day_in_month[month]

    def date_diff(self,date1,date2):
        date_1 = [int(date) for date in date1.split("-")]
        date_2 = [int(date) for date in date2.split("-")]
        if date_1[1] > 12 or date_1[1] < 1 or date_2[1] > 12 or date_2[1] < 1:
            raise ValueError("Incorrect Month Value")
        if date_1[2] > self.month_date_call(date_1[1],date_1[0]) or date_2[2] > self.month_date_call(date_2[1],date_2[0]):
            raise ValueError("Incorrect Day Value")
        year_list = sum(self.day_in_year(year) for year in range(date_1[0],date_2[0])) + self.day_of_year(date_2[2],date_2[1],date_2[0]) - self.day_of_year(date_1[2],date_1[1],date_1[0]) + 1
        return(year_list)

   
   



