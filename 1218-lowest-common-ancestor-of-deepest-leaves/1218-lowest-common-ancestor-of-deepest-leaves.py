# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        N = int(1e3) + 1
        par = [-1] * N
        deep = [-1] * N
        def dfs(curNode, curPar, curLvl):
            par[curNode.val] = curPar
            deep[curNode.val] = curLvl
            if curNode.left is not None:
                dfs(curNode.left, curNode.val, curLvl + 1)
            if curNode.right is not None:
                dfs(curNode.right, curNode.val, curLvl + 1)
        dfs(root, -1, 0)
        deepestNodes = []
        mxDeep = max(deep)
        for node, lvl in enumerate(deep):
            if mxDeep == lvl:
                deepestNodes.append(node)
        def findLca():
            assert len(deepestNodes) > 0
            while True:
                flag = True
                for i in range(1, len(deepestNodes)):
                    flag &= (deepestNodes[i] == deepestNodes[i - 1])
                if flag is True:
                    break
                for i in range(len(deepestNodes)):
                    deepestNodes[i] = par[deepestNodes[i]]
            return deepestNodes[0]
        lca = findLca()
        res = None
        def dfs2(cur):
            nonlocal res
            if cur.val == lca:
                res = cur
                return
            if cur.left is not None:
                dfs2(cur.left)
            if cur.right is not None:
                dfs2(cur.right)
        dfs2(root)
        return res