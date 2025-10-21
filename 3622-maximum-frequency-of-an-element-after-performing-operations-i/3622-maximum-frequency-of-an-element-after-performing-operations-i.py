class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        cnt = Counter(nums)
        res = 0
        for x in range(nums[0], nums[-1] + 1):
            low, high = x - k, x + k
            lo = bisect.bisect_left(nums, low)
            hi = bisect.bisect_right(nums, high) - 1
            if lo > hi:
                continue
            res = max(res, cnt[x] + min(hi - lo + 1 - cnt[x], numOperations))
        return res