class Human:
    def __init__(self,name):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passenger = []

    def add_passenger(self,human):
        self.passenger.append(human)

    def print_passenger_names(self):
        if self.passenger != []:
            print(f"Names of {self.brand} passenger: ")

            for passenger in self.passenger:
                print(passenger.name)

        else:
           print(f"There are no passengers in {self.brand}")


vlad = Human("Vlad")
mary = Human("Mary")

car = Auto("Mercedes")

car.add_passenger(vlad)
car.add_passenger(mary)
car.print_passenger_names()



