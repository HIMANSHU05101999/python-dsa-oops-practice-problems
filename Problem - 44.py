# ============================================================
# RECURSION + OOP EXERCISE 21 — Employee Hierarchy
# ============================================================
#
# Create a class Employee with:
#
#     name
#     subordinates
#
# Every employee starts with an empty list of subordinates.
#
# Add the method:
#
#     add_subordinate(employee)
#
# which adds an Employee to the list of subordinates.
#
#
# Example hierarchy:
#
#             Sally
#            /     \
#         Emily    Claire
#        / | \
#     Eric Matthew Adele
#
#
# Write the function:
#
#     count_subordinates(employee)
#
# It should return the total number of employees below the
# given employee.
#
# Both direct and indirect subordinates must be counted.
#
# Examples:
#
#     count_subordinates(Sally)
#     -> 5
#
#     count_subordinates(Emily)
#     -> 3
#
#     count_subordinates(Eric)
#     -> 0
#
#
# HINTS:
#
# If employee has no subordinates:
#
#     return 0
#
# Otherwise:
#
#     count the subordinates of each subordinate
#     and include the subordinate themselves.
#
#
# IMPORTANT:
#
# - Use recursion.
# - Do not use a global counter.
# - Think about what each recursive call should RETURN.
#
# ============================================================

class Employee:
    def __init__(self, name: str):
        self.__name=name
        self.__subordinate=[]

    @property
    def name(self):
        return self.__name

    @property
    def subordinate(self):
        return self.__subordinate

    def __str__(self):
        return f"Name: {self.__name}"

    def add_subordinate(self, emp_obj: "Employee"):
        self.__subordinate.append(emp_obj)

def count_subordinates(emp_obj: "Employee"):
    tot=0
    if not emp_obj.subordinate:
        return 0
    
    tot=len(emp_obj.subordinate)

    for emp in emp_obj.subordinate:
        tot += count_subordinates(emp)
    return tot    

if __name__=="__main__":
    sally=Employee("Sally")
    emily=Employee("Emily")
    claire=Employee("Claire")
    eric=Employee("Eric")
    mathew=Employee("Mathew")
    adele=Employee("Adele")

    sally.add_subordinate(emily)
    sally.add_subordinate(claire)
    emily.add_subordinate(eric)
    emily.add_subordinate(mathew)
    emily.add_subordinate(adele)

    print(count_subordinates(sally))
    print(count_subordinates(claire))
    print(count_subordinates(emily))
