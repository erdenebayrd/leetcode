from functools import cache

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        @cache
        def suffixZeros(index: int) -> int:
            if index >= n:
                return 0
            return int(s[index] == '0') + suffixZeros(index + 1)

        @cache
        def solve(index: int) -> int:
            if index >= n:
                return 0
            if s[index] == '1':
                result = suffixZeros(index)
                result = min(result, 1 + solve(index + 1))
            else:
                result = solve(index + 1)
            return result
        
        return solve(0)