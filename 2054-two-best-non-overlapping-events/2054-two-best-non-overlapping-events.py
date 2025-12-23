class SegmentTree:
    def __init__(self, values: List[int]) -> None:
        self.arr = values
        self.n = len(values)
        self.st = [0] * 4 * self.n
        self.build(1, 0, self.n - 1)

    def build(self, p: int, l: int, r: int) -> None:
        if l == r:
            self.st[p] = self.arr[r]
            return
        self.build(2 * p, l, (l + r) // 2)
        self.build(2 * p + 1, (l + r) // 2 + 1, r)
        self.st[p] = max(self.st[2 * p], self.st[2 * p + 1])
    
    def getMax(self, p: int, l: int, r: int, L: int, R: int) -> int:
        if l > r or l > R or r < L:
            return int(-2e6)
        if l >= L and r <= R:
            return self.st[p]
        leftValue = self.getMax(2 * p, l, (l + r) // 2, L, R)
        rightValue = self.getMax(2 * p + 1, (l + r) // 2 + 1, r, L, R)
        return max(leftValue, rightValue)

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        # print(events)
        n = len(events)
        segTree = SegmentTree([val for _, _, val in events])
        
        def findLeftMostIdxAfter(endTime: int) -> int:
            lo, hi = -1, n
            while lo + 1 < hi:
                md = (lo + hi) // 2
                startTime, _, _ = events[md]
                if startTime <= endTime:
                    lo = md
                else:
                    hi = md
            return hi

        res = 0
        for i in range(n):
            _, endTime, value = events[i]
            le = findLeftMostIdxAfter(endTime)
            # print(i, le)
            res = max(res, value + segTree.getMax(1, 0, n - 1, le, n - 1), value)
        return res