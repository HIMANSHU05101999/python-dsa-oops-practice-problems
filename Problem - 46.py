# ============================================================
# RECURSION + OOP EXERCISE 23 — Employee Search
# ============================================================
#
# Using the Employee class from the previous exercise,
# write:
#
#     find_employee(employee, name)
#
# It should search the entire employee hierarchy.
#
# If an employee with the given name exists, return the
# actual Employee object.
#
# If no employee is found, return None.
#
#
# Example:
#
#     result = find_employee(sally, "Matthew")
#
#     result.name
#     -> "Matthew"
#
#     result.salary
#     -> 70000
#
#
# If the employee does not exist:
#
#     find_employee(sally, "John")
#     -> None
#
#
# HINTS:
#
# Base case:
#
#     employee is None
#
# But also think about another successful stopping condition:
#
#     current employee's name == target
#
#
# IMPORTANT:
#
# The recursive function should return an OBJECT, not True/False.
#
# ============================================================

class Employee:
    def __init__(self, name, salary=None):
        self.__name=name
        self.__subordinates=[]

    @property
    def name(self):
        return self.__name

    @property
    def subordinates(self):
        return self.__subordinates

    def add_subordinate(self, emp_obj):
        self.__subordinates.append(emp_obj)

    def __str__(self):
        return f"Name : {self.__name}\nSubordinates : {self.__subordinates}"

    def __repr__(self):
        return f"Name : {self.__name}\nSubordinates : {self.__subordinates}"

def check_employee(emp_obj: "Employee", target):

    if emp_obj.name==target:
        return emp_obj
    
    for emp in emp_obj.subordinates:
        temp=check_employee(emp,target)
        if temp:
            return temp

if __name__=="__main__":
    sally=Employee("Sally")
    emily=Employee("Emily")
    claire=Employee("Claire")
    eric=Employee("Eric")
    mathew=Employee("Mathew")
    sally.add_subordinate(emily)
    sally.add_subordinate(claire)
    emily.add_subordinate(eric)
    emily.add_subordinate(mathew)

    print(check_employee(sally,"Emily"))