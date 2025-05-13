class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = int(1e9) + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        while t > 0:
            t -= 1
            cur = [0] * 26
            for i in range(26):
                if i == 25:
                    cur[0] += cnt[25]
                    cur[1] += cnt[25]
                    cur[0] %= mod
                    cur[1] %= mod
                else:
                    cur[i + 1] += cnt[i]
                    cur[i + 1] %= mod
            cnt = cur
        return sum(cnt) % mod