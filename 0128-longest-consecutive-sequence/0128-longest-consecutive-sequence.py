class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        cur = 1
        prev = float('inf')
        result = 1
        for  i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i - 1] + 1 == nums[i]:
                    cur += 1
                else:
                    cur = 1
                result = max(result, cur)
        return result
