class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # time: O(N * Log M) M <=> 1e9
        # space: O(1)
        n = len(nums)
        def check(md) -> bool:
            cnt = 0
            i = 0
            while i < n:
                if nums[i] <= md:
                    cnt += 1
                if i + 1 < n and nums[i] <= md and nums[i + 1] <= md:
                    i += 1
                i += 1
            return cnt >= k

        lo, hi = min(nums) - 1, max(nums) + 1
        while lo + 1 < hi:
            md = (lo + hi) // 2
            if check(md) is True:
                hi = md
            else:
                lo = md
        return hi