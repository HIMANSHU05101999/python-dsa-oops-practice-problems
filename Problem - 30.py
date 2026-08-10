# ============================================================
# RECURSION EXERCISE 7 — Find an Element
# ============================================================
#
# Write a recursive function named contains(numbers, target).
#
# It should return True if target exists in numbers,
# otherwise False.
#
# Example:
#
# contains([4, 7, 2, 9], 2)
#
# returns:
# True
#
# contains([4, 7, 2, 9], 5)
#
# returns:
# False
#
# Hints:
#
# Look at the first element.
#
# If it is target:
#     return True
#
# Otherwise:
#     recursively search the rest of the list.
#
# What should happen when the list becomes empty?
#
# Do NOT use "in".
#
# WRITE YOUR SOLUTION BELOW:

def contains(ls,trg):
    if not ls:
        return False

    if ls[0]==trg:
        return True
    return contains(ls[1:],trg)

if __name__=="__main__":
    print(contains([4, 7, 2, 9], 2))
    print(contains([4, 7, 2, 9], 5))