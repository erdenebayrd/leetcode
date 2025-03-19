class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cur = [0, 0, 0]
        n = len(s)
        le, ri = 0, 0
        res = 0
        while ri < n:
            idx = ord(s[ri]) - ord('a')
            cur[idx] += 1
            while cur[0] > 0 and cur[1] > 0 and cur[2] > 0:
                res += n - ri
                idx = ord(s[le]) - ord('a')
                cur[idx] -= 1
                le += 1
            ri += 1
        return res