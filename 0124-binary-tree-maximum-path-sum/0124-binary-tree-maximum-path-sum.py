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
        le, ri = 0, 0
        if cur.left is not None:
            le = max(le, self.dfs(cur.left))
        if cur.right is not None:
            ri = max(ri, self.dfs(cur.right))
        self.res = max(self.res, le + ri + cur.val)
        return max(le + cur.val, ri + cur.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res