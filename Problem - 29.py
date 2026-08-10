# ============================================================
# RECURSION EXERCISE 6 — List Sum
# ============================================================
#
# Write a recursive function named list_sum(numbers).
#
# It should return the sum of all numbers in the list.
#
# Example:
#
# list_sum([2, 4, 6, 8])
#
# should return:
# 20
#
# Hints:
#
# Think about:
#
# [2, 4, 6, 8]
#
# first item = 2
# remaining items = [4, 6, 8]
#
# So the problem becomes:
#
# 2 + list_sum([4, 6, 8])
#
# What should the function return for an empty list?
#
# Do NOT use sum().
#
# WRITE YOUR SOLUTION BELOW:

def list_sum(ls: list):
    if not ls:
        return 0

    return list_sum(ls[1:])+ls[0]

if __name__=="__main__":
    print(list_sum([1,2,3,4,5,6]))