# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def deepest(cur: Optional[TreeNode], level: int) -> int:
            if cur is None:
                return 0
            deep = level
            deep = max(deep, deepest(cur.left, level + 1))
            deep = max(deep, deepest(cur.right, level + 1))
            return deep
        deep = deepest(root, 0)
        self.res = -1
        def dfs(cur: Optional[TreeNode], deep: int, cnt: int) -> int:
            if cur is None:
                return 0
            if deep == 0:
                if cnt == 1 and self.res == -1:
                    self.res = cur
                return 1
            res = dfs(cur.left, deep - 1, cnt)
            res += dfs(cur.right, deep - 1, cnt)
            if cnt == res and self.res == -1:
                self.res = cur
            return res
        cnt = dfs(root, deep, 0)
        self.res = -1
        dfs(root, deep, cnt)
        return self.res
        
        