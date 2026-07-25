# OOP Revision Exercise 8 (Class Variables & Class Methods)
#
# Employee ID Generator
#
# Please define a class named Employee.
#
# Each employee has:
#
# - name
# - salary
# - employee_id
#
#
# Requirements:
#
# -------------------------
# Class Variable
# -------------------------
#
# The class should maintain a class variable:
#
# next_id
#
# Initially:
#
# next_id = 1
#
# Every time a new Employee object is created:
#
# • employee_id is assigned the current value of next_id
# • next_id increases by one
#
#
# Example:
#
# e1 = Employee("Peter",3000)
# e2 = Employee("Maria",4000)
#
# e1.employee_id -> 1
# e2.employee_id -> 2
#
#
# -------------------------
# Class Method
# -------------------------
#
# Define a class method:
#
# reset_ids()
#
# It should reset next_id back to 1.
#
#
# Example:
#
# Employee.reset_ids()
#
# e3 = Employee("John",5000)
#
# e3.employee_id -> 1
#
#
# -------------------------
# Instance Method
# -------------------------
#
# yearly_salary()
#
# returns salary * 12
#
#
# -------------------------
# __str__()
#
# Format:
#
# "ID <employee_id>: <name>, salary <salary>"
#
#
# Example:
#
# e1 = Employee("Peter",3000)
# e2 = Employee("Maria",4000)
#
# print(e1)
# print(e2)
#
# Employee.reset_ids()
#
# e3 = Employee("John",5000)
#
# print(e3)
#
#
# Sample output:
#
# ID 1: Peter, salary 3000
# ID 2: Maria, salary 4000
# ID 1: John, salary 5000

class Employee:
    next_id=1

    @classmethod
    def reset_ids(cls):
        cls.next_id=1
        return cls.next_id

    def __init__(self, name: str, salary: float):
        self.__name=name
        self.__salary=salary
        self.__id=Employee.next_id
        Employee.next_id+=1

    def yearly_salary(self):
        return self.__salary*12

    def __str__(self):
        return f"ID {self.__id}: {self.__name}, salary {self.__salary}"

def main():
    e1 = Employee("Peter",3000)
    e2 = Employee("Maria",4000)

    print(e1)
    print(e2)

    Employee.reset_ids()

    e3 = Employee("John",5000)

    print(e3)
if __name__=="__main__":
    main()