# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        adj = {}

        def connect(u, v):
            if u not in adj:
                adj[u] = []
            adj[u].append(v)
            if v not in adj:
                adj[v] = []
            adj[v].append(u)

        def dfs(curNode, p):
            if curNode.left is not None:
                connect(p, 2 * p)
                dfs(curNode.left, 2 * p)
            if curNode.right is not None:
                connect(p, 2 * p + 1)
                dfs(curNode.right, 2 * p + 1)
        
        dfs(root, 1)
        
        curNode, curLvl = 0, 0
        def dfs2(v, par, lvl):
            if v not in adj:
                adj[v] = []
            nonlocal curNode
            nonlocal curLvl
            if curLvl < lvl:
                curLvl = lvl
                curNode = v
            for ch in adj[v]:
                if ch == par:
                    continue
                dfs2(ch, v, lvl + 1)
        
        dfs2(1, 0, 1)
        dfs2(curNode, 0, 1)
        return curLvl - 1