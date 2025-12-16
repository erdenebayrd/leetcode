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
            if not cur:
                return [0, 0]
            leftVal = calc(cur.left)
            rightVal = calc(cur.right)
            return [max(leftVal) + max(rightVal), cur.val + leftVal[0] + rightVal[0]]
        
        return max(calc(root))
