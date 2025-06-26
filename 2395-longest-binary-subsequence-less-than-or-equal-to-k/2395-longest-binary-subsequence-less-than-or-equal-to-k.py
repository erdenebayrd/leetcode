class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        res = len(s) - Counter(s)["1"]
        for i in range(min(32, n)):
            if s[n - 1 - i] == "1":
                k -= (1 << i)
                if k < 0:
                    break
                res += 1
        return res