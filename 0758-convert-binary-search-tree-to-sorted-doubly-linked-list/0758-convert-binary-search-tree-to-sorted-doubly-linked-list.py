"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        def dfs(cur):
            leftPointer = cur
            rightPointer = cur
            if cur.left is not None:
                leftMostPointer, rightMostPointer = dfs(cur.left)
                rightMostPointer.right = cur
                cur.left = rightMostPointer
                leftPointer = leftMostPointer
            if cur.right is not None:
                leftMostPointer, rightMostPointer = dfs(cur.right)
                cur.right = leftMostPointer
                leftMostPointer.left = cur
                rightPointer = rightMostPointer
            return leftPointer, rightPointer
        leftPointer, rightPointer = dfs(root)
        leftPointer.left = rightPointer
        rightPointer.right = leftPointer
        return leftPointer