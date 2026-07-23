# OOP Revision Exercise 6 (Very Hard)
#
# University System
#
# Please define:
#
# Course
# ----------------
# name
# credits
# grade
#
#
# Student
# ----------------
# name
# stores Course objects
#
#
# Methods:
#
# add_course(course)
#
# completed_credits()
#
# average_grade()
#
# best_course()
# Returns the Course object with the highest grade.
#
#
# __str__()
#
# Format:
#
# "<name>
# completed credits: X
# average grade: Y"
#
#
# Operator Overloading:
#
# student1 > student2
#
# compares average grades.
#
#
# student1 + student2
#
# returns a NEW Student object:
#
# name = "Combined Student"
#
# containing all courses from both students.
#
#
# Example:
#
# s1 = Student("Himanshu")
#
# s1.add_course(Course("Python",5,5))
# s1.add_course(Course("SQL",3,4))
#
# print(s1)
#
#
# Sample output:
#
# Himanshu
# completed credits: 8
# average grade: 4.5