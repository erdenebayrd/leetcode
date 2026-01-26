class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if 1 <= nums[i] <= n:
                continue
            nums[i] = n + 1
        # [1 -> n, n + 1]
        for i in range(n):
            index = nums[i] if nums[i] > 0 else -nums[i]
            if index == n + 1:
                continue
            # index would be in this range [1, n]
            index -= 1
            if nums[index] > 0:
                nums[index] = -nums[index] # using a "-" (minus) sign instead of auxilary boolean array
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1