# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0
        self.res = 0
        def dfs(cur: Optional[TreeNode]) -> int:
            if cur is None:
                return 0
            sub = cur.val
            sub += dfs(cur.left)
            sub += dfs(cur.right)
            self.res = max(self.res, (total - sub) * sub)
            return sub
        total = dfs(root)
        dfs(root)
        return self.res % 1_000_000_007