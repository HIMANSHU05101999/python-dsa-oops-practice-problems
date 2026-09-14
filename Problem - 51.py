# ============================================================
# OOP + INHERITANCE EXERCISE 28 — Employee Factory
# ============================================================
#
# Create:
#
#     Employee
#     Manager
#     Developer
#     Designer
#
#
# Add a CLASS METHOD to Employee:
#
#     Employee.from_string(data)
#
#
# The method receives employee information as a string.
#
#
# Example:
#
#     "developer,Alice,70000,Python"
#
# should create a Developer object.
#
#
#     "manager,Bob,80000,5"
#
# should create a Manager object.
#
#
#     "designer,Charlie,65000,Figma"
#
# should create a Designer object.
#
#
# REQUIREMENTS:
#
# - Use inheritance.
# - Use a class method.
# - The class method must determine which subclass to create.
# - Do not manually create the objects outside the method.
#
#
# THINK:
#
# Why does from_string() make sense as a CLASS METHOD rather
# than an instance method?
#
# There is no Employee object yet when the string is received.
#
# ============================================================


class Employee:
    def __init__(self, name, salary):
        self.__name=name
        self.__salary=salary


    def __str__(self):
        return f"Name: {self.__name} Salary: {self.__salary}"

    @classmethod
    def from_string(cls, string):
        ls=string.lower().split(",")
        desig=ls[0]
        name=ls[1]
        sal=float(ls[2])
        extra=ls[3]

        if desig=="developer":
            dev_class=Developer(name, sal, extra)
            return dev_class
        elif desig=="manager":
            mang_class=Manager(name, sal, int(extra))
            return mang_class
        elif desig=="designer":
            des_class=Designer(name, sal, extra)
            return des_class

class Developer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.__tool=tool

    def __str__(self):
        return f"{super().__str__()}, Tool: {self.__tool}"

class Manager(Employee):
    def __init__(self, name, salary, mng_emp):
        super().__init__(name, salary)
        self.__mng_emp=mng_emp

    def __str__(self):
        return f"{super().__str__()}, Manager's Employee: {self.__mng_emp}"

class Designer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.__tool=tool

    def __str__(self):
        return f"{super().__str__()}, Tool: {self.__tool}"


if __name__=="__main__":
    a=Employee.from_string("developer,Alice,70000,Python")
    print(a)
    print(type(a))
    b=Employee.from_string("manager,Bob,80000,5")
    print(b)
    print(type(b))
    c=Employee.from_string("designer,Charlie,65000,Figma")
    print(c)
    print(type(c))
