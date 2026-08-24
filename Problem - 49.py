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