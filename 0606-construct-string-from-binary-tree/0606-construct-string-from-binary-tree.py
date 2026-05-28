# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
            tree hash/AHU
        """
        
        def dfs(node: TreeNode) -> str:
            if node.left and node.right:
                return f"({str(node.val)}{dfs(node.left)}{dfs(node.right)})"
            elif node.left and not node.right:
                return f"({str(node.val)}{dfs(node.left)})"
            elif not node.left and node.right:
                return f"({str(node.val)}(){dfs(node.right)})"
            return f"({str(node.val)})"
        
        result = dfs(root)
        return result[1:-1]