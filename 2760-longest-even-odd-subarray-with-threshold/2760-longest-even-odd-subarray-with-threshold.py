class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        def findLeftIndex(startingIndex: int) -> int: # O(N)
            leftIndex = startingIndex # 0
            while leftIndex < len(nums):
                if nums[leftIndex] % 2 == 0 and nums[leftIndex] <= threshold: # nums[1] = 2 is odd and 2 <= 5
                    break
                leftIndex += 1 # leftIndex = 1
            if leftIndex == len(nums):
                return -1
            return leftIndex
        
        leftIndex = findLeftIndex(0) # leftIndex = 1
        if leftIndex == -1:
            return 0
        
        result = 1
        rightIndex = leftIndex + 1 # rightIndex = 3 nums = [3, 2, 5, 4]
        while rightIndex < len(nums):
            if nums[rightIndex] % 2 != nums[rightIndex - 1] % 2 and nums[rightIndex] <= threshold: # 4 ^ 5 & 1 = 1
                result = max(result, rightIndex - leftIndex + 1) # result = 3 - 1 + 1 = 3
                rightIndex += 1 # rightIndex = 4
            else:
                leftIndex = findLeftIndex(rightIndex)
                if leftIndex == -1:
                    break
                rightIndex = leftIndex + 1
        return result

        # nums = [2, 3, 4, 5], threshold = 4
        # 