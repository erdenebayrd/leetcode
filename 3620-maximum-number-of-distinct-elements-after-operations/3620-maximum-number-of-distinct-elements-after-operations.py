class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = 1
        cur = nums[0] - k
        for i in range(1, n):
            if cur >= nums[i] + k:
                continue
            cur = max(cur + 1, nums[i] - k)
            res += 1
        return res