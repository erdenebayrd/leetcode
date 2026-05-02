# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, current: Optional[TreeNode], target: int) -> int:
        if not current:
            return 0
        target -= current.val
        result = 0
        if target == 0:
            result += 1
        result += self.dfs(current.left, target)
        result += self.dfs(current.right, target)
        return result
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        result = self.dfs(root, targetSum)
        result += self.pathSum(root.left, targetSum)
        result += self.pathSum(root.right, targetSum)
        return result