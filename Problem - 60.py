# ============================================================
# RECURSION + OOP FINAL CHALLENGE — Organization Management
# ============================================================
#
# Build a small organization management system.
#
#
# Create:
#
#     Employee
#     Manager
#     Developer
#     Designer
#     Intern
#     Department
#     Company
#
#
# Employee should have:
#
#     name
#     salary
#     employee_id
#
#
# Managers can have subordinates.
#
#
# The Employee class should maintain:
#
#     automatic employee ID generation
#     total number of employees
#     employee registry
#
#
# Use CLASS METHODS for operations that concern the Employee
# class as a whole.
#
#
# The system should support:
#
#     find employee by ID
#     find employee by name
#     count employees
#     count employees by role
#     calculate total salary
#     find highest-paid employee
#     count subordinates
#     count developers under a manager
#     find an employee recursively
#
#
# Example hierarchy:
#
#                 CEO
#              /       \
#          Manager A   Manager B
#          /     \          \
#     Developer Designer   Developer
#         |
#       Intern
#
#
# REQUIREMENTS:
#
# - Use inheritance.
# - Use class variables.
# - Use class methods.
# - Use instance methods.
# - Use recursion.
# - Use object relationships.
# - Do not flatten the hierarchy for recursive operations.
#
#
# BEFORE CODING:
#
# Draw the object structure.
#
# Ask yourself:
#
#     What is an object?
#
#     What is an attribute?
#
#     What is an instance method?
#
#     What is a class variable?
#
#     What is a class method?
#
#     Which classes inherit from Employee?
#
#     Which objects contain other objects?
#
#     Where is the recursive structure?
#
#     What should ONE recursive call return?
#
#
# IMPORTANT:
#
# There is intentionally no step-by-step algorithm here.
#
# This exercise is meant to test whether you can design the
# solution rather than recognize a previously memorized pattern.
#
# ============================================================