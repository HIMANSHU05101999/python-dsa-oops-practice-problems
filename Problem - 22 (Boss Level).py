# OOP Revision Exercise 22 (Boss Level)
#
# University Management System
#
# Difficulty: ★★★★★
#
# Student
#
# Stores:
# - student id
# - name
#
#
# Course
#
# Stores:
# - course code
# - course name
# - credits
#
#
# Enrollment
#
# Stores:
# - Student object
# - Course object
# - grade
#
#
# University
#
# Stores:
#
# students:
#     student id -> Student object
#
# courses:
#     course code -> Course object
#
# enrollments:
#     (student id, course code) -> Enrollment object
#
#
# Commands:
#
# add student
# add course
# enroll student
# update grade
# view transcript
# university statistics
#
#
# Statistics:
#
# total students
# total courses
# average GPA
# grade distribution
#
#
# This combines everything you've learned:
#
# ✓ Multiple classes
# ✓ Objects inside dictionaries
# ✓ Objects referencing other objects
# ✓ Properties
# ✓ Setters
# ✓ Updating existing objects
# ✓ Statistics
# ✓ Interface class


class Student:
    def __init__(self, stud_id, name):
        self.__stud_id=stud_id
        self.__name=name

    @property
    def stud_id(self):
        return self.__stud_id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Student ID: {self.__stud_id} Student Name: {self.__name}"

class Course:
    def __init__(self, course_id, name):
        self.__course_id=course_id
        self.__name=name

    @property
    def course_id(self):
        return self.__course_id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Course ID: {self.__course_id} Course Name: {self.__name}"

class Enrolment:
    def __init__(self, stud_obj, course_obj, grade=None):
        self.__stud=stud_obj
        self.__course=course_obj
        self.__grade=grade        

    @property
    def stud_obj(self):
        return self.__stud

    @property
    def course_obj(self):
        return self.__course

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self,val):
        self.__grade=val

    def __str__(self):
        return f"Student Detail: {self.__stud}\nCourse Details: {self.__course}\nGrade: {self.grade}"

class University:
    def __init__(self):
        self.__students={}
        self.__course={}
        self.__enroll={}

    def add_stud(self, stud_id, name):
        stud_obj=Student(stud_id,name)
        self.__students[stud_id]=stud_obj

    def add_course(self, course_id, name):
        course_obj=Course(course_id, name)
        self.__course[course_id]=course_obj

    def enroll_stud(self,stud_obj,course_obj,grade=None):
        enroll_obj=Enrolment(stud_obj,course_obj,grade)
        if (stud_obj.stud_id,course_obj.course_id) in self.__enroll:
            print("Already Enrolled")
        else:
            self.__enroll[(stud_obj.stud_id,course_obj.course_id)]=enroll_obj

    def search(self, stud_id, course_id):
        if stud_id in self.__students: 
            stud_obj=self.__students[stud_id]
        else:
            print("No Student available with this ID, please enroll the student first")
            return 
        if course_id in self.__course:
            course_obj=self.__course[course_id]
        else:
            print("No Coorse available with this ID, please enroll the student first")
            return
        return(stud_obj,course_obj)

    def view_transcript(self):
        for val in self.__enroll.values():
            print(val)

    def add_grade(self, enroll_id, grade):
        if self.__enroll[enroll_id].grade==None:
            self.__enroll[enroll_id].grade=grade
            return
        if self.__enroll[enroll_id]!=None:
            if self.__enroll[enroll_id].grade<grade:
                self.__enroll[enroll_id].grade=grade

        
    def stats(self):
        stat={}
        print(f"Total Students: {len(self.__students)}")
        print(f"Total Courses: {len(self.__course)}")
        print(f"Average GPA: {sum(enrol.grade for enrol in self.__enroll.values())/len(self.__students)}")
        for enrol in self.__enroll.values():
            if enrol.grade not in stat:
                stat[enrol.grade]="x"
            else:
                stat[enrol.grade]+="x"
        for grd,val in stat.items():
            print(f"{grd}: {val}")

class Interface:
    def __init__(self):
        self.__interact=University()

    def view(self):
        print("1 add student\n2 add course\n3 enroll student\n4 update grade\n5 view transcript\n6 university stats\n0 exit")

    def exe(self):
        self.view()
        while True:
            ch=input("enter choice: ")
            if ch=="1":
                stud_id=input("Enter student id: ")
                name=input("Enter student name: ")
                self.__interact.add_stud(stud_id,name)
            if ch=="2":
                course_id=input("Enter course ID: ")
                name=input("Enter course name: ")
                self.__interact.add_course(course_id, name)
            if ch=="3":
                stud_id=input("Enter the student ID: ")
                course_id=input("Enter the course ID: ")
                result=self.__interact.search(stud_id,course_id)
                if result is None:
                    continue
                stud_obj,course_obj=result
                self.__interact.enroll_stud(stud_obj,course_obj)
            if ch=="4":
                stud_id=input("Enter the student ID: ")
                course_id=input("Enter the course ID: ")
                grade=int(input("Enter Grade: "))
                self.__interact.add_grade((stud_id,course_id),grade)
            if ch=="5":
                self.__interact.view_transcript()
            if ch=="6":
                self.__interact.stats()
            if ch=="0":
                return

app=Interface()
app.exe()