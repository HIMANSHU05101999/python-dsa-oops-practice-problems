# OOP Revision Exercise 5 (Hard)
#
# Employee Management System
#
# Please define:
#
# class Employee
#
# Constructor:
# - name
# - salary
#
# Methods:
#
# yearly_salary()
#
# __str__()
#
# Format:
#
# "<name>, salary <salary>"
#
#
# Define a derived class:
#
# class Manager(Employee)
#
# Additional constructor argument:
# - bonus
#
# yearly_salary()
#
# Managers receive:
#
# salary * 12 + bonus
#
#
# Define another derived class:
#
# class Developer(Employee)
#
# Additional constructor argument:
# - projects_completed
#
# Developers receive:
#
# salary * 12
# + projects_completed * 1000
#
#
# Example:
#
# e = Employee("Peter", 3000)
# m = Manager("Maria", 5000, 10000)
# d = Developer("John", 4000, 5)
#
# print(e.yearly_salary())
# print(m.yearly_salary())
# print(d.yearly_salary())
#
#
# Sample output:
#
# 36000
# 70000
# 53000