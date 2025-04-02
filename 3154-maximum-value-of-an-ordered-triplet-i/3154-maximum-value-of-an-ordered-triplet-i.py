class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(N)
        n = len(nums)
        preMax = [0] * n
        sufMax = [0] * n
        preMax[0] = nums[0]
        sufMax[n - 1] = nums[n - 1]
        for i in range(1, n):
            preMax[i] = max(preMax[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            sufMax[i] = max(sufMax[i + 1], nums[i])
        res = 0
        for i in range(1, n - 1):
            res = max(res, (preMax[i - 1] - nums[i]) * sufMax[i + 1])
        return res