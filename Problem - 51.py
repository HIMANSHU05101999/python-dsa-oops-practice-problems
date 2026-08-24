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