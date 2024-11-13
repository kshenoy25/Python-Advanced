# parent class

class Car:
    def __init__(self, windows, doors, engine_type):
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type

    def drive(self):
        print(f"The person will drive the {self.engine_type} car")


car1 = Car(4,5,"petrol")
#car1.drive()


class Tesla(Car):
    def __init__(self, windows, doors, engine_type,self_drive):
        super().__init__(windows, doors, engine_type) # calling init from the car parent class
        self.self_drive = self_drive


    def self_driving(self):
        print(f"Tesla supports self driving:{self.self_drive}")


tesla1 = Tesla(4,5,"petrol",self_drive=True)

#print(tesla1.self_driving())
tesla1.self_driving()