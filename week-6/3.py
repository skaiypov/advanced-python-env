# Task 3. OOP Principles & Custom Classes
#
# 1. Create a base class Person
#
# 2. Create a child class Student that:
#    - Inherits from Person
#    - Overrides a method
#
# 3. Demonstrate:
#    - Encapsulation
#    - Inheritance
#    - Polymorphism


class Person:
    def greet(self):
        return "Hello, I'm " + self.name


class Student(Person):
    def greet(self):
        return "Hi, my name is " + self.name

p = Person()
p.name = "Mansur"

s = Student()
s.name = "Eskendir"

arr = [p, s]

for person in arr:
    print(person.greet())

#Encapsulation: __age is hidden.

#Inheritance: Person --> Student

#Polymorphism: The greet() method behaves differently.



