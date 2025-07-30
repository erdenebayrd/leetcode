class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        n = len(nums)
        res = 1
        cur = 0
        for i in range(n):
            if nums[i] == k:
                cur += 1
            else:
                cur = 0
            res = max(res, cur)
        return res