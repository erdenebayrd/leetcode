# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # time: O(N)
        # space: O(h) height of the tree
        # method: dfs
        def check(first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
            if first is None and second is None:
                return True
            if first is None or second is None:
                return False
            if first.val != second.val:
                return False
            result = True
            result &= check(first.left, second.right)
            result &= check(first.right, second.left)
            return result
        return check(root, root)