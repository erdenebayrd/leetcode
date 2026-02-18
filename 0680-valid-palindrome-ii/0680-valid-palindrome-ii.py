from functools import cache

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
                             a. c. c       chances=1
        left                 ^
        right                      ^
                         /.            \

                   a   c chances=0        c    c, chances = 0
        left       ^.  ^                  ^    ^ 
        right
        """        
        @cache
        def valid(left: int, right: int, chances: int) -> bool: #O ( N * chances) N is length of s
            if chances < 0:
                return False
            if left >= right:
                return True

            if s[left] == s[right]:
                return valid(left + 1, right - 1, chances)
            else:
                return valid(left + 1, right, chances - 1) | valid(left, right - 1, chances - 1)

        
        result = valid(0, len(s) - 1, 1)
        return result