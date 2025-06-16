class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = nums[0]
        n = len(nums)
        res = -1
        for i in range(1, n):
            if nums[i] - mn > 0:
                res = max(res, nums[i] - mn)
            mn = min(mn, nums[i])
        return res