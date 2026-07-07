"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""
# time: O(N)
# space: O(h) height of the tree
# method: DFS
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        children = []
        for child in root.children:
            children.append(self.cloneTree(child))
        copied_node = Node(val=root.val, children=children)
        
        return copied_node