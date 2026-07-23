# OOP Revision Exercise 4 (Medium-Hard)
#
# Library System
#
# Please define two classes:
#
# 1. Book
#
# Constructor arguments:
# - title: str
# - author: str
# - pages: int
#
# Methods:
# - __str__()
#
# Format:
# "<title> by <author>, <pages> pages"
#
#
# 2. Library
#
# Constructor arguments:
# - name: str
#
# Methods:
#
# add_book(book)
#
# total_pages()
# Returns the total number of pages in all books.
#
# find_book(title)
# Returns the Book object with the matching title.
# If not found, return None.
#
# remove_book(title)
# Removes the book with that title.
#
# __str__()
#
# Format:
#
# "<library_name>: <number_of_books> books, <total_pages> pages"
#
#
# Example:
#
# library = Library("City Library")
#
# library.add_book(Book("Python", "Guido", 500))
# library.add_book(Book("Algorithms", "CLRS", 1300))
#
# print(library)
#
#
# Sample output:
#
# City Library: 2 books, 1800 pages

class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.__name=name
        self.__author=author
        self.__pages=pages

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @property
    def pages(self):
        return self.__pages
    
    def __str__(self):
        return f"{self.__name} by {self.__author}, {self.__pages} pages"

class Library:
    def __init__(self, name: str):
        self.__name=name
        self.__books=[]

    def __str__(self):

        return f"{self.__name}: {len(self.__books)} books, {sum(book.pages for book in self.__books)} pages"

    def add_book(self, book: "Book"):
        self.__books.append(book)

    def remove_book(self, name: str):
        if not self.__books:
            return None
        for book in self.__books:
            if book.name==name:
                self.__books.remove(name)
                break
    def total_pages(self):
        if not self.__books:
            return None
        return sum(book.pages for book in self.__books)

    def find_book(self, name: str):
        if not self.__books:
            return None
        for book in self.__books:
            if book.name==name:
                return book
            else:
                return None

def main():
    library = Library("City Library")

    library.add_book(Book("Python", "Guido", 500))
    library.add_book(Book("Algorithms", "CLRS", 1300))

    print(library)
if __name__=="__main__":
    main()