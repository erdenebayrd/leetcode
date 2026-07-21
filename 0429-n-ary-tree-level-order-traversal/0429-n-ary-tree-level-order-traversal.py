from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # time: O(N)
        # space: O(N)
        # method: BFS
        if not root:
            return []
        result = []
        queue = deque()
        queue.append((root, 0)) # level
        while queue:
            node, current_level = queue.popleft()
            if current_level == len(result):
                result.append([])
            result[current_level].append(node.val)
            for child in node.children:
                queue.append((child, current_level + 1))
        return result