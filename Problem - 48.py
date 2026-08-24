# ============================================================
# OOP EXERCISE 25 — Employee Registry
# ============================================================
#
# Extend the Employee class from Exercise 24.
#
# The Employee class should maintain a class-level registry
# containing all Employee objects that have been created.
#
#
# Implement these class methods:
#
#     Employee.find_by_id(id)
#
#     Employee.find_by_name(name)
#
#     Employee.total_employees()
#
#
# Example:
#
#     alice = Employee("Alice")
#     bob = Employee("Bob")
#     charlie = Employee("Charlie")
#
#
#     Employee.find_by_id(2)
#     -> returns the Employee object representing Bob
#
#
#     Employee.find_by_name("Charlie")
#     -> returns the Employee object representing Charlie
#
#
#     Employee.find_by_name("David")
#     -> None
#
#
# REQUIREMENTS:
#
# - Use a class variable for the registry.
# - Use class methods.
# - Do not create a separate registry object outside the class.
#
#
# IMPORTANT QUESTION:
#
# Should find_by_name() operate on ONE Employee object,
# or on the Employee class as a whole?
#
# ============================================================