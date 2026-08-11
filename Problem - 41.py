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

class Node:
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

def tree_contains(node: Node, tagret):
    result1=False
    result2=False
    if node==None:
        return False
    if node.value==tagret:
        return True
    
    if node.left:
        result1=tree_contains(node.left,tagret)
    if result1==False:
        result2=tree_contains(node.right,tagret)

    if result1==True or result2==True:
        return True
    return False
    
    
if __name__=="__main__":
    root=Node(10)
    root.left=Node(5)
    root.left.left=Node(2)
    root.left.right=Node(7)
    root.right=Node(15)

    print(tree_contains(root,12))
