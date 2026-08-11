# ============================================================
# RECURSION + DSA EXERCISE 13 — Linked List Search
# ============================================================
#
# Write:
#
# find_node(node, target)
#
# It should return True if target exists in the linked list.
#
# Example:
#
# 10 -> 20 -> 30 -> None
#
# find_node(node1, 20)
# -> True
#
# find_node(node1, 50)
# -> False
#
# Hints:
#
# Base case:
#     node is None
#
# If node.value == target:
#     True
#
# Otherwise:
#     recursively search node.next
#
# WRITE YOUR SOLUTION BELOW:

class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next

def find_node(node, target):
    if node == None:
        return False

    if node.val==target:
        return True
    
    return find_node(node.next,target)
    
    

if __name__=="__main__":
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)

    node1.next = node2
    node2.next = node3

    print(find_node(node1,60))
