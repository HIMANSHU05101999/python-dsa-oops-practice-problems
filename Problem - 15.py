# OOP Revision Exercise 15
#
# Student Records
#
# Difficulty: ★★☆☆☆
#
# Create a program for storing student records.
#
# Student
#
# A Student object stores:
# - name
# - age
# - major
#
# Implement:
# - properties for all attributes
# - __str__()
#
#
# StudentRegistry
#
# Stores Student objects in a dictionary:
#
#     student_name -> Student object
#
#(I have use lists instead, to increase the complexity a little to try a different data structure)
#
# Methods:
#
# add_student(student)
#
# If a student with the same name already exists,
# replace the old object with the new one.
#
#
# get_student(name)
#
# Returns the Student object or None.
#
#
# statistics()
#
# Prints:
#
# total students
# average age
#
#
# Interface
#
# Commands:
#
# 1 add student
# 2 search
# 3 statistics
# 0 exit
#
#
# Example:
#
# 1
# Alice
# 21
# Computer Science
#
# 2
# Alice
#
# Output:
#
# Alice (21 years) Computer Science

class Student:
    def __init__(self, name: str, age: int, major: str):
        self.__name=name
        self.__age=age
        self.__major=major

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def major(self):
        return self.__major

    def __str__(self):
        return f"{self.__name} ({self.__age} age) {self.__major}"
    
class StudentRegistary:
    def __init__(self):
        self.__studentdetail=[]

    def add_students(self,name,age,major):
        stud=Student(name,age,major)
        for student in self.__studentdetail:
            if stud.name==student.name:
                self.__studentdetail.remove(student)
                break
            
        self.__studentdetail.append(stud)
            
        
    def search_student(self,name):
        for student in self.__studentdetail:
            if name == student.name:
                return student

    def statistics(self):
        total_stud=len(self.__studentdetail)
        if total_stud<=0:
            return (0,0)
        total_age=0
        for student in self.__studentdetail:
            total_age+=student.age
        average_age=total_age/total_stud
        return(total_stud,average_age)

class Interface:
    def __init__(self):
        self.__interact=StudentRegistary()

    def options(self):
        print("1 add student: ")
        print("2 search: ")
        print("3 stats")
        print("0 exit")

    def choice(self):
        self.options()
        while True:
            pick=input("Pick: ")
            if pick=="1":
                self.add_student()  
            if pick=="2":
                self.search()  
            if pick=="3":
                self.stats()
            if pick=="0":
                return

    def add_student(self):
        name=input("Enter Name: ")
        age=int(input("Enter Age: "))
        major=input("Enter Majors: ")
        self.__interact.add_students(name,age,major)

    def search(self):
        name=input("Enter name: ")
        stud_obj=self.__interact.search_student(name)
        self.print_str(stud_obj)

    def stats(self):
        tot_stud,avg_age=self.__interact.statistics()
        print(f"Total Students: {tot_stud}")
        print(f"Average Age: {avg_age}")

    def print_str(self, stud_obj):
        if stud_obj==None:
            print("Student not found")
        else:    
            print(stud_obj)

app=Interface()
app.choice()
