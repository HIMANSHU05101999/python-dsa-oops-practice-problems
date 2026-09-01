# ============================================================
# OOP EXERCISE 24 — Employee IDs
# ============================================================
#
# Create an Employee class.
#
# Every Employee should automatically receive a unique ID.
#
# Example:
#
#     Employee("Alice")
#     -> ID 1
#
#     Employee("Bob")
#     -> ID 2
#
#     Employee("Charlie")
#     -> ID 3
#
#
# The ID should NOT be supplied to the constructor.
#
# The Employee class itself should keep track of the next
# available ID.
#
#
# Add a class method:
#
#     Employee.total_employees()
#
# which returns the number of Employee objects created.
#
#
# Example:
#
#     Employee("Alice")
#     Employee("Bob")
#     Employee("Charlie")
#
#     Employee.total_employees()
#     -> 3
#
#
# REQUIREMENTS:
#
# - Use a class variable.
# - Use a class method.
# - IDs must automatically increase.
# - Do not use a global variable.
#
#
# THINK ABOUT:
#
# Which information belongs to ONE Employee?
#
# Which information belongs to the Employee CLASS?
#
# ============================================================

class Employee:
    count=0

    def __init__(self,name):
        self.__name=name
        self.__id=Employee.count+1
        Employee.count+=1

    def __str__(self):
        return f"Name: {self.__name} ID: {self.__id}"

    @classmethod
    def total_emp_created(cls):
        return cls.count
    
if __name__=="__main__":
    a=Employee("a")
    b=Employee("b")
    print(a)
    print(b)

    print(Employee.total_emp_created())

    