class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        res = len(word) + 1
        for ch in cnt:
            lo, hi = cnt[ch], cnt[ch] + k
            cur = 0
            for x in cnt:
                if cnt[x] < lo:
                    cur += cnt[x]
                if cnt[x] > hi:
                    cur += cnt[x] - hi
            res = min(res, cur)
        return res