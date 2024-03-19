import math

class Shape:
    def area(self):
        self.area = 0
    def perim(self):
        self.perim = 0

class Circle(Shape):
    def __init__(self,r):
        self.radius = r
    def area(self):
        self.area = math.pi * (self.radius**2)
        print("A = ",self.area)
    def perim(self):
        self.perim = 2 * math.pi * self.radius
        print("P = ",self.perim)

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area(self):
        self.area = self.width * self.height
        print("A = ",self.area)
    def perim(self):
        self.perim = 2*(self.width+self.height)
        print("P = ",self.perim)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        self.area = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        print("A = ",self.area)
    def perim(self):
        self.perim = self.a + self.b + self.c
        print("P = ",self.perim)

def main():
    shapes = [Circle(2),Rectangle(3, 4),Triangle(5, 6, 7)]
    for i in shapes:
        i.area()
        i.perim()
              
main()
