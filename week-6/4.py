#Task 4. OOP Principles & Custom Classes 
#
# 1. Create a base class Employee with:
#    - Private attribute _salary
#    - Method get_salary()
#    - Method get_role() (returns "Employee")
#
# 2. Create a child class Manager that:
#    - Inherits from Employee
#    - Overrides get_role()
#    - Adds a method get_bonus()
#
# 3. Write a function that:
#    - Accepts a list of Employee objects
#    - Prints each employee’s role and salary


class Employee:
    def get_salary(self):
        return self._salary

    def get_role(self):
        return "employee"


class Manager(Employee):
    def get_role(self):
        return "manager"

    def get_bonus(self):
        return 10000


def total_info(employee_list):
    for i in employee_list:
        print(i.name, "is the", i.get_role(), "with salary", i.get_salary())


e1 = Employee()
e1.name = "Mansur"
e1._salary = 50000

e2 = Employee()
e2.name = "Eskendir"
e2._salary = 45000

m1 = Manager()
m1.name = "Cristina"
m1._salary = 70000

all_employees = [e1, e2, m1]

total_info(all_employees)
