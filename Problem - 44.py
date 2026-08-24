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