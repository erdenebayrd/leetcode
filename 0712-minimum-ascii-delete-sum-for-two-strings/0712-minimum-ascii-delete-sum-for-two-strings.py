class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        @cache
        def asciiSum(idx: int, s: int) -> int:
            if s == 0: # s1
                if idx >= n:
                    return 0
                return ord(s1[idx]) + asciiSum(idx + 1, s)
            if idx >= m:
                return 0
            return ord(s2[idx]) + asciiSum(idx + 1, s)

        @cache
        def solve(i: int, j: int) -> int:
            if i >= n or j >= m:
                return asciiSum(i, 0) + asciiSum(j, 1)
            res = min(ord(s2[j]) + solve(i, j + 1), ord(s1[i]) + solve(i + 1, j))
            if s1[i] == s2[j]:
                res = min(res, solve(i + 1, j + 1))
            return res
        return solve(0, 0)