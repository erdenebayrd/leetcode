class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # step 1 is checking the array is nondecreasing or not
        def isNonDecreasing(arr: List[int]) -> bool:
            if len(arr) <= 1:
                return True
            for i in range(1, len(arr)):
                if arr[i - 1] > arr[i]:
                    return False
            return True
        
        # step 2 is find a minimum sum index (the leftmost one)
        def findMinimumSumIndexLeftMost(arr: List[int]) -> int:
            # [5,2,4]
            #    | | = 6
            assert len(arr) > 1
            minSum = 50001
            leftMostIndex = -1
            for i in range(1, len(arr)):
                if arr[i - 1] + arr[i] < minSum:
                    minSum = arr[i - 1] + arr[i]
                    # 6
                    leftMostIndex = i - 1
                    # 1
            return leftMostIndex # 1
        
        # step 3 replacing minimum sum index (left most one) by it's sum value
        def replaceMinSumIndex(arr: List[int], leftMostIndex: int) -> List[int]:
            # arr = [5,2,4]
            # leftMostIndex = 1
            assert 0 <= leftMostIndex < len(arr) - 1
            arr[leftMostIndex] += arr[leftMostIndex + 1]
            # arr = [5,6,4]
            # leftMostIndex = 1
            for i in range(leftMostIndex + 1, len(arr) - 1): # 2, -> 2
                arr[i] = arr[i + 1]
            # arr = [5,6,4]
            return arr[:len(arr) - 1]
        
        operations = 0
        # arr = [5,2,4]
        while isNonDecreasing(nums) is False:
            leftMostIndex = findMinimumSumIndexLeftMost(nums)
            # 1
            nums = replaceMinSumIndex(nums, leftMostIndex)
            # [5,6]
            operations += 1
            # 2

        return operations

        # input: nums = [5,2,3,1]
        # Output: 2