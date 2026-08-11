# ============================================================
# RECURSION + DSA EXERCISE 17 — Maximum Tree Value
# ============================================================
#
# Write:
#
# tree_max(root)
#
# It should return the largest value in the tree.
#
# Example:
#
#             10
#            /  \
#           5    15
#          / \
#         2   7
#
# tree_max(root)
# -> 15
#
# Hints:
#
# Recursively find:
#
# - maximum in left subtree
# - maximum in right subtree
#
# Then compare those values with root.value.
#
# You may assume the tree is not empty.
#
# Do NOT use max().
#
# WRITE YOUR SOLUTION BELOW:

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

def max_node(node: Node):
    if node==None:
        return

    max=node.value
    if node.left:
        if max<max_node(node.left):
            max=max_node(node.left)

    if node.right:
            if max<max_node(node.right):
                max=max_node(node.right)
    return max

if __name__=="__main__":
    root=Node(10)
    root.left=Node(5)
    root.left.left=Node(2)
    root.left.right=Node(7)
    root.right=Node(15)

    print(max_node(root))
