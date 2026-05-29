# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        # time: O(N)
        # space: O(N)
        # method: DFS
        if not root:
            return 0
            
        def dfs(node: Optional[TreeNode]) -> tuple: # first value is boolean (all values are same or not), second value is int (total unival)
            if not node.left and not node.right: # leaf
                return (True, 1)
            if not node.left:
                is_uni_right, unival_right = dfs(node.right)
                is_uni = is_uni_right and node.val == node.right.val
                uni_val = unival_right + int(is_uni)
                return (is_uni, uni_val)
            if not node.right:
                is_uni_left, unival_left = dfs(node.left)
                is_uni = is_uni_left and node.val == node.left.val
                uni_val = unival_left + int(is_uni)
                return (is_uni, uni_val)
            is_uni_left, unival_left = dfs(node.left)
            is_uni_right, unival_right = dfs(node.right)
            is_uni = is_uni_left and is_uni_right and node.val == node.left.val and node.val == node.right.val
            uni_val = unival_left + unival_right + int(is_uni)
            return (is_uni, uni_val)
        
        _, unival = dfs(root)
        return unival