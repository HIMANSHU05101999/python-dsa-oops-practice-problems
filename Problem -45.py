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