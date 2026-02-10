from functools import cache

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        @cache
        def isPalindromic(left: int, right: int) -> bool:
            if left >= right:
                return True
            if s[left] == s[right]:
                return isPalindromic(left + 1, right - 1)
            return False
        
        longest = 0
        leftIndex, rightIndex = -1, -1
        for left in range(n):
            for right in range(left, n):
                if isPalindromic(left, right) is True:
                    if right - left + 1 > longest:
                        longest = right - left + 1
                        leftIndex, rightIndex = left, right
        isPalindromic.cache_clear()
        if leftIndex == -1:
            return ""
        return s[leftIndex:rightIndex + 1]