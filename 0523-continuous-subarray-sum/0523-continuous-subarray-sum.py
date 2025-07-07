class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            if i > 0:
                nums[i] += nums[i - 1]
            nums[i] %= k
        seen = {0: True}
        for i in range(1, n):
            if nums[i] in seen:
                return True
            seen[nums[i - 1]] = True
        return False