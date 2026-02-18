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
        # -------------------------- Recursive --------------------------
        # tc: O(N * chances)
        # sc: O(N) at worst case recursive stack can reach N when its initially palindrome

        # def valid(left: int, right: int, chances: int) -> bool: #O ( N * chances) N is length of s
        #     if chances < 0:
        #         return False
        #     if left >= right:
        #         return True

        #     if s[left] == s[right]:
        #         return valid(left + 1, right - 1, chances)
        #     else:
        #         return valid(left + 1, right, chances - 1) | valid(left, right - 1, chances - 1)

        
        # result = valid(0, len(s) - 1, 1)
        # return result

        # -------------------------- Iterative --------------------------

        def isPalindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        chances = 1
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
            
        result = isPalindrome(left, right - 1)
        result |= isPalindrome(left + 1, right)
        return result