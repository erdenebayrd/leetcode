class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        res, cur = 1, 0
        for i in range(len(nums)):
            if nums[i] == k:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0
        return res