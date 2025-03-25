# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # left, level, idx, val
        arr = []
        idx = 0
        def dfs(cur, left, level):
            nonlocal idx
            arr.append((left, level, idx, cur.val))
            idx += 1
            if cur.left is not None:
                dfs(cur.left, left - 1, level + 1)
            if cur.right is not None:
                dfs(cur.right, left + 1, level + 1)
        dfs(root, 0, 0)
        arr.sort()
        group = defaultdict(list)
        for left, _, _, val in arr:
            group[left].append(val)
        res = []
        for key in group:
            res.append(group[key])
        return res