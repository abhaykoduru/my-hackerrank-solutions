"""
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
"""

def Reverse(head):
"""
    Takes in the head of a single linked list.
    Returns the head of the new linked list after reversal
"""
    if head is None:
        return head
    else:
        current = head
        previous = Reverse(current.next)
        if previous:
            current.next.next = current
            current.next = None
            return previous
        else:
            return current
