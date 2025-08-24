class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if sum(nums) == n:
            return n - 1
        for i in range(1, n):
            if nums[i] == 0:
                continue
            nums[i] += nums[i - 1]
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                continue
            nums[i] = max(nums[i], nums[i + 1])
        res = max(nums)
        for i in range(1, n - 1):
            if nums[i] == 0:
                res = max(res, nums[i - 1] + nums[i + 1])
        return res