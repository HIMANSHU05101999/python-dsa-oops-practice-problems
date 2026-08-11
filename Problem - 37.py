# ============================================================
# RECURSION + DSA EXERCISE 14 — Binary Tree Traversal
# ============================================================
#
# Create this Node class:
#
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
#
#
# Create this tree:
#
#             10
#            /  \
#           5    15
#          / \
#         2   7
#
#
# Write:
#
# print_nodes(root)
#
# It should print every node.
#
# Expected:
#
# 10
# 5
# 2
# 7
# 15
#
# Hints:
#
# 1. Print root.value
# 2. If root.left exists, recursively process it
# 3. If root.right exists, recursively process it
#
# WRITE YOUR SOLUTION BELOW:

class Node:
    def __init__(self, root, left=None, right=None):
        self.root=root
        self.left=left
        self.right=right


def print_node(root):
    if root==None:
        return

    print(root.root)

    if root.left:
        print_node(root.left)
        
    if root.right:
        print_node(root.right)

    


if __name__=="__main__":
    root=Node(10)
    root.left=Node(5)
    root.left.left=Node(2)
    root.left.right=Node(7)
    root.right=Node(15)

    print_node(root)
