
import datetime
today_year = datetime.datetime.now().year
today_month = datetime.datetime.now().month
today_day = datetime.datetime.now().day

# Air Management System
# Your goal is to build an airplanes traffic management system.

# Your program should rely on four classes: Company, Airplane, Flight and Airport.

# Consider every plane can fly only once per day.

# Here is a description of those classes:



# 0) Company
# Attributes:

# id (str) A two letters code
# name (str)
# planes (List of Plane) Every plane that belong to this airlines

class Company():

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.list_of_planes = []
# 1) Airplane
# Attributes:

# id (int)
# current_location (Airport)
# company (Company) The airlines
# next_flights (List of Flight) Every future flight of the airplane, this list should always be sorted by datetime.
# Methods:

# fly(self, destination)
# location_on_date(self, date) Returns where the plane will be on this date
# available_on_date(self, date, location) 
# Returns True if the plane can fly from this location on this date 
# (it can fly if it is in this location on this date and if it doesn’t already have a flight planned).

class Airplane():
    plane_id = 0

    def __init__(self, current_location, company):
        self.id = Airplane.plane_id
        Airplane.plane_id += 1
        self.current_location = current_location
        self.company = company
        self.next_flights = []
            #still need to sort the flithgs list
    def fly(self, destination):
        print(f" Airplane id {self.id} is flying to {destination.city} ")
        self.current_location = destination

    

    def location_on_date(self, location_on_date):
        """
        date must be a list of day mont and year [DD, MM, YYYY]
        """
        if location_on_date == [today_day, today_month, today_year]:
            return self.current_location
        else:
            for individual_flight in self.next_flights:
                if individual_flight["date of arrival"] == location_on_date:
                    return individual_flight["destination"].city
                
            return "unknow"
                    


    def add_fly (self, fly):
        next_flight = fly.complete_flight
        self.next_flights.append(next_flight)
        



    def available_on_date(self, date_check, location= "unknow"):
        """
        date must be [DD, MM, YYYY], you can chek if the plane is available in an unknow place
        in a certain date putting unknow
        as location
        """
        location_of_the_plane = self.location_on_date(date_check)
        
        if location_of_the_plane == location.city:
            for individual_flight in self.next_flights:
                
                if individual_flight["date of departure"] == date_check:
                    return False
            return True
        else:
            return False


 

# 2) Flight
# Attributes:

# date (datetime.Date)
# destination (Airport) The destination airport.
# origine (Airport) The origine airport.
# plane (Plane)
# id (str) The ID is an encoded string composed of the destination, the airlines code and the date.
# Methods (Those methods are here only to update the rest of the system, 
# for example, to change the location of the plane when he arrives):

# take_off(self)
# land(self)

class Flight():

    def __init__(self, plane, origin , destination, departure_flight_date, arrival_flight_date):
        """
        dates must be put as [DD, MM, YYYY]
        """
        self.plane = plane
        self.origin = origin
        self.destination = destination
        self.departure_flight_date = departure_flight_date
        self. arrival_flight_date = arrival_flight_date
        self.date = datetime.datetime.now()
        self.id = f"{destination}  {plane.company.id}  {self.date.day}  {self.date.month}  {self.date.year}"
        self.complete_flight = {
            "plane": self.plane,
            "origin" : self.origin,
            "destination" : self.destination,
            "date of departure" : self.departure_flight_date,
            "date of arrival" : self.arrival_flight_date,
        }
        

    def take_off(self):
        pass

    def land(self):
        pass






# 3) Airport
# Attributes:

# city (str) The code of the city where the airport is
# planes (List of Airplane) A list of every plane that is currently in this airport
# scheduled_departures (List of Flight) Every future flight from this airport, sorted by date
# scheduled_arrivals (List of Flight) Every future arrival to this airport, sorted by date
# Methods:

# schedule_flight(self, destination, datetime) This method finds when an available airplane
#  from an airline that serve the origine and the destination and schedule a flight for it.

# info(self, start_date, end_date) Display every scheduled flight from start_date to end_date.
# You are free to add any class/method/attribute to your code, be sure to document everything you write.

# Write a small code to test your program.


class Airport():

    def __init__(self, city):
        self.city = city
        self.list_of_airplains = []
        self.scheduled_departures = []
        self.scheduled_arrives = []
    # # need a sorted departures function
    # def __getitem__(self, item):
    #     return self.complete_flight[item]
    
    def add_airplane(self, airplane):
        self.list_of_airplains.append(airplane)

    def schedule_flight(self,plane,  origin, destination, departure_date, arrival_date):
        """
        arrival date and departure date must be [DD, MM, YYYY]
        origin and destination are Airports class
        plane must be Airplane class
        """
        fly_to_schedule = Flight(plane, origin, destination, departure_date, arrival_date)
        #input the fly to the airport of arrival and destination
        origin.add_departure_fly(fly_to_schedule)
        destination.add_arrival_fly(fly_to_schedule)
        #input the fly to the plane
        plane.add_fly(fly_to_schedule)
        # self.scheduled_departures.append(fly_to_schedule.complete_flight)

        
    def add_departure_fly (self, fly):
        next_flight = fly.complete_flight
        self.scheduled_departures.append(next_flight)
        
    def add_arrival_fly (self, fly):
        next_flight = fly.complete_flight
        self.scheduled_arrives.append(next_flight)
        
    
        
        

    def info(self, start_date, end_date):
        """
        dates must be put like [DD, MM, YYYY]
        """
        departures_to_show = []
        arrives_to_show = []
        days_in_between_the_dates = betweenDays(start_date, end_date)
        for i in range(len(days_in_between_the_dates)):
            days_in_between_the_dates[i] = [int(days_in_between_the_dates[i][0]), int(days_in_between_the_dates[i][1]), int(days_in_between_the_dates[i][2]) ]
        # print(days_in_between_the_dates)
        for i in range(len(self.scheduled_arrives)):
            flight = self.scheduled_arrives[i]
            print(flight)
            date_of_arrival = self.scheduled_arrives[i]["date of arrival"]
            date_of_arrival[2] = str(date_of_arrival[2])[1:3]
            for i in range(len(days_in_between_the_dates)):
                if date_of_arrival[0] == days_in_between_the_dates[i][0] and date_of_arrival[1] == days_in_between_the_dates[i][1]:
                    arrives_to_show.append(flight)
        for i in range(len(self.scheduled_departures)):
            flight = self.scheduled_departures[i]
            # print(flight)
            date_of_departure = self.scheduled_departures[i]["date of departure"]
            date_of_departure[2] = str(date_of_departure[2])[1:3]
            for i in range(len(days_in_between_the_dates)):
                if date_of_departure[0] == days_in_between_the_dates[i][0] and date_of_departure[1] == days_in_between_the_dates[i][1]:
                    departures_to_show.append(flight)
        
        return f"Departures in between the dates: \n {departures_to_show} \n \n Arrivals in between the dates: \n {arrives_to_show}"
                
            
            # flight_departure[2] = str(flight_departure[2])[1:3] 
            # print(flight_departure)


# print(str(aeropuerto_argentino.scheduled_departures[0]["date of arrival"][2])[1:3])

        
    def __repr__(self):
        return f"Aeropuerto de {self.city}"



def betweenDays(start_date, end_date): 
    starting_date = datetime.date(start_date[2], start_date[1], start_date[0])
    ending_date = datetime.date(end_date[2], end_date[1], end_date[0])
    difference = (ending_date - starting_date).days
    print(difference, "days")
    list_of_days = []    
    for i in range(difference + 2):
        try: 
            # print(starting_date)
            list_of_days.append(starting_date)
            start_date[0] += 1
            starting_date = datetime.date(start_date[2], start_date[1], start_date[0])
        except:
            try:
                starting_date= datetime.date(start_date[2], (start_date[1]) +1, 1)
                start_date[1] += 1
                start_date[0] = 1
                # print(starting_date)

            except:
                try:
                    starting_date = datetime.date((start_date[2]) + 1, 1, 1)
                    start_date[1] = 1
                    start_date[0] = 1
                    start_date[2] += 1
                    # print(start_date)
                except:
                    print("Something went wrong")
    # print(list_of_days)
    # return list_of_days

    for i in range(len(list_of_days)):
        list_of_days[i] = list_of_days[i].strftime("%D") #changes the datetime elements of the list of days in to string
        list_of_days[i] = [list_of_days[i][3:5], list_of_days[i][0:2], list_of_days[i][6:8]] #transform in something i was using before
    return(list_of_days)
    
    
    
    

    

# calculate = betweenDays([27, 1,1989], [2,2,1989])
# print(betweenDays([30,11,2002], [1,1,2003]))
aeropuerto_argentino = Airport("cordoba")
aeropuerto_de_mallorca = Airport("mallorca")
aeropuerto_de_EEUU = Airport("Washington")
gaston_flights = Company("GF", "Gaston Flights")
developers_insitute = Company("DV", "developing flights")
avion1 = Airplane(aeropuerto_argentino, gaston_flights)
avion2 = Airplane(aeropuerto_de_mallorca, developers_insitute)
avion3 = Airplane(aeropuerto_de_mallorca, gaston_flights)
avion4 = Airplane(aeropuerto_argentino, developers_insitute)


aeropuerto_argentino.schedule_flight(avion1, aeropuerto_argentino, aeropuerto_de_mallorca, [2, 3, 2021], [2, 3, 2021])
aeropuerto_argentino.schedule_flight(avion1, aeropuerto_argentino, aeropuerto_de_EEUU, [1, 3, 2021], [1, 3, 2021])
aeropuerto_de_EEUU.schedule_flight(avion1, aeropuerto_de_EEUU, aeropuerto_de_mallorca, [1, 4, 2021], [2, 4, 2021])
aeropuerto_de_mallorca.schedule_flight(avion2, aeropuerto_de_mallorca, aeropuerto_de_EEUU, [2, 5, 2021], [3, 5, 2021])
aeropuerto_argentino.schedule_flight(avion2, aeropuerto_argentino, aeropuerto_de_mallorca, [1, 1, 2021], [1, 1, 2021])
aeropuerto_de_mallorca.schedule_flight(avion2, aeropuerto_de_mallorca, aeropuerto_de_EEUU, [12, 5, 2021], [12, 5, 2021])
aeropuerto_argentino.schedule_flight(avion3, aeropuerto_argentino, aeropuerto_de_EEUU, [1, 3, 2021], [2, 3, 2021])
aeropuerto_de_EEUU.schedule_flight(avion3, aeropuerto_de_EEUU, aeropuerto_de_mallorca, [2, 3, 2021], [2, 3, 2021])
aeropuerto_de_mallorca.schedule_flight(avion3, aeropuerto_de_mallorca, aeropuerto_argentino, [12, 1, 2021], [12, 1, 2021])
aeropuerto_de_EEUU.schedule_flight(avion4, aeropuerto_de_EEUU, aeropuerto_de_mallorca, [8, 8, 2021], [9, 8, 2021])
aeropuerto_argentino.schedule_flight(avion4, aeropuerto_argentino, aeropuerto_de_EEUU, [2, 3, 2021], [2, 3, 2021])
aeropuerto_argentino.schedule_flight(avion4, aeropuerto_argentino, aeropuerto_de_mallorca, [1, 3, 2021], [1, 3, 2021])

aeropuerto_argentino.schedule_flight(avion1, aeropuerto_argentino, aeropuerto_de_mallorca, [5, 3, 2021], [5, 3, 2021] )
# print(avion1.location_on_date([2, 4, 2021]))
# print(avion1.available_on_date([2, 3, 2021], aeropuerto_de_EEUU))
# print(aeropuerto_argentino.info([11,1,2021], [12,2,2021]))