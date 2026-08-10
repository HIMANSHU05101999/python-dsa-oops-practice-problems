# ============================================================
# RECURSION EXERCISE 9 — Balanced Parentheses
# ============================================================
#
# Write a recursive function named balanced_parentheses(text).
#
# The function should return True if the parentheses are
# completely nested.
#
# Examples:
#
# balanced_parentheses("((()))")
# -> True
#
# balanced_parentheses("()")
# -> True
#
# balanced_parentheses("(()())")
# -> False
#
# balanced_parentheses("())")
# -> False
#
# balanced_parentheses(")(")
# -> False
#
# IMPORTANT:
#
# This exercise only handles completely nested parentheses.
#
# Therefore:
#
# "((()))" is valid
#
# but:
#
# "()()" is NOT valid.
#
# Hints:
#
# 1. Empty string -> True
# 2. First character must be "("
# 3. Last character must be ")"
# 4. Remove the first and last characters
# 5. Recursively check the remaining string
#
# WRITE YOUR SOLUTION BELOW: