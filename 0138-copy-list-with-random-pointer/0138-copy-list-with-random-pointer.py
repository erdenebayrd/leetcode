"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # time: O(N)
        # space: O(N)
        # method: mapping node address to new node address using dict
        if not head:
            return head
        
        bridge = {}
        current = head
        while current:
            copied_node = Node(current.val)
            bridge[current] = copied_node
            current = current.next
        
        current = head
        while current:
            copied_node = bridge[current]
            if current.next:
                copied_node.next = bridge[current.next]
            if current.random:
                copied_node.random = bridge[current.random]
            current = current.next
        return bridge[head]