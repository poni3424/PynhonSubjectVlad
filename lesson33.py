class Human:
    def __init__(self,name,job,home,car):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.gladness = 50
        self.satiety = 50
        self.money = 100
class Auto:
    def __init__(self):
        self.brand = 0
        self.strength = 0
        self.consumption = 0
        self.fuel = 0

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:

    def __init__(self,job_list):
        self.job = 0
        self.salary = 0
        self.gladness = 0

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






