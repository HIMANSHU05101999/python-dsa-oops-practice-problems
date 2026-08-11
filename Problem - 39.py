# ============================================================
# RECURSION + DSA EXERCISE 16 — Sum Tree Values
# ============================================================
#
# Write:
#
# tree_sum(root)
#
# It should return the sum of all values in the tree.
#
# Example:
#
#             10
#            /  \
#           5    15
#          / \
#         2   7
#
# Result:
#
# 10 + 5 + 15 + 2 + 7 = 39
#
# tree_sum(root)
# -> 39
#
# Hints:
#
# Empty tree -> 0
#
# Otherwise:
#
# root.value
# + sum of left subtree
# + sum of right subtree
#
# WRITE YOUR SOLUTION BELOW:

class Node:
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

def sum_node(node: Node):
    if node==None:
        return 0
    
    sum=node.value+sum_node(node.left)+sum_node(node.right)
    return sum

if __name__=="__main__":
    root=Node(10)
    root.left=Node(5)
    root.left.left=Node(2)
    root.left.right=Node(7)
    root.right=Node(15)

    print(sum_node(root))
