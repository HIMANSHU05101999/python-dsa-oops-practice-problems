# ============================================================
# RECURSION EXERCISE 10 — Balanced Brackets
# ============================================================
#
# Expand the previous exercise so that it handles:
#
# ()
# []
#
# Examples:
#
# balanced_brackets("([[]])")
# -> True
#
# balanced_brackets("([])")
# -> True
#
# balanced_brackets("([)]")
# -> False
#
# balanced_brackets("([bad])")
# -> True
#
# Characters which are not brackets should be ignored.
#
# The brackets must be completely nested.
#
# Hints:
#
# You need to check matching pairs:
#
# "(" matches ")"
# "[" matches "]"
#
# If the first and last characters are not a matching pair,
# return False.
#
# If they match:
#
# remove them and recursively check the inside.
#
# WRITE YOUR SOLUTION BELOW:
def balanced_brackets(string):
    for char in string:
        if char not in "()[]":
            string=string.replace(char,"")
        

    if string == "":
        return True

    if string[0]=="(" and string[-1]==")" or string[0]=="[" and string[-1]=="]":
        return balanced_brackets(string[1:-1])
    return False

if __name__=="__main__":
    print(balanced_brackets("([[]])"))


    print(balanced_brackets("([])"))


    print(balanced_brackets("([)]"))


    print(balanced_brackets("([bad])"))