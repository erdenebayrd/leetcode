class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        for i in range(min(32, n)):
            if s[n - 1 - i] == "1":
                k -= (1 << i)
                if k < 0:
                    break
                res += 1
        for ch in s:
            if ch == "0":
                res += 1
        return res