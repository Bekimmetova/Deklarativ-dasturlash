from math import pi

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Misol sifatida foydalanish
circle_example = Circle(5.0)
rectangle_example = Rectangle(4.0, 6.0)

print("Doiraning yuzasi:", circle_example.area())
print("To'rtburchakning yuzasi:", rectangle_example.area())
