from bisect import bisect_left

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        res = bisect_left(nums, 0) # negative
        res = max(res, n - bisect_left(nums, 1)) # positive
        return res
