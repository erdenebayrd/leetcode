from functools import cache

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        countOnes = 0
        flips = 0
        for ch in s:
            if ch == '1':
                countOnes += 1
            else: # ch == '0'
                flips = min(flips + 1, countOnes)
        return flips