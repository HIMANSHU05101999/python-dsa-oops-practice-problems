# OOP Revision Exercise 5 (Hard)
#
# Employee Management System
#
# Please define:
#
# class Employee
#
# Constructor:
# - name
# - salary
#
# Methods:
#
# yearly_salary()
#
# __str__()
#
# Format:
#
# "<name>, salary <salary>"
#
#
# Define a derived class:
#
# class Manager(Employee)
#
# Additional constructor argument:
# - bonus
#
# yearly_salary()
#
# Managers receive:
#
# salary * 12 + bonus
#
#
# Define another derived class:
#
# class Developer(Employee)
#
# Additional constructor argument:
# - projects_completed
#
# Developers receive:
#
# salary * 12
# + projects_completed * 1000
#
#
# Example:
#
# e = Employee("Peter", 3000)
# m = Manager("Maria", 5000, 10000)
# d = Developer("John", 4000, 5)
#
# print(e.yearly_salary())
# print(m.yearly_salary())
# print(d.yearly_salary())
#
#
# Sample output:
#
# 36000
# 70000
# 53000

class Employee:
    def __init__(self, name: str, salary: float):
        self.__name=name
        self.__salary=salary

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    def yearly_salary(self):
        return self.__salary*12

    def __str__(self):
        return f"{self.__name}, salary {self.__salary}"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.__bonus=bonus

    def yearly_salary(self):
        return super().yearly_salary()+self.__bonus

class Developer(Employee):
    def __init__(self, name, salary, proj_comp):
        super().__init__(name, salary)
        self.__proj_comp=proj_comp

    def yearly_salary(self):
        return super().yearly_salary()+(self.__proj_comp*1000)

def main():
    e = Employee("Peter", 3000)
    m = Manager("Maria", 5000, 10000)
    d = Developer("John", 4000, 5)

    print(e.yearly_salary())
    print(m.yearly_salary())
    print(d.yearly_salary())
if __name__=="__main__":
    main()