class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = 1000
        dp = [[1] * n for _ in range(n)]
        for i in range(len(nums)):
            nums[i] %= k
        for i in range(len(nums)):
            for j in range(i):
                dp[i][nums[j]] = max(dp[i][nums[j]], dp[j][nums[i]] + 1)
        return max([max(row) for row in dp])