class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: array
        n = len(nums)
        total = sum(nums)
        prefix, suffix = 0, total
        for i in range(n):
            suffix -= nums[i]
            if prefix == suffix:
                return i
            prefix += nums[i]
        return -1