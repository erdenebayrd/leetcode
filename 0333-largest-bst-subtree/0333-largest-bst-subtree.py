# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def dfs(self, cur) -> [int, int, int, bool]:
        maxValue = cur.val
        minValue = cur.val
        size = 1
        flag = True
        if cur.left is not None:
            mx, mn, sz, fg = self.dfs(cur.left)
            size += sz
            maxValue = max(maxValue, mx)
            minValue = min(minValue, mn)
            flag &= (mx < cur.val) & fg
        if cur.right is not None:
            mx, mn, sz, fg = self.dfs(cur.right)
            size += sz
            maxValue = max(maxValue, mx)
            minValue = min(minValue, mn)
            flag &= (cur.val < mn) & fg
        if flag is True:
            self.res = max(self.res, size)
        return maxValue, minValue, size, flag
        
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.dfs(root)
        return self.res