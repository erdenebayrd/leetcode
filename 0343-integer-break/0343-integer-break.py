class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def solve(current: int) -> int:
            if current <= 1:
                return current
            res = 0
            for i in range(1, current + 1):
                res = max(res, i * max(current - i, solve(current - i)))
            return res
        
        return solve(n)