# ============================================================
# RECURSION + DSA EXERCISE 15 — Count Tree Nodes
# ============================================================
#
# Using the same binary tree structure, write:
#
# count_nodes(root)
#
# It should return the total number of nodes.
#
# Example tree:
#
#             10
#            /  \
#           5    15
#          / \
#         2   7
#
# count_nodes(root)
#
# returns:
# 5
#
# Hints:
#
# What should an empty tree contain?
#
# If root is None:
#     return 0
#
# Otherwise:
#
#     1
#     + nodes in left subtree
#     + nodes in right subtree
#
# WRITE YOUR SOLUTION BELOW: