# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(cur, parentVal: int, curLength: int) -> None:
            if not cur:
                return 0
            if parentVal + 1 == cur.val:
                curLength += 1
            else:
                curLength = 1
            self.res = max(self.res, curLength)
            dfs(cur.left, cur.val, curLength)
            dfs(cur.right, cur.val, curLength)
        dfs(root, float("-inf"), 1)
        return self.res