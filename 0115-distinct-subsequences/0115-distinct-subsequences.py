class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # time: O(N ^ 2)
        # space: O(N ^ 2)
        # method: DP
        n = len(s)
        m = len(t)

        @cache
        def count(i: int, j: int) -> int:
            if j >= m:
                return 1
            if i >= n:
                return 0
            result = count(i + 1, j) # skipping
            if s[i] == t[j]:
                result += count(i + 1, j + 1)
            return result
        
        return count(0, 0)