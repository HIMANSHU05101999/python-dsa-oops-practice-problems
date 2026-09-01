# ============================================================
# OOP EXERCISE 25 — Employee Registry
# ============================================================
#
# Extend the Employee class from Exercise 24.
#
# The Employee class should maintain a class-level registry
# containing all Employee objects that have been created.
#
#
# Implement these class methods:
#
#     Employee.find_by_id(id)
#
#     Employee.find_by_name(name)
#
#     Employee.total_employees()
#
#
# Example:
#
#     alice = Employee("Alice")
#     bob = Employee("Bob")
#     charlie = Employee("Charlie")
#
#
#     Employee.find_by_id(2)
#     -> returns the Employee object representing Bob
#
#
#     Employee.find_by_name("Charlie")
#     -> returns the Employee object representing Charlie
#
#
#     Employee.find_by_name("David")
#     -> None
#
#
# REQUIREMENTS:
#
# - Use a class variable for the registry.
# - Use class methods.
# - Do not create a separate registry object outside the class.
#
#
# IMPORTANT QUESTION:
#
# Should find_by_name() operate on ONE Employee object,
# or on the Employee class as a whole?
#
# ============================================================

class Employee:
    count=0
    reg=[]

    def __init__(self,name):
        self.__name=name
        Employee.count+=1
        self.__id=Employee.count
        Employee.reg.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f"Name: {self.__name} ID: {self.__id}"

    def __repr__(self):
        return f"Name: {self.__name} ID: {self.__id}"

    @classmethod
    def find_by_id(cls,id):
        for obj in cls.reg:
            if id == obj.id:
                return obj
        return "Not Found"
            
    @classmethod
    def find_by_name(cls,name):
        for nam in cls.reg:
            if name == nam.name:
                return nam
            return "Not Found"
    @classmethod
    def tot_emps(cls):
        return cls.count
    
    @classmethod
    def tot_emp(cls):
        return cls.reg

if __name__=="__main__":
    a=Employee("a")
    b=Employee("b")
    c=Employee("c")
    print(Employee.find_by_id(2))
    print(Employee.find_by_name("a"))
    print(Employee.tot_emp())
    print(Employee.tot_emps())
