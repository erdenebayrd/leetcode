class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        """        
                          V
             colors = [1, 1, 2, 2]
        Input: nums = [1, 4, 3, 5]
        take it        1  4. 7. 9
        Not take it.   0. 1. 4. 7
        Output: 9
        # time: O(N)
        # space: O(1) keeping only prev window
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        take = nums[0]
        notTake = 0
        result = max(take, notTake)
        for index in range(1, n):
            if colors[index] == colors[index - 1]: # color is same with prev adjacent
                currentTake = nums[index] + notTake
            else:
                currentTake = nums[index] + max(notTake, take)
            currentNotTake = max(take, notTake)
            take = currentTake
            notTake = currentNotTake
            result = max(result, max(take, notTake))
        return result