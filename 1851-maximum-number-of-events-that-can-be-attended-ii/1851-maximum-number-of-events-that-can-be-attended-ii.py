class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        @cache
        def solve(idx: int, curK: int) -> int:
            if idx >= n or curK == 0:
                return 0
            res = solve(idx + 1, curK)
            le, ri, val = events[idx]
            lo, hi = idx, n
            while lo + 1 < hi:
                md = (lo + hi) // 2
                if ri < events[md][0]:
                    hi = md
                else:
                    lo = md
            res = max(res, val + solve(hi, curK - 1))
            return res
        return solve(0, k)