class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            pre = int(-1e18)
            nex = int(-1e18)
            if i + 1 < n:
                nex = nums[i + 1]
            if i - 1 >= 0:
                pre = nums[i - 1]
            if pre < nums[i] and nums[i] > nex:
                return i
        return -1