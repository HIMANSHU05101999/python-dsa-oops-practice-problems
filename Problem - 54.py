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