# OOP Revision Exercise 10 (Factory Methods)
#
# Book
#
# Constructor:
# - title
# - author
# - pages
#
#
# Define the following class method:
#
# from_string(data)
#
# data is in the format:
#
# "Python;Guido;500"
#
# The method should return a Book object.
#
#
# Example:
#
# b = Book.from_string("Python;Guido;500")
#
# print(b)
#
#
# __str__()
#
# "<title> by <author>, <pages> pages"
#
#
# Sample output:
#
# Python by Guido, 500 pages

class Books:
    def __init__(self, title: str, auth: str, page: int):
        self.__title=title
        self.__auth=auth
        self.__page=page

    @property
    def title(self):
        return self.__title

    @property
    def auth(self):
        return self.__auth

    @property
    def page(self):
        return self.__page

    @classmethod          
    def from_string(cls, inp: str):
        inp=inp.split(";")
        return cls(inp[0],inp[1],int(inp[2]))

    def __str__(self):
        return f"{self.__title} by {self.__auth}, {self.__page} pages"

def main():
    b = Books.from_string("Python;Guido;500")

    print(b)
if __name__=="__main__":
    main()