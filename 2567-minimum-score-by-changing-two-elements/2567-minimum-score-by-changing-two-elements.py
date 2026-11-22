class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # time: O(N log N)
        # space: O(N) for timsort
        # method: sorting + greedy

        nums.sort()

        # case 1 - first 2 nums
        result = nums[-1] - nums[2]

        # case 2 - last 2 nums
        result = min(nums[-3] - nums[0], result)

        # case 3 - first and last number in nums
        result = min(result, nums[-2] - nums[1])
        return result