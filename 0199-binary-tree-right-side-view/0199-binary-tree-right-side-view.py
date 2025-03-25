# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        seen = [False] * 101
        def dfs(cur, deep):
            if cur is None:
                return
            if seen[deep] is False:
                seen[deep] = True
                res.append(cur.val)
            if cur.right is not None:
                dfs(cur.right, deep + 1)
            if cur.left is not None:
                dfs(cur.left, deep + 1)
        dfs(root, 0)
        return res