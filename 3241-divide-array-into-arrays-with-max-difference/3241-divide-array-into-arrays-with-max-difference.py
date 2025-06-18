class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # time: O(N * Log N)
        # space: O(1)
        # method: sorting + greedy
        nums.sort()
        # print(nums)
        for i in range(0, len(nums) - 2, 3):
            # print(nums[i], nums[i + 2], nums[i + 2] - nums[i], k)
            if nums[i + 2] - nums[i] > k:
                return []
        return [nums[i: i + 3] for i in range(0, len(nums) - 2, 3)]