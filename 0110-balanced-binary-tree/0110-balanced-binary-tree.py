# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time: O(N) visiting every node
    # space: O(Log N) as I added "depth" integer as a parameter. It'll be created every function calls, and deleted when function end.
    def isBalanced(self, root: Optional[TreeNode], depth: int = 0) -> bool:
        if not root:
            return True
        result = self.isBalanced(root.left, depth + 1) & self.isBalanced(root.right, depth + 1)
        if result is False:
            return False
        leftDepth = depth if root.left is None else root.left.val
        rightDepth = depth if root.right is None else root.right.val
        result &= (abs(leftDepth - rightDepth) <= 1)
        root.val = max(leftDepth, rightDepth)
        return result