class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        cnt = Counter(nums)

        def calc(x: int) -> int:
            lo = bisect.bisect_left(nums, x - k)
            hi = bisect.bisect_right(nums, x + k) - 1
            if lo > hi:
                return 0
            return cnt[x] + min(hi - lo + 1 - cnt[x], numOperations)

        res = 0
        for x in nums:
            for i in range(-1, 2):
                res = max(res, calc(x + k * i))
        return res
