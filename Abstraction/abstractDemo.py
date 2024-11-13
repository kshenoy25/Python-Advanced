from abc import ABC, abstractmethod

class Vehicle(ABC):
    def drive(self):
        print("The vehicle is for driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("The car is starting the engine")

def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()


car = Car()
operate_vehicle(car)
