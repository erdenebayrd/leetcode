class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        # print(nums)
        n = len(nums)
        lo, hi = -1, max(nums) - min(nums) + 1
        while lo + 1 < hi:
            md = (lo + hi) // 2
            cur = 0
            i = 1
            while i < n:
                if nums[i] - nums[i - 1] <= md:
                    i += 2
                    cur += 1
                else:
                    i += 1
            if cur >= p:
                hi = md
            else:
                lo = md
        return hi