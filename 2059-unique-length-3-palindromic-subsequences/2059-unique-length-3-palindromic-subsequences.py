class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pre, suf = [0] * 26, [0] * 26
        for ch in s:
            suf[ord(ch) - ord('a')] += 1
        
        seen = set()
        for ch in s:
            x = ord(ch) - ord('a')
            suf[x] -= 1
            for i in range(26):
                if pre[i] > 0 and suf[i] > 0:
                    le = chr(ord('a') + i)
                    pal = str(le + ch + le)
                    if pal not in seen:
                        seen.add(pal)
            pre[x] += 1
        return len(seen)