class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        le = 0
        n = len(s)
        res = 0
        cnt = defaultdict(int)
        for ri in range(n):
            cnt[s[ri]] += 1
            while le < n and cnt[s[ri]] > 1:
                cnt[s[le]] -= 1
                le += 1
            res = max(res, ri - le + 1)
        return res