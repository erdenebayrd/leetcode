class RollingHash:
    def __init__(self, text: str, base: int, mod: int) -> None:
        self.base = base
        self.mod = mod
        n = len(text)
        self.hash = []
        self.bases = [1]
        self.hash.append(ord(text[0]))
        for i in range(1, n):
            self.bases.append((self.bases[-1] * base) % mod)
            self.hash.append((self.hash[-1] * base + ord(text[i])) % mod)

    def getRangeHash(self, left: int, right: int) -> int:
        if left == 0:
            return self.hash[right]
        return (self.hash[right] - (self.hash[left - 1] * self.bases[right - left + 1]) % self.mod) % self.mod

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time: O( len(root) * len(subRoot) )
    # space: O(log(len(root)))
    # method: DFS

    # def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool: # O(N) N is the size of minimum tree (nodes)
    #     if not tree1 and not tree2:
    #         return True
    #     if not tree1 or not tree2 or tree1.val != tree2.val:
    #         return False
    #     return self.isSameTree(tree1.left, tree2.left) & self.isSameTree(tree1.right, tree2.right)

    def serialize(self, node: Optional[TreeNode]) -> str:
        if not node:
            return "#,"
        return f"^{node.val},{self.serialize(node.left)},{self.serialize(node.right)}"

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if not root:
        #     return False
        # if self.isSameTree(root, subRoot):
        #     return True
        # return self.isSubtree(root.left, subRoot) | self.isSubtree(root.right, subRoot)
        # time: O(N + M)
        # space: O(N + M)
        # method: string searching algo ( rolling hash )

        text = self.serialize(root)
        pattern = self.serialize(subRoot)
        # print(text)
        # print(pattern)
        textHash = RollingHash(text, 257, int(1e9 + 7))
        patternHash = RollingHash(pattern, 257, int(1e9 + 7))
        textHash1 = RollingHash(text, 37, int(1e9 + 9))
        patternHash1 = RollingHash(pattern, 37, int(1e9 + 9))
        for i in range(len(pattern) - 1, len(text)):
            left = i - len(pattern) + 1
            right = i
            if textHash.getRangeHash(left, right) == patternHash.getRangeHash(0, len(pattern) - 1) and textHash1.getRangeHash(left, right) == patternHash1.getRangeHash(0, len(pattern) - 1):
                return True
        return False