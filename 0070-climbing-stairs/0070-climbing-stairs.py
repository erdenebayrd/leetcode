class Solution:
    def climbStairs(self, n: int) -> int:
        # time: O(N)
        # space: O(N)
        if n <= 1:
            return n
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for stair in range(2, n):
            dp[stair] = dp[stair - 1] + dp[stair - 2]
        return dp[n - 1]

        # 1, 2, 3, 5, 8, 13 .....  
        # [ 1   1 ]     dp[1].     dp[2]
        #           X         =.   
        # [ 1   0 ].    dp[0]      dp[1]

        # n - 1 element by power n - 2 times

        # [[1, 1], [1, 0]] ^ (n - 2) * [2, 1] = dp[n - 1], dp[n - 2]
        # time:  O(Log N)
        # space: O(1) 
        # using powLog