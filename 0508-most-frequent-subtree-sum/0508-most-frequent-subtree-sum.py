from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # time: O(N)
        # space: O(N)
        # method: DFS
        if not root:
            return []

        def dfs(node: Optional[TreeNode], frequency: defaultdict) -> int:
            if not node:
                return 0
            node.total = dfs(node.left, frequency) + dfs(node.right, frequency) + node.val
            frequency[node.total] += 1
            return node.total
        
        freq = defaultdict(int)
        dfs(root, freq)
        
        max_freq = 0
        for subtree_sum in freq:
            max_freq = max(max_freq, freq[subtree_sum])
        
        result = []
        for subtree_sum in freq:
            if max_freq == freq[subtree_sum]:
                result.append(subtree_sum)
        return result
        