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