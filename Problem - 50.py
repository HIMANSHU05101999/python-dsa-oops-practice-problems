# ============================================================
# RECURSION + INHERITANCE EXERCISE 27 — Count Developers
# ============================================================
#
# Use the Employee hierarchy from Exercise 26.
#
# Managers can have subordinates.
#
# Example:
#
#                 CEO
#              /       \
#          Manager A  Manager C
#          /     \
#     Developer  Manager B
#                    /   \
#              Developer Designer
#
#
# Write:
#
#     count_developers(employee)
#
# It should recursively count all Developer objects in the
# hierarchy below the given employee.
#
#
# Examples:
#
#     count_developers(CEO)
#     -> 2
#
#     count_developers(Manager B)
#     -> 1
#
#
# REQUIREMENTS:
#
# - Use recursion.
# - Use inheritance.
# - Do not create a flat list of employees first.
#
#
# IMPORTANT:
#
# You need to determine whether the current object is a
# Developer before deciding what the recursive result should be.
#
# ============================================================

class Employee:
    def __init__(self, name):
        self.__name=name
        self.__subordinates=[]

    def add_subordinates(self,obj):
        self.__subordinates.append(obj)

    @property
    def subordinates(self):
        return self.__subordinates

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
            return f"{self.__name}"
    
class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        

class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)

class Designer(Employee):
    def __init__(self, name):
        super().__init__(name)


def count_dev(obj):
    count=0

    if isinstance(obj,Developer):
            count+=1
    
    for sub in obj.subordinates:
        count+=count_dev(sub)

    return count

if __name__=="__main__":
    
    ceo=Employee("CEO")
    m_a=Manager("Manager A")
    m_b=Manager("Manager B")
    m_c=Manager("Manager C")
    dev_a=Developer("Developer A")
    dev_b=Developer("Developer B")
    des=Designer("Designer A")

    ceo.add_subordinates(m_a)
    ceo.add_subordinates(m_c)
    m_a.add_subordinates(dev_a)
    m_a.add_subordinates(m_b)
    m_b.add_subordinates(dev_b)
    m_b.add_subordinates(des)

    print(count_dev(ceo))