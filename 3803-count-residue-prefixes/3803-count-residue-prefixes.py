class Solution:
    def residuePrefixes(self, s: str) -> int:
        res = 0
        seen = set()
        for i in range(len(s)):
            seen.add(s[i])
            res += int((i + 1) % 3 == len(seen))
        return res