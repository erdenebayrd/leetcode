class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        m = n + 1
        res = 0
        hidden = [0] * m
        for i in range(1, m):
            hidden[i] = differences[i - 1] + hidden[i - 1]
        delta = lower - min(hidden)
        res = max(res, upper - max(hidden) - delta + 1)
        return res