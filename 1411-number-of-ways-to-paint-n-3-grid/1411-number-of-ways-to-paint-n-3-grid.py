class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 1_000_000_007
        arr = ["121", "123", "131", "132", "212", "213", "231", "232", "312", "313", "321", "323"]
        @cache
        def solve(pre: str, idx: int) -> int:
            if idx >= n:
                return 1
            res = 0
            for pattern in arr:
                if all(pattern[i] != pre[i] for i in range(3)):
                    res = (res + solve(pattern, idx + 1)) % mod
            return res
        return solve("444", 0)