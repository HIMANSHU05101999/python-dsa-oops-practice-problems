# ============================================================
# RECURSION + DSA EXERCISE 20 — Count Leaves
# ============================================================
#
# Write:
#
# count_leaves(root)
#
# A leaf is a node which has:
#
#     no left child
#     AND
#     no right child
#
# Example:
#
#             10
#            /  \
#           5    15
#          / \
#         2   7
#
# Leaves are:
#
# 2
# 7
# 15
#
# Therefore:
#
# count_leaves(root)
# -> 3
#
# Hints:
#
# Base case:
#     root is None
#
# Leaf condition:
#     root.left is None
#     AND
#     root.right is None
#
# Otherwise:
#
#     count leaves in left subtree
#     +
#     count leaves in right subtree
#
# WRITE YOUR SOLUTION BELOW: