# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float('-inf')
        def maxSum(cur: Optional[TreeNode]) -> int:
            if not cur:
                return float("-inf")
            leftMax = maxSum(cur.left)
            rightMax = maxSum(cur.right)
            self.result = max(self.result, leftMax + cur.val)
            self.result = max(self.result, rightMax + cur.val)
            self.result = max(self.result, cur.val)
            self.result = max(self.result, leftMax + rightMax + cur.val)
            currentMax = max(leftMax, rightMax)
            currentMax = max(currentMax + cur.val, cur.val)
            return currentMax
        maxSum(root)
        return self.result