"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()
        while p is not None:
            seen.add(p.val)
            p = p.parent
        while q is not None:
            if q.val in seen:
                return q
            q = q.parent