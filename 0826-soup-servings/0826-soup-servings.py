class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0
        n = (n + 24) // 25
        
        @cache
        def solve(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            res = 0
            for i in range(1, 5):
                res += solve(a - i, b - 4 + i)
            return res * 0.25

        return solve(n, n)