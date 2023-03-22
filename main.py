import airport,flight

AirportCatalog = airport.AirportCatalog()
AirportA = airport.Airport("AirportA")
AirportCatalog.add_airport(AirportA)
AirportB = airport.Airport("AirportB")
AirportCatalog.add_airport(AirportB)
dd405 = flight.Flight("DD405",90,False,AirportA,AirportB)
AirportA.add_flight(dd405)
dd406 = flight.Flight("DD406",90,False,AirportA,AirportB)
AirportA.add_flight(dd406)
dd405_20230518 = flight.FlightInstance("DD405",90,False,AirportA,AirportB,"2023/05/18","18.30","20.00")
AirportA.add_flight_instance(dd405_20230518)
dd406_20230518 = flight.FlightInstance("DD405",90,False,AirportA,AirportB,"2023/05/18","20.30","22.00")
AirportA.add_flight_instance(dd406_20230518)

airport_list = AirportCatalog.get_list_airport()
for i in airport_list:
    print(i._name)
depart_airport = airport_list[int(input())]

arrive_airport_list = depart_airport.get_arrive_airport_list()
print(arrive_airport_list)