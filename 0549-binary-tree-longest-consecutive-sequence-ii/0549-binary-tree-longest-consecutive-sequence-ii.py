# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def initDpTree(currentNode: Optional[TreeNode]) -> None:
            if not currentNode:
                return
            currentNode.increasing = 0
            currentNode.decreasing = 0
            initDpTree(currentNode.left)
            initDpTree(currentNode.right)
        
        initDpTree(root)
        self.longest = 0
        def calculateDpTree(currentNode: Optional[TreeNode]) -> None:
            if not currentNode:
                return
            calculateDpTree(currentNode.left)
            calculateDpTree(currentNode.right)
            # calculating "increasing" of currentNode
            if currentNode.left and currentNode.left.val - 1 == currentNode.val:
                currentNode.increasing = max(currentNode.increasing, currentNode.left.increasing)
            if currentNode.right and currentNode.right.val - 1 == currentNode.val:
                currentNode.increasing = max(currentNode.increasing, currentNode.right.increasing)
            currentNode.increasing += 1

            # calculating "decreasing" of currentNode
            if currentNode.left and currentNode.left.val + 1 == currentNode.val:
                currentNode.decreasing = max(currentNode.decreasing, currentNode.left.decreasing)
            if currentNode.right and currentNode.right.val + 1 == currentNode.val:
                currentNode.decreasing = max(currentNode.decreasing, currentNode.right.decreasing)
            currentNode.decreasing += 1

            # calculating "longest" of currentNode

            # decreasing to left
            if currentNode.left and currentNode.left.val + 1 == currentNode.val:
                self.longest = max(self.longest, 1 + currentNode.left.decreasing)
            # increasing to left
            if currentNode.left and currentNode.left.val - 1 == currentNode.val:
                self.longest = max(self.longest, 1 + currentNode.left.increasing)
            
            # decreasing to right
            if currentNode.right and currentNode.right.val + 1 == currentNode.val:
                self.longest = max(self.longest, 1 + currentNode.right.decreasing)
            # increasing to right
            if currentNode.right and currentNode.right.val - 1 == currentNode.val:
                self.longest = max(self.longest, 1 + currentNode.right.increasing)
            
            # decreasing left and increasing right
            if currentNode.left and currentNode.right and currentNode.left.val + 1 == currentNode.val == currentNode.right.val - 1:
                self.longest = max(self.longest, currentNode.left.decreasing + 1 + currentNode.right.increasing)
            # increasing left and decreasing right
            if currentNode.left and currentNode.right and currentNode.left.val - 1 == currentNode.val == currentNode.right.val + 1:
                self.longest = max(self.longest, currentNode.left.increasing + 1 + currentNode.right.decreasing)
            self.longest = max(self.longest, 1)
        calculateDpTree(root)

        return self.longest