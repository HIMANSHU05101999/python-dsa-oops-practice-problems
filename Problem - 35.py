# ============================================================
# RECURSION + DSA EXERCISE 12 — Linked List Length
# ============================================================
#
# Using the Node class from the previous exercise,
# write:
#
# linked_list_length(node)
#
# It should return the number of nodes.
#
# Example:
#
# 10 -> 20 -> 30 -> None
#
# linked_list_length(node1)
#
# returns:
# 3
#
# Hints:
#
# If node is None:
#     there are 0 nodes.
#
# Otherwise:
#
#     1 + length of the remaining list
#
# WRITE YOUR SOLUTION BELOW:

class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

def print_length_nodes(node):
    if node == None:
        return 0
    return print_length_nodes(node.next) + 1

if __name__=="__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    node1.next = node2
    node2.next = node3

    print(print_length_nodes(node1))