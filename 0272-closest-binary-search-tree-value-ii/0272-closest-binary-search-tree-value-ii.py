# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        arr = []
        def dfs(cur):
            if not cur:
                return
            arr.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        diff = []
        for x in arr:
            diff.append(abs(float(x) - target))
        pairs = []
        for i in range(len(diff)):
            pairs.append((diff[i], arr[i]))
        pairs.sort()
        res = []
        for i in range(k):
            res.append(pairs[i][1])
        return res
