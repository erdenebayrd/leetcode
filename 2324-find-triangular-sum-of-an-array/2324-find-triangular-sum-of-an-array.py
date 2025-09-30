class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for j in range(1, len(nums)):
            for i in range(len(nums) - j):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0]