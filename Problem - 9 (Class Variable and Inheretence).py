# OOP Revision Exercise 9 (Class Variables + Inheritance)
#
# Company Employees
#
# Please define the following classes:
#
# Employee
# -----------------------
# Attributes:
# - name
#
# Class variable:
# - employee_count
#
# Every time an Employee (or any subclass) object is created,
# employee_count should increase by one.
#
#
# Class method:
#
# total_employees()
#
# Returns the total number of employees created.
#
#
# __str__()
#
# "<name>"
#
#
#
# Manager(Employee)
#
# Additional attribute:
# - department
#
#
# Developer(Employee)
#
# Additional attribute:
# - programming_language
#
#
#
# Example:
#
# e1 = Employee("Peter")
# e2 = Manager("Maria", "HR")
# e3 = Developer("John", "Python")
#
# print(Employee.total_employees())
#
#
# Sample output:
#
# 3

#Mod done from my end(Adding Manager And Developer Count as Well)

class Employee:
    employee_count=0

    def __init__(self, name: str):
        self.__name=name
        Employee.employee_count+=1

    @property
    def name(self):
        return self.__name

    @classmethod
    def total_employees(cls):
        return cls.employee_count

    def __str__(self):
        return f"{self.name}"
    
class Manager(Employee):
    mng_count=0
    def __init__(self, name, dept: str):
        super().__init__(name)
        self._dept=dept
        type(self).mng_count+=1

    @classmethod
    def total_employees(cls):
        return cls.mng_count

class Developer(Employee):
    dev_count=0
    def __init__(self, name, lang: str):
        super().__init__(name)
        self._lang=lang
        type(self).dev_count+=1

    @classmethod
    def total_employees(cls):
        return cls.dev_count

def main():
    e1 = Employee("Peter")
    e2 = Manager("Maria", "HR")
    e3 = Developer("John", "Python")

    e4 = Employee("Peat")
    e5 = Manager("May", "HR")
    e6 = Developer("Johny", "Python")


    print(Employee.total_employees())
    print(Manager.total_employees())
    print(Developer.total_employees())

    print(e1)
    print(e2)
    print(e3)

if __name__=="__main__":
    main()