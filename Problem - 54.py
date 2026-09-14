# ============================================================
# RECURSION + OOP EXERCISE 31 — Total Folder Size
# ============================================================
#
# Using File and Folder from Exercise 30, write:
#
#     total_size(folder)
#
# It should return the combined size of every file inside the
# folder and all nested folders.
#
#
# Example:
#
#     Projects/
#     ├── main.py       10 KB
#     ├── test.py       20 KB
#     └── Python/
#         ├── app.py    30 KB
#         └── data.csv  40 KB
#
#
#     total_size(Projects)
#     -> 100
#
#
# HINT:
#
# A File already knows its own size.
#
# A Folder does not have a size directly.
#
# Its size must be calculated from its contents.
#
#
# REQUIREMENTS:
#
# - recursion
# - objects
# - return values
#
# ============================================================

class File:
    def __init__(self, name, size):
        self.__name=name
        self.__size=size

    @property
    def size(self):
        return self.__size

class Folder:
    def __init__(self, name):
        self.__name=name
        self.__contents=[]

    @property
    def contents(self):
        return self.__contents

    def add_fobj(self, obj):
        self.__contents.append(obj)

def total_size(obj):
    temp=0

    if isinstance(obj, File):
        return obj.size

    for item in obj.contents:
        temp+=total_size(item)
    return temp

if __name__=="__main__":
    project=Folder("Project")
    python=Folder("Python")

    main_py=File("Main.py", 10)
    test_py=File("Test.py", 20)
    app_py=File("app.py", 30)
    data_csv=File("Data.csv", 40)

    project.add_fobj(main_py)
    project.add_fobj(test_py)
    project.add_fobj(python)

    python.add_fobj(app_py)
    python.add_fobj(data_csv)

    print(total_size(project))

