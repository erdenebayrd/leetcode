# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = int(-1e9)

    def dfs(self, cur) -> int:
        if cur is None:
            return 0
        le = max(self.dfs(cur.left), 0)
        ri = max(self.dfs(cur.right), 0)
        self.res = max(self.res, le + ri + cur.val)
        return max(le + cur.val, ri + cur.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res