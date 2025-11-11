class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        cnt = [[0, 0] for _ in range(k)]
        for i in range(k):
            cur = Counter(strs[i])
            cnt[i][0] = cur['0']
            cnt[i][1] = cur['1']

        @cache
        def solve(idx: int, curM: int, curN: int) -> int:
            if curM < 0 or curN < 0:
                return -int(1e8)
            if idx >= k:
                return 0
            res = solve(idx + 1, curM, curN)
            res = max(res, 1 + solve(idx + 1, curM - cnt[idx][0], curN - cnt[idx][1]))
            return res

        return solve(0, m, n)