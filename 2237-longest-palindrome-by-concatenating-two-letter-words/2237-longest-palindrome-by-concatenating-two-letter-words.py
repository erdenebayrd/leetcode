class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        cnt = Counter(words)
        flag = False
        # print(cnt)
        for s in cnt:
            if s[0] == s[1]:
                res += 4 * (cnt[s] // 2)
                if cnt[s] & 1 and flag is False:
                    flag = True
                    res += 2
            else:    
                res += 2 * min(cnt[s[::-1]], cnt[s])
        return res
