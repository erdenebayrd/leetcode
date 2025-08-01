# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        cnt = 0
        def solve(colNum: int, cur: Optional[TreeNode], lvl: int):
            if not cur:
                return
            nonlocal res
            nonlocal cnt
            if colNum not in res:
                res[colNum] = []
            res[colNum].append((lvl, cnt, cur.val))
            cnt += 1
            solve(colNum - 1, cur.left, lvl + 1)
            solve(colNum + 1, cur.right, lvl + 1)
        solve(0, root, 0)
        answer = []
        for _, val in sorted(res.items()):
            cur = []
            for _, _, num in sorted(val):
                cur.append(num)
            answer.append(cur)
        return answer