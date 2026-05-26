# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        stack = [root]
        encoder = []
        while stack:
            node = stack.pop()
            if node:
                encoder.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                encoder.append("#") # means null
        encoded_string = ",".join(encoder)
        return encoded_string
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        encoder = data.split(",")
        if encoder[0] == "#":
            return None
        root = TreeNode(int(encoder[0]))
        stack = [(root, "R"), (root, "L")]
        for value in encoder[1:]:
            parent, side = stack.pop()
            if value == "#": # Null
                continue
            node = TreeNode(int(value))
            if side == "L": # left child of parent
                parent.left = node
            else: # right child of parent
                parent.right = node
            stack.append((node, "R"))
            stack.append((node, "L"))
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans