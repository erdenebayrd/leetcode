class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * k for _ in range(n)]
        res = 0
        for i in range(len(nums)):
            nums[i] %= k
            for j in range(i):
                dp[i][nums[j]] = max(dp[i][nums[j]], dp[j][nums[i]] + 1)
                res = max(res, dp[i][nums[j]])
        return res
        