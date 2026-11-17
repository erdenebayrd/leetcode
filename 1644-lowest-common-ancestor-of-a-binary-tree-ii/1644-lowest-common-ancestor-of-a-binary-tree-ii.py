# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # time: O(N)
        # space: O(N)
        # method: DFS
        parent = {}
        def dfs(node: "TreeNode" | None, par: "TreeNode" | None) -> None:
            if not node:
                return

            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        if p not in parent or q not in parent:
            return None
        
        parents = set()
        while p:
            parents.add(p)
            p = parent[p]
        
        while q:
            if q in parents:
                return q
            q = parent[q]