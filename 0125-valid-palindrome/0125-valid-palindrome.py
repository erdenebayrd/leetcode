class Solution:
    def isPalindrome(self, s: str) -> bool:
        # time: O(N)
        # space: O(1)
        # method: 2 pointers

        s = s.lower()

        left, right = 0, len(s) - 1
        while left < right:
            if s[left].isalnum() is False:
                left += 1
                continue

            if s[right].isalnum() is False:
                right -= 1
                continue
            
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True