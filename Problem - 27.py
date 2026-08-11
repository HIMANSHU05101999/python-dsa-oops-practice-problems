# ============================================================
# RECURSION EXERCISE 5 — Count a Character
# ============================================================
#
# Write a recursive function named count_character(text, target).
#
# The function should return how many times target occurs
# in text.
#
# Example:
#
# count_character("banana", "a")
#
# should return:
# 3
#
# Example:
#
# count_character("hello", "l")
#
# should return:
# 2
#
# Hints:
#
# Look at the first character.
#
# If it matches target:
#     add 1
#
# Otherwise:
#     add 0
#
# Then recursively process the remaining string.
#
# WRITE YOUR SOLUTION BELOW:

def count_char(string, char):
    if string=="":
        return 0
    if string[0]==char:
        return count_char(string[1:],char)+1
    return count_char(string[1:],char)
    

if __name__=="__main__":
    string=input("Enter string")
    char=input("Enter character")
    print(count_char(string,char))