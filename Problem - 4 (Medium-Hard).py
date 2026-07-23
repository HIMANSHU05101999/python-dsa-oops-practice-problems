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