# ============================================================
# OOP EXERCISE 33 — University Student Registry
# ============================================================
#
# Create:
#
#     Student
#     University
#
#
# Student has:
#
#     name
#     student_id
#
#
# University should maintain all students through a
# CLASS-LEVEL registry in Student.
#
#
# Implement:
#
#     Student.total_students()
#
#     Student.find_by_id(student_id)
#
#     Student.find_by_name(name)
#
#
# Student IDs should be generated automatically.
#
#
# Example:
#
#     Student("Alice")
#     Student("Bob")
#     Student("Charlie")
#
#
#     Student.total_students()
#     -> 3
#
#
# REQUIREMENTS:
#
# - class variable
# - class method
# - automatic ID generation
# - object lookup
#
# ============================================================

class Student:
    reg=[]


    @classmethod
    def id_generator(cls):
        if cls.reg == []:
            return 1
        return len(cls.reg)+1
    
    def __init__(self, name):
        id = self.id_generator()
        self.__id = id
        self.__name = name

        self.reg.append(self)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.__id} {self.__name}" 

    @classmethod
    def total(cls):
        return len(cls.reg)

    @classmethod
    def by_id(cls,id):
        for item in cls.reg:
            if id == item.id:
                return item
        return None 

    @classmethod
    def by_name(cls,id):
        for item in cls.reg:
            if id == item.name:
                return item
        return None 


    
    

if __name__=="__main__":

    s1=Student("HKD")
    print(s1)
    s2=Student("ABC")
    print(s2)
    s3=Student("EFG")
    print(s3)
    print(s3.total())
    print(s1.by_id(3))
    print(s1.by_name("ABC"))
    