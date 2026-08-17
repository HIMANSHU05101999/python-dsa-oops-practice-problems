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

class Node:
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

def count_leaves(root):
    val=0
    if root == None:
        return 0
    if not root.left and not root.right:
        return 1
    if root.left:
            val+=count_leaves(root.left)
    if root.right:
            val+=count_leaves(root.right)
    return val
            
    
if __name__=="__main__":
    root=Node(10)
    root.left=Node(5)
    root.left.left=Node(2)
    root.left.right=Node(7)
    root.right=Node(15)

    print(count_leaves(root))