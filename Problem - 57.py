# ============================================================
# RECURSION + OOP EXERCISE 34 — University Hierarchy
# ============================================================
#
# Create:
#
#     Person
#     Teacher
#     Student
#     Department
#     University
#
#
# Teacher and Student should inherit from Person.
#
#
# A University contains Departments.
#
# A Department contains:
#
#     Teachers
#     Students
#     Sub-departments
#
#
# Example:
#
#     University
#     ├── Computer Science
#     │   ├── Teachers
#     │   ├── Students
#     │   └── AI
#     │       ├── Teachers
#     │       └── Students
#     │
#     └── Mathematics
#         ├── Teachers
#         └── Students
#
#
# Implement:
#
#     total_students(department)
#
# It should recursively count all students in the department
# and its sub-departments.
#
#
# REQUIREMENTS:
#
# - inheritance
# - recursion
# - multiple classes
# - object relationships
#
#
# IMPORTANT:
#
# The recursive structure is now Department -> Department.
#
# Students and Teachers are objects contained inside the
# department, but they are not themselves part of the recursive
# department hierarchy.
#
# ============================================================