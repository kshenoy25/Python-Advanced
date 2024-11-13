class Shape:
    def area(self):
        return "The area of the figure - "

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


def print_area(shape):
    print(f"the area is {shape.area()}")

rectangle = Rectangle(5, 5)
circle = Circle(3)

print_area(rectangle)
print_area(circle)


