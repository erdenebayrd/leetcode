class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        minimum = min(nums[1:])
        nums[nums[1:].index(minimum) + 1] = max(nums)
        return nums[0] + minimum + min(nums[1:])