# ============================================================
# OOP EXERCISE 26 — Employee Inheritance
# ============================================================
#
# Create a base class:
#
#     Employee
#
# Every Employee has:
#
#     name
#     salary
#
#
# Create these subclasses:
#
#     Manager
#     Developer
#     Designer
#
#
# Manager additionally has:
#
#     team_size
#
#
# Developer additionally has:
#
#     programming_language
#
#
# Designer additionally has:
#
#     design_tool
#
#
# Create a function:
#
#     describe_employee(employee)
#
# It should return a description appropriate for the employee's
# actual type.
#
#
# Example:
#
#     Manager("Alice", 80000, 5)
#     -> Alice manages 5 employees
#
#     Developer("Bob", 70000, "Python")
#     -> Bob develops using Python
#
#     Designer("Charlie", 65000, "Figma")
#     -> Charlie designs using Figma
#
#
# REQUIREMENTS:
#
# - Use inheritance.
# - Manager, Developer and Designer must inherit from Employee.
# - Avoid duplicating common Employee attributes.
#
#
# THINK ABOUT:
#
# What should be defined in Employee?
#
# What should only exist in Developer?
#
# ============================================================

class Employee:
    def __init__(self, name, salary):
        self.__name=name
        self.__salary=salary

    def __str__(self):
        return f"{self.__name}"
    
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.__team_size=team_size

    def __str__(self):
        return f"{super().__str__()} manages {self.__team_size}"

class Developer(Employee):
    def __init__(self, name, salary, prog_language):
        super().__init__(name, salary)
        self.__prog_language=prog_language

    def __str__(self):
        return f"{super().__str__()} developes using {self.__prog_language}"

class Designer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.__tool=tool

    def __str__(self):
        return f"{super().__str__()} design using {self.__tool}"

def describe_employee(emp_obj):
    return str(emp_obj)

if __name__=="__main__":
    m=Manager("anc",123,5)
    p=Developer("abc",123,"python")
    d=Designer("adt",123,"Figma")

    print(describe_employee(m))


    