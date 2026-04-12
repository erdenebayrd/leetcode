class Solution:
    def strangePrinter(self, s: str) -> int:
        # time: O(N ^ 3)
        # space: O(N ^ 2)
        # method: DP

        n = len(s)

        @cache
        def solve(left: int, right: int) -> int:
            if left > right or left >= n:
                return 0
            result = 1 + solve(left + 1, right)
            for i in range(left + 1, right + 1):
                if s[left] == s[i]:
                    result = min(result, solve(left + 1, i - 1) + solve(i, right))
            return result
        
        return solve(0, n - 1)