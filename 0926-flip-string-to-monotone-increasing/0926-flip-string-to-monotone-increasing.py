from functools import cache

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        ones = 0
        for i in range(n):
            ones += int(s[i] == '1')
        result = n - ones # all 1's
        zeros = 0
        for i in range(n): # until "i" all zeros after "i" all 1s
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            result = min(result, n - ones - zeros)
        return result
