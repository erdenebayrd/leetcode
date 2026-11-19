# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            node.val += dfs(node.left)
            node.val += dfs(node.right)
            return node.val
        
        total = dfs(root)
        if total & 1: # odd
            return False
        
        half = total // 2

        def find(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if node.val == half:
                return True
            return find(node.left) or find(node.right)
        
        return find(root.left) or find(root.right)
