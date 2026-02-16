# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            result = [
            0    [3]
            1.   [9, 20]
            2.   [15, 7]
            ]

            0        3
                /   \   
            1     9     20
                    /   \
            2         15    7
        """
        # time: O(N) number of vertices
        # space O(N) we store every single node value into the result array

        def getDeepestLevel(node: Optional[TreeNode], currentLevel: int) -> int:
            if not node:
                return currentLevel - 1
            leftLevel = getDeepestLevel(node.left, currentLevel + 1)
            rightLevel = getDeepestLevel(node.right, currentLevel + 1)
            return max(leftLevel, rightLevel)
        
        level = getDeepestLevel(root, 0)
        result = [[] for _ in range(level + 1)]

        def buildOrder(node: Optional[TreeNode], currentLevel: int) -> None:
            if not node:
                return
            result[currentLevel].append(node.val)
            buildOrder(node.left, currentLevel + 1)
            buildOrder(node.right, currentLevel + 1)

        buildOrder(root, 0)
        return result