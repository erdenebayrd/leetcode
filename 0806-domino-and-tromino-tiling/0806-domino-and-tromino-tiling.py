class Solution:
    def numTilings(self, n: int) -> int:
        # time: O(N)
        # space O(N)
        # method: DP top-down
        mod = int(1e9) + 7
        @cache
        def solve(idx: int, bit: int) -> int:
            if idx >= n:
                if idx == n and bit == 0:
                    return 1
                return 0
            res = solve(idx + 2, 0) % mod
            if bit == 0:
                res = (res + solve(idx + 1, 0)) % mod
                res = (res + solve(idx + 1, 1)) % mod
                res = (res + solve(idx + 1, 2)) % mod
            elif bit == 1:
                res = (res + solve(idx + 1, 2)) % mod
            elif bit == 2:
                res = (res + solve(idx + 1, 1)) % mod
            return res

        return solve(0, 0)