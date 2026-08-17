# ============================================================
# RECURSION + DSA EXERCISE 19 — Inorder Traversal
# ============================================================
#
# Write:
#
# inorder(root)
#
# The function should print nodes in this order:
#
# LEFT -> ROOT -> RIGHT
#
# Example:
#
#             10
#            /  \
#           5    15
#          / \
#         2   7
#
# Output:
#
# 2
# 5
# 7
# 10
# 15
#
# Hints:
#
# 1. Recursively visit left
# 2. Print root
# 3. Recursively visit right
#
# WRITE YOUR SOLUTION BELOW:

class Node:
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

def inorder(root):
    if root == None:
        return

    if root.left:
        inorder(root.left)
        
    print(root.value)

    if root.right:
        inorder(root.right)

    


if __name__=="__main__":
    root=Node(10)
    root.left=Node(5)
    root.left.left=Node(2)
    root.left.right=Node(7)
    root.right=Node(15)

    inorder(root)