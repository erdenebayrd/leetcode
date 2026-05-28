# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # time: O(N)
        # space: O(N)
        # method: recursion

        # if not p and not q:
        #     return True
        
        # if not p or not q or p.val != q.val:
        #     return False
        
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        """
            string matching using serialize
        """

        def serialize(node: Optional[TreeNode]) -> str:
            stack = [node]
            result = []
            while stack:
                node = stack.pop()
                value = "#"
                if node:
                    stack.append(node.right)
                    stack.append(node.left)
                    value = str(node.val)
                result.append(value)
            return ",".join(result)
    
        p = serialize(p)
        q = serialize(q)
        return p == q