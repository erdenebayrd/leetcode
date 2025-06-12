class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            res = max(res, abs(nums[(i + 1) % n] - nums[i]))
        return res