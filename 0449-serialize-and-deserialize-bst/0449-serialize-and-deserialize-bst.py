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
        def post_order(node: Optional[TreeNode]) -> List[str]:
            if not node:
                return []
            return post_order(node.left) + post_order(node.right) + [str(node.val)]
        
        encoded = ",".join(post_order(root))
        return encoded

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        encoded = data.split(",")

        def helper(low_limit: float, high_limit: float) -> Optional[TreeNode]:
            if not encoded or not (low_limit <= int(encoded[-1]) <= high_limit):
                return None
            value = encoded.pop()
            node = TreeNode(int(value))
            node.right = helper(node.val, high_limit)
            node.left = helper(low_limit, node.val)
            return node

        root = helper(float("-inf"), float("inf"))
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans