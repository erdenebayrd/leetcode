class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        a1, a2 = 0, -int(1e9)
        for key in cnt:
            if cnt[key] & 1:
                a1 = max(a1, cnt[key])
            else:
                if a2 == -int(1e9):
                    a2 = cnt[key]
                a2 = min(a2, cnt[key])
        return a1 - a2