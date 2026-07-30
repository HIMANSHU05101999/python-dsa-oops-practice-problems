# OOP Revision Exercise 17
#
# Library System
#
# Difficulty: ★★★☆☆
#
# Book
#
# Stores:
# - title
# - author
# - pages
# - borrowed (True/False)
#
#
# Library
#
# Dictionary:
#
# title -> Book object
#
#
# Methods:
#
# add_book(book)
#
# borrow(title)
#
# return_book(title)
#
# get_book(title)
#
# statistics()
#
# Prints:
#
# total books
# borrowed books
# available books
#
#
# Interface:
#
# 1 add book
# 2 borrow
# 3 return
# 4 search
# 5 statistics
# 0 exit

class Book:
    def __init__(self, title: str, author: str, pages: int, borrowed=None):
        self.__title=title
        self.__author=author
        self.__pages=pages
        self.__borrowed=borrowed

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def pages(self):
        return self.__pages

    @property
    def borrowed(self):
        return self.__borrowed

    @borrowed.setter
    def borrowed(self,val):
        self.__borrowed=val

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Pages: {self.__pages}, Borrowed: {"Yes" if self.__borrowed==True else "No, Available"}"

class Library:
    def __init__(self):
        self.__storage={}
        self.__borrowed={}

    def add_book(self,title,author,pages):
        book_obj=Book(title,author,pages)
        if book_obj.title in self.__storage:
            print("Book already exists")
            return
        else:
            self.__storage[title]=book_obj

    def borrow(self,title):
        if title in self.__storage:            
            self.__storage[title].borrowed=True
            self.__borrowed[title]=self.__storage[title]
            del self.__storage[title]
        else:
            print("Book already borrowed")


    def return_book(self,title):
        if title in  self.__borrowed:
                self.__borrowed[title].borrowed=False
                self.__storage[title]=self.__borrowed[title]
                del self.__borrowed[title]
        else:
            print("Book already returned")

    def search(self, title):
        if title in self.__borrowed: #or title in self.__storage:
            return self.__borrowed[title]
        if title in self.__storage:
            return self.__storage[title]

    def stats(self):
        borrowed=len(self.__borrowed)
        avaliable=len(self.__storage)
        total=borrowed+avaliable
        return (total,avaliable,borrowed)
    
class Interface:
    def __init__(self):
        self.__interact=Library()

    def disp(self):
        print("1 add book")
        print("2 borrow")
        print("3 return")
        print("4 search")
        print("5 statistics")
        print("0 exit")

    def execute(self):
        self.disp()
        while True:
            choice=input("Enter choice: ")
            if choice == "1":
                self.add_book()
            if choice == "2":
                self.borrow()
            if choice == "3":
                self.return_book()
            if choice == "4":
                self.search()
            if choice == "5":
                self.stats()
            if choice == "0":
                return

    def add_book(self):
        title=input("Enter Title of The Book: ")
        author=input("Enter Auhtor of the Book: ")
        pages=int(input("Number of Pages: "))
        self.__interact.add_book(title,author,pages)

    def borrow(self):
        title=input("Enter the title of the book you want to borrow: ")
        self.__interact.borrow(title)

    def return_book(self):
        title=input("Enter the title of the book you want to borrow: ")
        self.__interact.return_book(title)

    def search(self):
        title=input("Title of the book you want to search: ")
        print(self.__interact.search(title))

    def stats(self):
        total,available,borrowed=self.__interact.stats()
        print(f"Total Books: {total}")
        print(f"Available Books: {available}")
        print(f"Borrowed: {borrowed}")

app=Interface()
app.execute()