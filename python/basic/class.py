class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

""" 
print(p1.name)
print(p1.age) 
print(p1)
p1.myfunc()
"""


class Student(Person):
  def __init__(self, fname, age,year):
    Person.__init__(self, fname, age)
#     super().__init__(fname, age)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.name, self.age, "to the class of", self.graduationyear)
  pass

x = Student("Mike", 26, 2019)
x.welcome()


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()