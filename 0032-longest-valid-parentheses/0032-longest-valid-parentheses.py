class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # time: O(N)
        # space: O(N)
        # method: DP
    
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == '(':
                continue
            if s[i - 1] == '(':
                if i - 2 >= 0:
                    dp[i] = dp[i - 2]
                dp[i] += 2
            else: # s[i - 1] == ')' eg: .... ) )
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] += dp[i - dp[i - 1] - 2]
        return max(dp)