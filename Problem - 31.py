# ============================================================
# RECURSION EXERCISE 8 — Maximum Value
# ============================================================
#
# Write a recursive function named recursive_max(numbers).
#
# It should return the largest value in the list.
#
# Example:
#
# recursive_max([4, 8, 2, 10, 3])
#
# returns:
# 10
#
# Hints:
#
# Compare the first element with the maximum value
# of the remaining list.
#
# For example:
#
# max([4, 8, 2])
#
# can be thought of as:
#
# max(4, max([8, 2]))
#
# What is the base case?
#
# You may assume the list is not empty.
#
# Do NOT use max().
#
# WRITE YOUR SOLUTION BELOW:

def recursive_max(ls: list):
    if len(ls)==1:
        return ls[0]

    a=recursive_max(ls[1:])

    if ls[0]>a:
        return ls[0]
    return a
        
        
        
    
    
if __name__=="__main__":
    print(recursive_max([4, 50, 2, 10, 3]))