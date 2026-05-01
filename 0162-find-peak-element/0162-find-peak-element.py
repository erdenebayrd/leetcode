class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        since the problem condition says "nums[i] != nums[i + 1] for all valid i."
        meaning there must be at least one PEAK element existed
        since we can return ANY peak element's index, so that we can do binary search through the given array
        if consecutive 3 elements of an array (including outside of an array which is -inf) is strictly increasing, we need to go right side
        if consecutive 3 elements of an array (including outside of an array which is -inf) is strictly decreasing, we need to go left side
        if we found an peak element, we can just return it's index, so that time complexity would be O( log N ), space: O(1)
        """
        # time: O(log N)
        # space: O(1)
        # method: binary search
        def isIncreasing(index: int) -> bool:
            prev = float('-inf') if index - 1 < 0 else nums[index - 1]
            next = float('-inf') if index + 1 >= n else nums[index + 1]
            return prev < nums[index] < next
        
        def isPeak(index: int) -> bool:
            prev = float('-inf') if index - 1 < 0 else nums[index - 1]
            next = float('-inf') if index + 1 >= n else nums[index + 1]
            return prev < nums[index] > next

        n = len(nums)
        low, high = -1, n
        while low + 1 < high:
            mid = (low + high) // 2
            if isPeak(mid):
                return mid
            elif isIncreasing(mid):
                low = mid
            else:
                high = mid
        return -1