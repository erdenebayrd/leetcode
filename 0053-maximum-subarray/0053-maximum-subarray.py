class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: The subarray [4,-1,2,1] has the largest sum 6.

        nums =                [5,      4,       -1,       7,        8]
        prefix.                5.      9.        8        15        23
        Pointer                        ^                 
        minprefixvalue         -2.  -2.  -4. -4.  -4, -4  -4.  
        result                 -2.  1,   -2.  4.   3.  5.  6

        time: O(N) N is the size of nums
        space: O(1)
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        #               |
        #               V
        
        # nums  [-2,   -1]
        # prefix -2,   -3
        # minP.  -2    -3
        # result -2,      
        prefix = nums[0]
        minPrefixValue = prefix
        result = nums[0]
        for pointer in range(1, n):
            prefix += nums[pointer]
            result = max(result, max(prefix, prefix - minPrefixValue))
            minPrefixValue = min(minPrefixValue, prefix)
        return result