# ============================================================
# RECURSION EXERCISE 3 — Factorial
# ============================================================
#
# Write a recursive function named factorial(n).
#
# The function should return n!.
#
# Remember:
#
# 5! = 5 * 4 * 3 * 2 * 1
#
# 0! = 1
#
# Example:
#
# factorial(5)
#
# should return:
# 120
#
# Think about the relationship:
#
# factorial(5)
#     =
# 5 * factorial(4)
#
# and:
#
# factorial(4)
#     =
# 4 * factorial(3)
#
# Continue until you reach the base case.
#
# WRITE YOUR SOLUTION BELOW:

def factorial(n):
    if n==0:
        return 1

    return factorial(n-1)*n

if __name__=="__main__":
    num=int(input("Enter Num:"))
    print(factorial(num))