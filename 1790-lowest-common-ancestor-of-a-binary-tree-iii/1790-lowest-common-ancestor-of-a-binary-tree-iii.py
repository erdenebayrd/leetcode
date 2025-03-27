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
        cnt = defaultdict(int)
        while p is not None:
            cnt[p.val] += 1
            p = p.parent
        while q is not None:
            cnt[q.val] += 1
            if cnt[q.val] == 2:
                return q
            q = q.parent