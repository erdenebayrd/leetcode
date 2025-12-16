# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def calc(cur: Optional[TreeNode]) -> [int, int]:
            if cur.left is None and cur.right is None:
                return [0, cur.val]
            leftVal = [0, 0]
            rightVal = [0, 0]
            if cur.left is not None:
                leftVal = calc(cur.left)
            if cur.right is not None:
                rightVal = calc(cur.right)
            return [max(leftVal) + max(rightVal), cur.val + leftVal[0] + rightVal[0]]
        
        return max(calc(root))
