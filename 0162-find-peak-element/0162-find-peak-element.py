class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        lo, hi = -1, n
        nums.append(int(-1e18))
        while lo + 1 < hi:
            md = (lo + hi) // 2
            if nums[md] > nums[md + 1]:
                hi = md
            else:
                lo = md
        return hi