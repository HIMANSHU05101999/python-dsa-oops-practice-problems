# ============================================================
# RECURSION + OOP EXERCISE 32 — Find File
# ============================================================
#
# Using File and Folder, write:
#
#     find_file(folder, filename)
#
# It should search recursively through the folder structure.
#
#
# If the file exists:
#
#     return the actual File object
#
# If it doesn't exist:
#
#     return None
#
#
# Example:
#
#     find_file(projects, "test.py")
#
#     -> File object representing test.py
#
#
# REQUIREMENTS:
#
# - Use recursion.
# - Return an object.
# - Do not create a flat list of files first.
#
#
# IMPORTANT:
#
# Your recursive function now needs to deal with different
# object types:
#
#     File
#     Folder
#
# ============================================================

class File:
    def __init__(self, name, size):
        self.__name=name
        self.__size=size

    def __str__(self):
        return f"Name: {self.__name} Size: {self.__size}"
    
    @property
    def name(self):
        return self.__name

class Folder:
    def __init__(self, name):
        self.__name=name
        self.__contents=[]

    @property
    def contents(self):
        return self.__contents


    def add_fobj(self, obj):
        self.__contents.append(obj)


def find_file(obj, name):

    if isinstance(obj,File):
        if obj.name==name:
            return obj
        

    if isinstance(obj,Folder):
        for item in obj.contents:
            temp=find_file(item,name)
            if temp:
                return temp   
    return None      


if __name__=="__main__":
    project=Folder("Project")
    python=Folder("Python")
    java=Folder("Java")

    main_py=File("Main.py",5)
    test_py=File("test.py",3)

    main_java=File("Main.java",6)
    read_me=File("README.md",1)

    project.add_fobj(python)
    project.add_fobj(java)
    project.add_fobj(read_me)

    python.add_fobj(main_py)
    python.add_fobj(test_py)

    java.add_fobj(main_java)

    print(find_file(project,"Main.java"))



