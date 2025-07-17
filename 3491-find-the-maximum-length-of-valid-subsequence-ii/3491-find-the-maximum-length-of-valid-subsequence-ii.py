class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * k for _ in range(n)]
        for i in range(len(nums)):
            nums[i] %= k
            for j in range(i):
                dp[i][nums[j]] = max(dp[i][nums[j]], dp[j][nums[i]] + 1)
        return max([max(row) for row in dp])