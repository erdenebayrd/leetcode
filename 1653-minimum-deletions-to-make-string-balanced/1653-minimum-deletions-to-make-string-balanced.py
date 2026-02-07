class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        suffixA = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixA[i] += suffixA[i + 1] + int(s[i] == 'a')
        
        @cache
        def solve(index: int) -> int:
            if index >= n:
                return 0
            res = float('inf')
            if s[index] == 'b':
                res = min(res, suffixA[index])
                res = min(res, 1 + solve(index + 1))
            else:
                res = min(res, solve(index + 1))
            return res
        
        return solve(0)