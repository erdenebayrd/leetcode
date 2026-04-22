class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: adhoc
        maxNumber = max(nums)
        minNumber = min(nums)
        result = maxNumber - minNumber
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == maxNumber:
                count += 1
                nums[i] = minNumber
        if count > 1:
            result += maxNumber
        else:
            result += max(nums)
        return result