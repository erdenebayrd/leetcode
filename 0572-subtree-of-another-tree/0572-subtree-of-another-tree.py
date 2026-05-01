# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time: O( len(root) * len(subRoot) )
    # space: O(log(len(root)))
    # method: DFS

    def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool: # O(N) N is the size of minimum tree (nodes)
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2 or tree1.val != tree2.val:
            return False
        return self.isSameTree(tree1.left, tree2.left) & self.isSameTree(tree1.right, tree2.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) | self.isSubtree(root.right, subRoot)