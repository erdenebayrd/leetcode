# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        # @cache
        def dfs(cur) -> int:
            res = cur.val
            if cur.left is not None:
                res += dfs(cur.left)
            if cur.right is not None:
                res += dfs(cur.right)
            return res
        total = dfs(root)
        if total & 1:
            return False
        half = total // 2
        
        def check(cur, isRoot: False) -> bool:
            if dfs(cur) == half and isRoot is False:
                return True
            res = False
            if cur.left is not None:
                res |= check(cur.left, False)
            if cur.right is not None:
                res |= check(cur.right, False)
            return res
        return check(root, True)