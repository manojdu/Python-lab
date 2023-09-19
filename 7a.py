#By using the concept of inheritance write a python program to find the area of triangle, circle and rectangle.

import math

class shape:
  def __init__(self, name):
    self.name = name

  def get_area(self):
    pass

class triangle(shape):
  def __init__(self, base, height):
    super().__init__("Triangle")
    self.base = base
    self.height = height

  def get_area(self):
    return 0.5 * self.base * self.height

class circle(shape):
  def __init__(self, radius):
    super().__init__("Circle")
    self.radius = radius

  def get_area(self):
    return math.pi * self.radius ** 2

class rectangle(shape):
  def __init__(self, length, width):
    super().__init__("Rectangle")
    self.length = length
    self.width = width

  def get_area(self):
    return self.length * self.width

tri = triangle(6, 8)
cir = circle(5)
rec = rectangle(4,10)

print("Area of ", tri.name, tri.get_area())
print("Area of ", cir.name, cir.get_area())
print("Area of ", rec.name, rec.get_area())
