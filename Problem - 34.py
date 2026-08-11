# ============================================================
# RECURSION + DSA EXERCISE 11 — Linked List Node
# ============================================================
#
# Create a class named Node.
#
# Each Node should contain:
#
# - value
# - next
#
# Example:
#
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
#
# node1.next = node2
# node2.next = node3
#
# This represents:
#
# 10 -> 20 -> 30 -> None
#
#
# Then write a recursive function:
#
# print_nodes(node)
#
# which prints every value in the linked list.
#
# Example output:
#
# 10
# 20
# 30
#
# Hints:
#
# The base case is when node is None.
#
# Otherwise:
#
# 1. print node.value
# 2. recursively process node.next
#
# WRITE YOUR SOLUTION BELOW:

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def print_nodes(node):
    if node==None:
        return
    print(node.val)
    return print_nodes(node.next)


if __name__=="__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    node1.next = node2
    node2.next = node3

    print_nodes(node1)