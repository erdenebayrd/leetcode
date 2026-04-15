class Solution:
    def minCut(self, s: str) -> int:
        # time: O(N ^ 2)
        # space: O(N ^ 2)
        # method: DP
        @cache
        def isPalindrome(left: int, right: int) -> bool:
            if left >= right:
                return True
            result = s[left] == s[right]
            result &= isPalindrome(left + 1, right - 1)
            return result
        
        n = len(s)

        @cache
        def solve(index: int) -> int:
            if index >= n:
                return 0
            result = 1 + solve(index + 1)
            for right in range(index, n):
                if isPalindrome(index, right):
                    result = min(result, 1 + solve(right + 1))
            return result
        result = solve(0) - 1
        return result