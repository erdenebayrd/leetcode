# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')
        def maxSum(cur: Optional[TreeNode]) -> int:
            nonlocal result
            if not cur:
                return float("-inf")
            leftMax = maxSum(cur.left)
            rightMax = maxSum(cur.right)
            result = max(result, leftMax + cur.val)
            result = max(result, rightMax + cur.val)
            result = max(result, cur.val)
            result = max(result, leftMax + rightMax + cur.val)
            currentMax = max(leftMax, rightMax)
            currentMax = max(currentMax + cur.val, cur.val)
            return currentMax
        maxSum(root)
        return result