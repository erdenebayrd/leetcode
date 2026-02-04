from typing import Literal

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        def farthestIndexStrictly(startIndex: int, order: Literal["ascending", "descending"], step: Literal[1, -1]) -> int:
            stop = 0 if step == -1 else len(nums) - 1
            for i in range(startIndex, stop, step):
                if (order == "ascending" and nums[i] >= nums[i + step]) or (order == "descending" and nums[i] <= nums[i + step]):
                    return i
            return len(nums) - 1 if step == 1 else 0
        
        def maxSum(startIndex: int, endIndex: int) -> int:
            step = -1 if startIndex > endIndex else 1
            currentSum = nums[startIndex]
            result = currentSum
            for i in range(startIndex + step, endIndex + step, step):
                currentSum += nums[i]
                result = max(result, currentSum)
            return result

        res = float('-inf')
        middlePeakIndex = 1
        while middlePeakIndex < len(nums):
            middleBottomIndex = farthestIndexStrictly(startIndex=middlePeakIndex, order="descending", step=1)
            if middlePeakIndex == middleBottomIndex: # not found any decreasing subarray
                middlePeakIndex += 1
                continue
            leftIndex = farthestIndexStrictly(startIndex=middlePeakIndex, order="descending", step=-1)
            if leftIndex == middleBottomIndex: # not found any increasing subarray which end middlePeakIndex
                middlePeakIndex = middleBottomIndex
                continue
            rightIndex = farthestIndexStrictly(startIndex=middleBottomIndex, order="ascending", step=1)
            if rightIndex == middleBottomIndex: # not found any increasing subarray starting from middleBottomIndex
                middlePeakIndex = middleBottomIndex
                continue
            # found "trionic subarray"
            currentSum = sum(nums[middlePeakIndex:middleBottomIndex + 1])
            res = max(res, maxSum(middlePeakIndex - 1, leftIndex) + currentSum + maxSum(middleBottomIndex + 1, rightIndex))
            middlePeakIndex = middleBottomIndex
        
        return res