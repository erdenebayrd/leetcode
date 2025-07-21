class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        for x in s:
            if len(res) <= 1 or res[-1] != res[-2] or res[-1] != x:
                res += x
        return res