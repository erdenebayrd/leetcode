class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # time: O(N)
        # space: O(1)
        # method: adhoc
        n = len(nums)
        def firstPeakIndex() -> int:
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    return i
            return -1
        
        index = firstPeakIndex()
        if index == -1:
            return True
        oldValue = nums[index]
        nums[index] = nums[index + 1]
        if firstPeakIndex() == -1:
            return True
        nums[index] = nums[index + 1] = oldValue
        return firstPeakIndex() == -1