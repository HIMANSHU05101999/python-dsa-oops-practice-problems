# ============================================================
# RECURSION EXERCISE 4 — Reverse a String
# ============================================================
#
# Write a recursive function named reverse_string(text).
#
# It should return the string reversed.
#
# Example:
#
# reverse_string("hello")
#
# should return:
#
# "olleh"
#
# Hints:
#
# Think about:
#
# "hello"
#
# The first character is "h".
# The remaining string is "ello".
#
# Can you put "h" somewhere after the recursive result?
#
# Do NOT use:
# - reversed()
# - [::-1]
# - loops
#
# WRITE YOUR SOLUTION BELOW:

def rev_str(string: str):
    if string=="":
        return ""

    return rev_str(string[1:]) + string[0]


if __name__=="__main__":
    string=input("Enter the string")
    print(rev_str(string))