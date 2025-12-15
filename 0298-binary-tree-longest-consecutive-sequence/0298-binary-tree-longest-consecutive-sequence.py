# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(cur) -> int:
            if cur is None:
                return 0
            leftVal = dfs(cur.left)
            rightVal = dfs(cur.right)
            curRes = 1
            if cur.left is not None and cur.left.val - 1 == cur.val:
                leftVal += 1
                curRes = max(curRes, leftVal)
            if cur.right is not None and cur.right.val - 1 == cur.val:
                rightVal += 1
                curRes = max(curRes, rightVal)
            nonlocal res
            res = max(res, curRes)
            return curRes
        dfs(root)
        return res