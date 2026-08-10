# ============================================================
# RECURSION + DSA EXERCISE 18 — Search Binary Tree
# ============================================================
#
# Write:
#
# tree_contains(root, target)
#
# It should return True if target exists anywhere in the
# binary tree.
#
# Example:
#
#             10
#            /  \
#           5    15
#          / \
#         2   7
#
# tree_contains(root, 7)
# -> True
#
# tree_contains(root, 20)
# -> False
#
# Hints:
#
# If root is None:
#     False
#
# If root.value == target:
#     True
#
# Otherwise search:
#
#     left subtree
#     OR
#     right subtree
#
# This is one of the most important recursive patterns
# for tree algorithms.
#
# WRITE YOUR SOLUTION BELOW: