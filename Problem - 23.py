# ============================================================
# RECURSION EXERCISE 1 — Countdown
# ============================================================
#
# Write a recursive function named countdown(n).
#
# The function should print numbers from n down to 1,
# followed by "Done!".
#
# Example:
#
# countdown(5)
#
# Output:
# 5
# 4
# 3
# 2
# 1
# Done!
#
# Hints:
# - You need a base case.
# - What should happen when n reaches 0?
# - The recursive call should use a smaller value of n.
#
# Do NOT use a loop.
#
# WRITE YOUR SOLUTION BELOW:

def countdown(n):
    if n==1:
        print(1)
        print("Done")
        return

    print(n)
    countdown(n-1)
    

if __name__=="__main__":
    num=int(input("Enter Number: "))
    countdown(num)
