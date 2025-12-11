class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        cnt = Counter(t)
        m = len(cnt)
        le = 0
        res = [le, -1]

        def add(ch: str, m: int) -> int:
            if ch in cnt:
                cnt[ch] -= 1
                if cnt[ch] == 0:
                    m -= 1
            return m
        
        def remove(ch: str, m: int) -> int:
            if ch in cnt:
                cnt[ch] += 1
                if cnt[ch] == 1:
                    m += 1
            return m

        for ri in range(n):
            m = add(s[ri], m)
            while le <= ri and m == 0:
                m = remove(s[le], m)
                le += 1
                if m != 0:
                    le -= 1
                    m = add(s[le], m)
                    assert m == 0
                    break
            if m == 0:
                if res[-1] == -1 or res[1] - res[0] > ri - le:
                    res = [le, ri]
        if res[-1] == -1:
            return ""
        return s[res[0]: res[1] + 1]