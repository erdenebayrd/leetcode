class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        preMax = max(nums[:2])
        diffMax = nums[0] - nums[1]
        res = 0
        for i in range(2, n):
            res = max(res, diffMax * nums[i])
            # print(diffMax, nums[i], diffMax * nums[i])
            diffMax = max(diffMax, preMax - nums[i])
            preMax = max(preMax, nums[i])
        return res