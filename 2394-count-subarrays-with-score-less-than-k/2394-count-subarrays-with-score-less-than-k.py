class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # time: O(N * LogN)
        # space: O(1)
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        res = 0
        for i in range(n):
            lo, hi = i - 1, n
            while lo + 1 < hi:
                md = (lo + hi) // 2
                x = nums[md]
                if i > 0:
                    x -= nums[i - 1]
                if x * (md - i + 1) < k:
                    lo = md
                else:
                    hi = md
            # print(i, ":", lo)
            res += lo - i + 1
        return res