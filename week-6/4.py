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
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus


def print_employee_info(employee_list):
    for emp in employee_list:
        role = emp.get_role()
        salary = emp.get_salary()
        print(emp.name, "is the", role, "with salary", salary)



e1 = Employee("Mansur", 50000)
e2 = Employee("Eskendir", 45000)
m1 = Manager("Cristina", 70000, 10000)

all_employees = [e1, e2, m1]

print_employee_info(all_employees)
