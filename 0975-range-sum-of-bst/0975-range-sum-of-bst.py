# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, cur: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        if low <= cur.val <= high:
            res += cur.val
        if cur.left is not None:
            res += self.dfs(cur.left, low, high)
        if cur.right is not None:
            res += self.dfs(cur.right, low, high)
        return res

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high)
