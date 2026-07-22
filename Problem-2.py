# OOP Revision Exercise 2 (Medium)
#
# Student and Course
#
# Please define two classes:
#
# 1. Student
#    Constructor arguments:
#    - name: str
#
#    Methods:
#    - add_course(course)
#    - average_grade()
#    - __str__()
#
#
# 2. Course
#    Constructor arguments:
#    - name: str
#    - grade: int
#
#
# The Student class should store Course objects.
#
# average_grade() should return the average of all grades.
# If there are no courses, return 0.
#
# __str__ should return:
#
# "<name>, courses completed <count>, average grade <avg>"
#
#
# Example usage:
#
# student = Student("Himanshu")
#
# student.add_course(Course("Python", 5))
# student.add_course(Course("SQL", 4))
# student.add_course(Course("Algorithms", 3))
#
# print(student)
#
#
# Sample output:
#
# Himanshu, courses completed 3, average grade 4.0