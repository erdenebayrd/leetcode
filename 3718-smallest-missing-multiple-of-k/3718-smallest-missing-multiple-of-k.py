class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        mx = max(nums) + k + 1
        for i in range(k, mx, k):
            if i not in nums:
                return i
        return 0