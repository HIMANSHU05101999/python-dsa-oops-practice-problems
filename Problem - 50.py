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