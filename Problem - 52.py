# ============================================================
# RECURSION + OOP EXERCISE 29 — Highest Paid Employee
# ============================================================
#
# Using the employee hierarchy, write:
#
#     highest_paid_employee(employee)
#
# It should return the actual Employee object with the highest
# salary in the entire hierarchy.
#
#
# Example:
#
#             Alice 80000
#            /             \
#       Bob 95000        Charlie 70000
#       /   \
#    David 60000   Emma 120000
#
#
#     highest_paid_employee(Alice)
#
# should return Emma's Employee object.
#
#
# REQUIREMENTS:
#
# - Use recursion.
# - Do not use max().
# - Return the OBJECT, not the salary.
#
#
# THINK:
#
# Each recursive call should answer:
#
# "Who is the highest-paid employee in THIS subtree?"
#
# ============================================================