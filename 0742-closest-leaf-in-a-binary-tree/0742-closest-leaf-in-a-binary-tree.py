from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode | None, k: int) -> int:
        # time: O(n)
        # space: O(n)
        # method: dfs/bfs

        leaves = deque()
        adj = defaultdict(list)
        seen = set()

        def dfs(node, parent):
            if not node:
                return

            if node and parent:
                adj[node].append(parent)
                adj[parent].append(node)

            dfs(node.left, node)
            dfs(node.right, node)

            if not node.left and not node.right: # leaf node
                leaves.append((node, node))
                seen.add(node)
            
        dfs(root, None)
        
        while leaves:
            node, leaf = leaves.popleft()
            if node.val == k:
                return leaf.val

            for neighbor in adj[node]:
                if neighbor not in seen:
                    leaves.append((neighbor, leaf))
                    seen.add(neighbor)
        
        return 0