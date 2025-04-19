class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList(nums)
        res = 0
        for x in nums:
            sl.remove(x)
            lo = lower - x
            hi = upper - x
            res += sl.bisect_right(hi) - sl.bisect_left(lo)
        return res