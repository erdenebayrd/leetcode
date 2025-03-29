class Solution:
    def partitionString(self, s: str) -> int:
        res, cnt = 1, 0
        for ch in s:
            x = ord(ch) - ord('a')
            if (cnt >> x) & 1:
                res += 1
                cnt = 1 << x
            cnt |= (1 << x)
        return res