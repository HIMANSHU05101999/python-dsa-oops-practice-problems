# ============================================================
# RECURSION + INHERITANCE EXERCISE 35 — Search by Role
# ============================================================
#
# Use:
#
#     Employee
#     Manager
#     Developer
#     Designer
#     Intern
#
#
# Managers can have subordinates.
#
#
# Write:
#
#     find_by_role(employee, role)
#
# It should return a list containing every employee underneath
# the given employee whose object belongs to the requested role.
#
#
# Example:
#
#     find_by_role(ceo, Developer)
#
# should return a list containing all Developer objects in the
# hierarchy.
#
#
# REQUIREMENTS:
#
# - recursion
# - inheritance
# - classes
# - returned lists
#
#
# IMPORTANT:
#
# Do not store strings such as:
#
#     "developer"
#     "manager"
#
# to identify the role.
#
# Use Python's object/inheritance system to determine the role.
#
# ============================================================