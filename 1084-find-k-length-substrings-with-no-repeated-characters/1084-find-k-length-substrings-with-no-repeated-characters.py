class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return 0
        cnt = defaultdict(int)
        cur = 0
        for i in range(k):
            cnt[s[i]] += 1
            if cnt[s[i]] == 1:
                cur += 1
        res = 0
        if cur == k:
            res += 1
        for i in range(k, n):
            cnt[s[i - k]] -= 1
            if cnt[s[i - k]] == 0:
                cur -= 1
            cnt[s[i]] += 1
            if cnt[s[i]] == 1:
                cur += 1
            if cur == k:
                res += 1
        return res