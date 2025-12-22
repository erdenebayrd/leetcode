# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def solve(cur: Optional[TreeNode]):
            curLongest = {"inc": 0, "dec": 0}
            if cur is None:
                return curLongest
            leftLongest = solve(cur.left)
            rightLongest = solve(cur.right)
            if cur.left is not None:
                if cur.val + 1 == cur.left.val: # increasing
                    curLongest["inc"] = max(curLongest["inc"], leftLongest["inc"])
                elif cur.val - 1 == cur.left.val: # decreasing
                    curLongest["dec"] = max(curLongest["dec"], leftLongest["dec"])
            if cur.right is not None:
                if cur.val + 1 == cur.right.val: # increasing
                    curLongest["inc"] = max(curLongest["inc"], rightLongest["inc"])
                elif cur.val - 1 == cur.right.val: # decreasing
                    curLongest["dec"] = max(curLongest["dec"], rightLongest["dec"])
            curLongest["inc"] += 1 # adding it's own node count
            curLongest["dec"] += 1 # adding it's own node count
            self.res = max(self.res, curLongest["inc"])
            self.res = max(self.res, curLongest["dec"])
            if cur.left is not None and cur.right is not None:
                if cur.val + 1 == cur.left.val and cur.val - 1 == cur.right.val:
                    self.res = max(self.res, leftLongest["inc"] + 1 + rightLongest["dec"])
                elif cur.val - 1 == cur.left.val and cur.val + 1 == cur.right.val: 
                    self.res = max(self.res, leftLongest["dec"] + 1 + rightLongest["inc"])
            
            return curLongest
        
        solve(root)

        return self.res