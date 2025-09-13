class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = ['a', 'e', 'i', 'o', 'u']
        cnt = Counter(s)
        vow = 0
        for ch in v:
            vow = max(vow, cnt[ch])
        cons = 0
        for ch in s:
            if ch in v:
                continue
            cons = max(cons, cnt[ch])
        return cons + vow