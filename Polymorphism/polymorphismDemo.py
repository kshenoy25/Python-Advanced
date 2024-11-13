class Animal:
    def speak(self):
        return "Sound of the animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

def animal_speak(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()

print(cat.speak())
print(dog.speak())
animal_speak(dog)