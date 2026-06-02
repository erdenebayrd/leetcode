"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        encoded = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                encoded.append(str(node.val))
                stack.append(None)
                for child in node.children[::-1]: # reversed order for stack
                    stack.append(child)
            else:
                encoded.append("#")
        return ",".join(encoded)

        
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if data == "":
            return None
        encoded = data.split(",")
        root = Node(int(encoded[0]))
        stack = [root]
        for value in encoded[1:]:
            parent = stack[-1]
            if value == "#":
                stack.pop()
                continue
            node = Node(int(value))
            parent.children.append(node)
            stack.append(node)
            
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))