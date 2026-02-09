# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.array = []
        
        def convertToArray(curr: Optional[TreeNode]) -> None:
            if not curr:
                return
            convertToArray(curr.left)
            self.array.append(curr.val) # in order travel which flats the given BST
            convertToArray(curr.right)

        convertToArray(root)

        def buildBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            cur = TreeNode(self.array[mid])
            cur.left = buildBST(left, mid - 1)
            cur.right = buildBST(mid + 1, right)
            return cur

        return buildBST(0, len(self.array) - 1)