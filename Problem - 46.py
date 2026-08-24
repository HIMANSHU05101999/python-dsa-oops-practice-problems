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