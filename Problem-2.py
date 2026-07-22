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

class Student:
    def __init__(self, name: str):
        self.__name=name
        self.__course=[]

    def add_course(self, course: "Course"):
        self.__course.append(course)

    def average_grade(self):
        if len(self.__course)==0:
            return 0
        total_score=0
        for course in self.__course:
            total_score+=course.grade
        average=total_score/len(self.__course)
        return average

    def __str__(self):
        return f"{self.__name}, courses completed {len(self.__course)}, average grade {self.average_grade()}"

class Course:
    def __init__(self, course_name: str, grade: int):
        self.__course_name=course_name
        self.__grade=grade

    @property
    def grade(self):
        return self.__grade

    @property
    def course_name(self):
        return self.__course_name
    
    
def main():
    student = Student("Himanshu")

    student.add_course(Course("Python", 5))
    student.add_course(Course("SQL", 4))
    student.add_course(Course("Algorithms", 3))

    print(student)
if __name__=="__main__":
    main()
        