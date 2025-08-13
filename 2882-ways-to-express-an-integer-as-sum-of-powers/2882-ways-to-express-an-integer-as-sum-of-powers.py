class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        arr = []
        for i in range(1, n + 1):
            y = int(pow(i, x))
            if y <= n:
                arr.append(y)
        m = len(arr)
        mod = int(1e9 + 7)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # init dp
        for i in range(m + 1):
            dp[0][i] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i][j - 1] % mod
                if i - arr[j - 1] >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - arr[j - 1]][j - 1]) % mod
        return dp[n][m]