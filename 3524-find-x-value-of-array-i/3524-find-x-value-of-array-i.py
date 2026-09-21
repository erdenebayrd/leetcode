class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # time: O(N * K)
        # space: O(N * K)
        # method: DP
        n = len(nums)
        dp = [[0] * n for _ in range(k)]
        dp[nums[0] % k][0] = 1
        for i in range(1, n):
            for j in range(k):
                dp[(j * nums[i]) % k][i] += dp[j][i - 1]
            dp[nums[i] % k][i] += 1
        
        result = [0] * k
        for i in range(k):
            result[i] = sum(dp[i])
        return result