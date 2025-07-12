# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        res = None
        found = False
        def dfs(cur: TreeNode) -> None:
            nonlocal res
            nonlocal found
            if not cur:
                return
            dfs(cur.left)
            if found is True and res is None:
                res = cur
            if p.val == cur.val:
                found = True
            dfs(cur.right)
        dfs(root)
        return res