class Solution:
    def validPalindrome(self, s: str) -> bool:
        def solve(le: int, ri: int, chance: int) -> bool:
            if le >= ri:
                return True
            if s[le] != s[ri]:
                if chance > 0:
                    return solve(le + 1, ri, 0) | solve(le, ri - 1, 0)
                return False
            return solve(le + 1, ri - 1, chance)
        return solve(0, len(s) - 1, 1)
        