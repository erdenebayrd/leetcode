class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        for x in s:
            if len(res) >= 2 and res[-1] == res[-2] and res[-1] == x:
                continue
            res += x
        return res