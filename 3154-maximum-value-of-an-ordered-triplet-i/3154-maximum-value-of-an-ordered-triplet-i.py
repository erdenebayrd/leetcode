class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        n = len(nums)
        res = 0
        dMax = nums[0] - nums[1]
        pMax = max(nums[0], nums[1])
        for i in range(2, n):
            res = max(res, dMax * nums[i])
            dMax = max(dMax, pMax - nums[i])
            pMax = max(nums[i], pMax)
        return res