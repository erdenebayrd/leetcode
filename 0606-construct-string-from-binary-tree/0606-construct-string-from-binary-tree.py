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
        if not root:
            return ""
        out = []

        def dfs(node: TreeNode) -> None:
            out.append(str(node.val))
            if node.left:
                out.append("(")
                dfs(node.left)
                out.append(")")
            elif node.right:
                out.append("()")
            if node.right:
                out.append("(")
                dfs(node.right)
                out.append(")")

        dfs(root)
        return "".join(out)