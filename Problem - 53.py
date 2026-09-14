# ============================================================
# RECURSION + OOP EXERCISE 30 — File System
# ============================================================
#
# Create two classes:
#
#     File
#     Folder
#
#
# File has:
#
#     name
#     size
#
#
# Folder has:
#
#     name
#     contents
#
#
# A folder can contain:
#
#     File objects
#     Folder objects
#
#
# Example:
#
#     Projects/
#     ├── Python/
#     │   ├── main.py
#     │   └── test.py
#     ├── Java/
#     │   └── Main.java
#     └── README.md
#
#
# Write:
#
#     total_files(folder)
#
# It should recursively return the number of files inside
# the folder and all its subfolders.
#
#
# Expected:
#
#     4
#
#
# REQUIREMENTS:
#
# - Use recursion.
# - Use OOP.
# - A Folder may contain other Folders.
# - Do not flatten the structure first.
#
#
# IMPORTANT:
#
# This problem is intentionally similar to your binary-tree
# exercises, but there is no Node class.
#
# You must recognize the recursive structure yourself.
#
# ============================================================

class File:
    def __init__(self, name, size):
        self.__name=name
        self.__size=size

class Folder:
    def __init__(self, name):
        self.__name=name
        self.__contents=[]

    @property
    def contents(self):
        return self.__contents

    def add_fobj(self, obj):
        self.__contents.append(obj)

def total_files(obj):
    temp=0
    if isinstance(obj,File):
        return 1
    

    for item in obj.contents:
        temp+=total_files(item)
    return temp

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

    print(total_files(project))

