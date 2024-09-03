from datetime import datetime
import random

flightsList = []  # Global list to store all flights, should be in Flight class but as a common list for all instances not created with each one
personIDs = []  # All persons' IDs in system should be here to ensure uniqness
flightNums = []  # All flights' numbers in system should be here to ensure uniqness
airportsList = []  # Global list to store all airports, should be in Airport class but as a common list for all instances not created with each one


class Booking:  # Class that stores data of each new Booking, used in Custmore class
    def __init__(self):
        self.tripToBook = -2
        self.depAirport = -2
        self.arrAirport = -2
        self.meal = "-"
        self.extraLuggage = 0
        self.firstClass = False

    def mainBooking(self):
        print("Fligths\n")
        for index in range(len(flightsList)):
            print("Flight " + str(index + 1))
            print("Time: " + str(flightsList[index].depTime))
            print("Price: " + str(flightsList[index].price))
            print("Airline: " + str(flightsList[index].airline))
            print()

        self.tripToBook = int(
            input("Choose the suitable one for you, type 0 if not available: "))
        if (self.tripToBook < 1):
            print("Come soon to check if your desired trip is available")
            self.tripToBook = -2
            return
        elif (self.tripToBook <= len(flightsList)):
            self.tripToBook = flightsList[self.tripToBook - 1]
        else:
            print("Wrong input, please try again later")
            self.tripToBook = -2
            return

        print("Airports\n")
        for index in range(len(airportsList)):
            print("Airport " + str(index + 1))
            print("Name: " + str(airportsList[index].name))
            print("Location: " + str(airportsList[index].location))
            print()

        self.depAirport = int(
            input("Choose the suitable one for you, type 0 if not available: "))
        if (self.depAirport < 1):
            print("Come soon to check if your desired trip is available")
            self.tripToBook = -2
            self.depAirport = -2
            return
        elif (self.depAirport <= len(airportsList)):
            self.depAirport = airportsList[self.depAirport - 1]
        else:
            print("Wrong input, please try again later")
            self.tripToBook = -2
            self.depAirport = -2
            return

        self.arrAirport = int(
            input("Choose the arrival airport, type 0 if not available or type -1 if its a one way trip: "))
        if (self.arrAirport == 0):
            print("Come soon to check if your desired trip is available")
            self.tripToBook = -2
            self.depAirport = -2
            self.arrAirport = -2
            return
        elif (self.arrAirport > 0 and self.arrAirport <= len(airportsList)):
            self.arrAirport = airportsList[self.arrAirport - 1]
        elif (self.arrAirport < 0):
            self.arrAirport = -2
        else:
            print("Wrong input, please try again later")
            self.tripToBook = -2
            self.depAirport = -2
            self.arrAirport = -2
            return

    def mealBooking(self):
        self.meal = int(input(
            "Choose your meal:\n1.vegetarian\n2.Meat\n3.Chicken\n4.Cancel meal\nYour Choic: "))
        match self.meal:
            case 1:
                self.meal = "Vegetarian"
            case 2:
                self.meal = "Meat"
            case 3:
                self.meal = "Chicken"
            case _:
                self.meal = "No meal"

    def extraServiceBooking(self):
        self.extraLuggage = int(input(
            "IF you need extra luggage, Enter the needed number(if not please enter 0): "))

        self.firstClass = input(
            "Make it first class (enter y to confirm, n to cncel): ").lower()
        match self.firstClass:
            case "y":
                self.firstClass = True
            case _:
                self.firstClass = False


class Airport:  # class to store airport data
    def __init__(self, name: str, location: str, ):
        self.name = name
        self.location = location
        self.id = random.randint(1000, 9999)
        airportsList.append(self)


class Flight:  # class to store each flight data
    def __init__(self, depTime: datetime, arrTime: datetime, price: float, airline: str):
        self.flightNum = random.randint(1000, 9999)
        while (self.flightNum in flightNums):
            self.flightNum = random.randint(1000, 9999)
        flightNums.append(self.flightNum)
        self.depTime = depTime
        self.arrTime = arrTime
        self.price = price
        self.airline = airline


class Person:  # parent class to make all persons of system: Custmore and Clerk
    def __init__(self, username: str, password: int, email: str):
        self.username = username
        self.password = password
        self.email = email
        self.loggedin = False
        self.id = random.randint(1000, 9999)
        while (self.id in personIDs):
            self.id = random.randint(1000, 9999)
        personIDs.append(self.id)

    def login(self, username, password):
        if (self.username == username and self.password == password):
            print(self.username + " logged in")
            self.loggedin = True
        else:
            print("Access Denied")

    def logout(self):
        self.loggedin = False
        print(self.username + " logged out")


class Custmore(Person):  # main class of system. afterlogging in, it can book tickets
    def __init__(self, username: str, password: int, email: str, passportNum: str):
        Person.__init__(self, username, password, email)
        self.passportNum = passportNum
        self.flights = []

    def bookFlight(self):
        if (self.loggedin):
            self.flights.append(Booking())
            self.flights[-1].mainBooking()
            if (self.flights[-1].depAirport != -2):
                self.flights[-1].mealBooking()
                self.flights[-1].extraServiceBooking()

                print("The flight will be booked with the following data: ")
                print("name: " + self.username + "\nEmail address: " +
                      self.email + "\nPassport number: " + self.passportNum)

                print("Flight booked successfully")
                print(
                    "******************************Your booking data******************************")
                print("name: " + self.username + "\tEmail address: " +
                      self.email + "\tPassport number: " + self.passportNum)
                print("Flight number: " + str(self.flights[-1].tripToBook.flightNum) +
                      " on " + self.flights[-1].tripToBook.airline + " airlines")
                print("from " + self.flights[-1].depAirport.name +
                      " airport, " + self.flights[-1].depAirport.location)
                print("Meal: " + self.flights[-1].meal +
                      "\tFirst Class: " + str(self.flights[-1].firstClass))
            else:
                self.flights.pop()
        else:
            print("Access Denied")


class Clerk(Person):  # system admin how creates flights
    def __init__(self, username: str, password: int, email: str):
        super().__init__(username, password, email)

    def addFlight(self, depTime: datetime, arrTime: datetime, price: float, airline: str):
        if (self.loggedin):
            flight = Flight(depTime, arrTime, price, airline)
            flightsList.append(flight)
            print("Added flight successfully by " + self.username)
        else:
            print("Access Denied.")


# system use
johnKendyAirPort = Airport("John Kendy", "Newyork")
kingKhaledAirPort = Airport("King Khaled", "Riyadh")
borgALarabAirPort = Airport("Borg ALarab", "Alexandria")

clerk1 = Clerk("Ahmed", 1234, "ahmed@gmail.com")
clerk1.login("Ahmed", 1234)

clerk1.addFlight(datetime(2024, 10, 1, 2), datetime(
    2024, 10, 1, 5), 200, "airKings")
clerk1.addFlight(datetime(2024, 11, 1, 2), datetime(
    2024, 11, 1, 5), 150, "flyKings")
clerk1.addFlight(datetime(2024, 12, 1, 2), datetime(
    2024, 12, 1, 5), 250, "airQueens")

clerk1.logout()

print("---------------------------------------------")

custmore1 = Custmore("John", 1212, "john@gmail.com", "8888ab")
custmore1.login("John", 1212)
custmore1.bookFlight()
