from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine has started"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle has started"


def start_vehicle(vehicle):
    print(vehicle.start_engine())

car = Car()
motorcycle = Motorcycle()

start_vehicle(car)