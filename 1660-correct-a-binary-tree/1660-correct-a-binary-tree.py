# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        # time: O(n)
        # space: O(n)
        # method: BFS

        def find_invalid_node(node):
            current_nodes = set([node])
            while current_nodes:
                next_nodes = set()
                for node in current_nodes:
                    if node.right and node.right in current_nodes:
                        return node
                    if node.left:
                        next_nodes.add(node.left)
                    if node.right:
                        next_nodes.add(node.right)
                current_nodes = next_nodes
            return None

        invalid_node = find_invalid_node(root)
        
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.right == invalid_node:
                node.right = None
                break
                
            if node.left == invalid_node:
                node.left = None
                break
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
        return root