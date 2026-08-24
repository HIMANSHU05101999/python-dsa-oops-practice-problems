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