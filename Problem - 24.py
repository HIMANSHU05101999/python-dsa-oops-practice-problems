# ============================================================
# RECURSION EXERCISE 2 — Sum from 1 to n
# ============================================================
#
# Write a recursive function named recursive_sum(n).
#
# The function should return:
#
# 1 + 2 + 3 + ... + n
#
# Example:
#
# recursive_sum(5)
#
# should return:
# 15
#
# Because:
# 1 + 2 + 3 + 4 + 5 = 15
#
# Hints:
# - What is the simplest value of n?
# - Think about:
#
#       5 + recursive_sum(4)
#
# - The recursive call should move toward the base case.
#
# Do NOT use a loop.
#
# WRITE YOUR SOLUTION BELOW:

def recursive_sum(n):
    if n<1:
        return 0

    return recursive_sum(n-1)+n
    

if __name__=="__main__":
    num=int(input("Enter Number:"))
    print(recursive_sum(num))