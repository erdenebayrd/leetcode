class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = max(nums)
        seen = {}
        cur = 0
        for x in nums:
            if x >= 0 and x not in seen:
                seen[x] = True
                cur += x
        if len(seen) == 0:
            return res
        return max(res, cur)