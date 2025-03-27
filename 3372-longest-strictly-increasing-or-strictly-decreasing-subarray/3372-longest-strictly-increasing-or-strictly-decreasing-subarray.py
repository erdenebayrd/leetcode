class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        # increasing
        st, ed = 0, 0
        while ed < n:
            res = max(res, ed - st + 1)
            ed += 1
            if ed == n:
                break
            if nums[ed - 1] >= nums[ed]:
                st = ed
        # res = max(res, ed - st + 1)

        # decreasing
        st, ed = 0, 0
        while ed < n:
            res = max(res, ed - st + 1)
            ed += 1
            if ed == n:
                break
            if nums[ed - 1] <= nums[ed]:
                st = ed
        # res = max(res, ed - st + 1)

        return res