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
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def greet(self):
        return "Hello, I'm " + self.name

    def get_age(self):
        return self.__age


class Student(Person):
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    def greet(self):
        return "Hi, I study at " + self.university + " and my name is " + self.name


p1 = Person("Mansur", 19)
s1 = Student("Eskendir", 18, "Astana IT Universiry")

people = [p1, s1]

for person in people:
    print(person.greet())
    print("Age:", person.get_age())
    print()


#Encapsulation: __age is hidden.

#Inheritance: Student > Person.

#Polymorphism: The greet() method behaves differently.



