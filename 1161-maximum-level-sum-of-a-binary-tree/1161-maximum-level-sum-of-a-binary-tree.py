# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        cnt = defaultdict(int)
        def dfs(cur: Optional[TreeNode], level: int) -> None:
            if cur is None:
                return
            cnt[level] += cur.val
            dfs(cur.left, level + 1)
            dfs(cur.right, level + 1)
        dfs(root, 1)
        return max(cnt, key=cnt.get)