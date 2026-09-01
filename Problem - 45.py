# ============================================================
# RECURSION + OOP EXERCISE 22 — Maximum Salary
# ============================================================
#
# Extend the Employee class so every employee has:
#
#     name
#     salary
#     subordinates
#
#
# Example:
#
#             Sally 100000
#            /             \
#       Emily 80000      Claire 120000
#       /   \
#   Eric 95000 Matthew 70000
#
#
# Write:
#
#     highest_salary(employee)
#
# It should return the highest salary found in the employee's
# entire hierarchy, including the given employee.
#
#
# Example:
#
#     highest_salary(Sally)
#     -> 120000
#
#     highest_salary(Emily)
#     -> 95000
#
#
# REQUIREMENTS:
#
# - Use recursion.
# - Do NOT use max().
# - Do NOT flatten the hierarchy into a list.
#
#
# HINT:
#
# For one employee, you need to compare:
#
#     employee's own salary
#     highest salary from the subordinate hierarchy
#
# ============================================================

class Employee:
    def __init__(self, name, salary=None):
        self.__name=name
        self.__salary=salary
        self.__subordinates=[]

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def subordinates(self):
        return self.__subordinates

    def add_salary(self, salary):
        self.__salary=salary

    def add_subordinate(self, emp_obj):
        self.__subordinates.append(emp_obj)

    def __str__(self):
        return f"Name : {self.__name}\nSalary : {self.__salary}\nSubordinates : {self.__subordinates}"

    def __repr__(self):
        return f"Name : {self.__name}\nSalary : {self.__salary}\nSubordinates : {self.__subordinates}"

def max_salary(emp_obj: "Employee"):
    max_sal=emp_obj.salary
    abc=0
    if not emp_obj.subordinates:
        return emp_obj.salary

    for emp in emp_obj.subordinates:
        abc=max_salary(emp)
        if max_sal<abc:
            max_sal=abc
    return max_sal

if __name__=="__main__":
    sally=Employee("Sally")
    sally.add_salary(100000)
    emily=Employee("Emily")
    emily.add_salary(80000)
    claire=Employee("Claire")
    claire.add_salary(120000)
    eric=Employee("Eric")
    eric.add_salary(95000)
    mathew=Employee("Mathew")
    mathew.add_salary(70000)
    sally.add_subordinate(emily)
    sally.add_subordinate(claire)
    emily.add_subordinate(eric)
    emily.add_subordinate(mathew)

    print(max_salary(sally))









    

    