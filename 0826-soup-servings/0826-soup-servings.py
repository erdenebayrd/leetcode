class Solution:
    def soupServings(self, n: int) -> float:
        if n == 0:
            return 0.5
        if n >= 4800:
            return 1.0
        arr = [(100, 0), (75, 25), (50, 50), (25, 75)]
        @cache
        def solve(a: int, b: int, p: float) -> float:
            if a <= 0 and b > 0:
                return p
            if a <= 0 or b <= 0:
                return 0
            res = 0
            for x, y in arr:
                res += solve(a - x, b - y, p * 0.25)
            return res
        res = solve(n, n, 1)
        @cache
        def solve2(a: int, b: int, p: float) -> float:
            if a <= 0 and b <= 0:
                return p
            if a <= 0 or b <= 0:
                return 0
            res = 0
            for x, y in arr:
                res += solve2(a - x, b - y, p * 0.25)
            return res
        
        res += solve2(n, n, 1) * 0.5
        return res