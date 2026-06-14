class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: using input array as dictionary
        n = len(nums)
        for i in range(n):
            value = abs(nums[i])
            index = value - 1
            if nums[index] < 0:
                return value
            nums[index] = -nums[index]
        return -1
        """
            index.    0, 1,  2,   3, 4
            nums = [ -1, -3, -4, -2, 2 ]
        """