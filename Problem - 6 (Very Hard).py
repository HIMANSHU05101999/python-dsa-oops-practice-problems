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

class Course:
    def __init__(self, name: str, credit: int, grade: float):
        self.__name=name
        self.__credit=credit
        self.__grade=grade

    @property
    def a(self):
        return self.__name

    @property
    def b(self):
        return self.__credit

    @property
    def c(self):
        return self.__grade

class Student:
    def __init__(self, name: str):
        self.__name=name
        self.__course=[]

    def add_course(self, course: "Course"):
        self.__course.append(course)

    def completed_credits(self):
        return sum(course.b for course in self.__course)

    def average_grade(self):
        if not self.__course:
            return 0
        return sum(course.c for course in self.__course)/len(self.__course)

    def best_course(self):
        max_grade=self.__course[0]
        for course in self.__course:
            if max_grade.c<course.c:
                max_grade=course
        return max_grade

    def __str__(self):
        return f"{self.__name} \ncompleted credits: {self.completed_credits()} \naverage grade: {self.average_grade()}"

    def __add__(self, other: "Student"):
        combined=Student("Combined Student")
        combined.__course=self.__course+other.__course
        return combined
         
    def __gt__(self, other: "Student"):
        return self.average_grade()>other.average_grade()

def main():
    s1 = Student("Himanshu")

    s1.add_course(Course("Python",5,5))
    s1.add_course(Course("SQL",3,4))

    print(s1)
    s3=(s1+s1)
    print(s3)

if __name__=="__main__":
    main()