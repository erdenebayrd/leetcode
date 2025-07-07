class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums[0] %= k
        seen = {0: True}
        for i in range(1, n):
            nums[i] = (nums[i - 1] + nums[i]) % k
            if nums[i] in seen:
                return True
            seen[nums[i - 1]] = True
        return False