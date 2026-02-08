# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode], depth: int = 0) -> bool:
        if not root:
            return True
        root.val = depth
        result = self.isBalanced(root.left, depth + 1) & self.isBalanced(root.right, depth + 1)
        if result is False:
            return False
        leftDepth = root.val if root.left is None else root.left.val
        rightDepth = root.val if root.right is None else root.right.val
        result &= (abs(leftDepth - rightDepth) <= 1)
        root.val = max(leftDepth, rightDepth)
        return result