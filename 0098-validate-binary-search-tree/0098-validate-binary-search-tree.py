# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(cur, low: int, high: int) -> bool:
            if cur is None:
                return True
            if cur.val <= low or cur.val >= high:
                return False
            return check(cur.left, low, cur.val) and check(cur.right, cur.val, high)
        return check(root, float('-inf'), float('inf'))