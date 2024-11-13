class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Subclasses must implement this method.")

class Pet:
    def __init__(self, owner):
        self.owner = owner

class Cat(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} says meow"


# create an object
cat1 = Cat("Fiona", "Kunal")
cat2 = Cat("Billi", "Haley")

print(cat1.speak())
print(cat2.speak())