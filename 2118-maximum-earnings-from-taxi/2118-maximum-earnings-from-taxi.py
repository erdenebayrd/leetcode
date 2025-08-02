class SegmentTree:
    def __init__(self, sz: int) -> None:
        self.st = [0] * 4 * (sz + 1)
    
    def setValue(self, p: int, l: int, r: int, idx: int, val: int) -> None:
        if l > r or l > idx or r < idx:
            return
        if l == r and l == idx:
            self.st[p] = val
            return
        self.setValue(2 * p, l, (l + r) // 2, idx, val)
        self.setValue(2 * p + 1, (l + r) // 2 + 1, r, idx, val)
        self.st[p] = max(self.st[2 * p], self.st[2 * p + 1])

    def rangeMax(self, p: int, l: int, r: int, L: int, R: int) -> int:
        if l > r or l > R or r < L:
            return 0
        if l >= L and r <= R:
            return self.st[p]
        v1 = self.rangeMax(2 * p, l, (l + r) // 2, L, R)
        v2 = self.rangeMax(2 * p + 1, (l + r) // 2 + 1, r, L, R)
        return max(v1, v2)

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        stObject = SegmentTree(n)
        dp = [0] * (n + 1)
        rides.sort(key=lambda x: x[1])
        rideIdx = 0
        for ri in range(1, n + 1):
            dp[ri] = max(dp[ri], dp[ri - 1])
            while rideIdx < len(rides) and ri == rides[rideIdx][1]:
                st, ed, tip = rides[rideIdx]
                val = stObject.rangeMax(1, 1, n, 1, st)
                dp[ri] = max(dp[ri], val + ed - st + tip)
                rideIdx += 1
            stObject.setValue(1, 1, n, ri, dp[ri])
        return dp[n]