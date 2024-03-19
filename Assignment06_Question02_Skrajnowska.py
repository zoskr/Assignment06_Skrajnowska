import math

class Shape:
    def area(self):
        self.area = 0
    def perim(self):
        self.perim = 0

class Circle(Shape):
    def __init(self,r):
        self.radius = r
    def area(self):
        self.area = math.pi * (self.radius**2)
    def perim(self):
        self.perim = 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area(self):
        self.area = self.width * self.height
    def perim(self):
        self.perim = 2*(self.width+self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        self.area = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def perim(self):
        self.perim = self.a + self.b + self.c


        