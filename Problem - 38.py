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

class Node:
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

def count_node(node: Node):
    if node==None:
        return 0
    sum_node=1+count_node(node.left)+count_node(node.right)
    return sum_node

if __name__=="__main__":
    root=Node(10)
    root.left=Node(5)
    root.left.left=Node(2)
    root.left.right=Node(7)
    root.right=Node(15)

    print(count_node(root))