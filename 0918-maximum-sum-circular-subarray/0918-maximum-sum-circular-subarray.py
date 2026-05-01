class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: Kadane + extension (min sub array by kadane)

        n = len(nums)
        maxSubArray, prefixForMax = float('-inf'), float('-inf')
        minSubArray, prefixForMin = float('inf'), float('inf')
        total = 0
        for i in range(n):
            prefixForMax = max(prefixForMax + nums[i], nums[i])
            maxSubArray = max(maxSubArray, prefixForMax)
            total += nums[i]
            prefixForMin = min(prefixForMin + nums[i], nums[i])
            minSubArray = min(minSubArray, prefixForMin)
        
        if maxSubArray < 0: # all numbers are negative
            return maxSubArray
        return max(maxSubArray, total - minSubArray)