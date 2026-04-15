class Solution:
    def checkPartitioning(self, s: str) -> bool:
        # time: O(N ^ 2)
        # space: O(N)
        # method: DP

        n = len(s)
        @cache
        def isPalindrome(left: int, right: int) -> bool:
            if left >= right:
                return True
            result = s[left] == s[right]
            result &= isPalindrome(left + 1, right - 1)
            return result

        @cache
        def solve(index: int, k: int) -> bool:
            if k == 0:
                return index == n
            result = False
            for right in range(index, n):
                if isPalindrome(index, right):
                    result |= solve(right + 1, k - 1)
            return result
        
        result = solve(0, 3)
        solve.cache_clear()
        isPalindrome.cache_clear()
        return result