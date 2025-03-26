class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # time: O(N * Log N)
        # space: O(N)
        # method: ternary search
        arr = []
        for row in grid:
            for col in row:
                arr.append(col)
        if len(arr) == 1:
            return 0
        arr.sort()
        n = len(arr)
        for i in range(1, n):
            if (arr[i] - arr[0]) % x != 0:
                return -1
        
        def calcCost(md: int) -> int:
            eq = md * x + arr[0]
            res = 0
            for i in range(n):
                res += abs(arr[i] - eq) // x
            return res

        lo, hi = -1, int((arr[-1] - arr[0]) / x) + 1
        while lo + 1 < hi:
            md = (lo + hi) // 2
            if calcCost(md) < calcCost(md + 1):
                hi = md
            else:
                lo = md
        return calcCost(hi)