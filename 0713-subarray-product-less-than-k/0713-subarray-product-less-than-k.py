class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(1)
        # method: sliding window
        n = len(nums)
        curProduct = 1
        l = 0
        res = 0
        for r in range(n):
            curProduct *= nums[r]
            while l <= r and curProduct >= k:
                curProduct //= nums[l]
                l += 1
            res += (r - l + 1)
        return res