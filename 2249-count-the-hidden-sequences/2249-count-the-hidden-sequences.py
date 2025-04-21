class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # time: O(N)
        # space: O(1)
        n = len(differences)
        m = n + 1
        res = 0
        hidden = 0
        mn = 0
        mx = 0
        for i in range(1, m):
            hidden = differences[i - 1] + hidden
            mn = min(mn, hidden)
            mx = max(mx, hidden)
        delta = lower - mn
        res = max(res, upper - mx - delta + 1)
        return res