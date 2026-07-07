# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        # time: O(N)
        # space: O(N)
        # method: 2 passes copying binary tree then connecting random nodes using dictionary
        if not root:
            return None
        head = NodeCopy(val=root.val)
        bridge = {}
        bridge[root] = head

        stack = [(root.left, root, "l"), (root.right, root, "r")]
        while stack:
            node, parent, child = stack.pop()
            if not node:
                continue
            
            copied_node = NodeCopy(val=node.val)
            bridge[node] = copied_node
            if child == "l":
                bridge[parent].left = copied_node
            else:
                bridge[parent].right = copied_node
            
            stack.append((node.left, node, 'l'))
            stack.append((node.right, node, 'r'))
        
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.random:
                bridge[node].random = bridge[node.random]
            stack.append(node.left)
            stack.append(node.right)
        return head