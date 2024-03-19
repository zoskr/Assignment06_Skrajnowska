class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name, "is eating.")
    def sleep(self):
        print(self.name, "is sleeping.")
        
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sleep(self):
        print(self.name, "sleeps in a nest.")

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        
class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name)
    def eat(self):
        print(self.name, "eats cat food.")

class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)
    def eat(self):
        print(self.name, "eats dog food.")
        
class Eagle(Bird):
    def __init__(self, name):
        super().__init__(name)
    def eat(self):
        print(self.name, "eats eagle food.")


def main():
    john = Fish("John")
    john.eat()
    john.sleep()
    
    joe = Cat("Joe")
    joe.eat()
    joe.sleep()
    
    bob = Dog("Bob")
    bob.eat()
    bob.sleep()
    
    steve = Eagle("Steve")
    steve.eat()
    steve.sleep()
    
main()
        