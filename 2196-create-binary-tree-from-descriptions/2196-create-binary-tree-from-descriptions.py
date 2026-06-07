# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = {}
        not_root_nodes = set()
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            
            if is_left == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            not_root_nodes.add(child)
        
        for parent, _, _ in descriptions:
            if parent not in not_root_nodes:
                return nodes[parent]
        return None