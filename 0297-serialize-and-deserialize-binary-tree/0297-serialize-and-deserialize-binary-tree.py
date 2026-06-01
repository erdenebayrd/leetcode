from typing import Optional

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        encoded = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                encoded.append("#")
                continue
            
            encoded.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return ",".join(encoded)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        encoded = data.split(",")
        if len(encoded) <= 1 or encoded[0] == "#": # Null
            return
        root = TreeNode(int(encoded[0]))
        stack = [(root, "R"), (root, "L")]
        for value in encoded[1:]:
            parent, side = stack.pop()
            if value == "#": # Null
                continue
            node = TreeNode(int(value))
            if side == "L":
                parent.left = node
            else:
                parent.right = node
            stack.append((node, "R"))
            stack.append((node, "L"))
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))