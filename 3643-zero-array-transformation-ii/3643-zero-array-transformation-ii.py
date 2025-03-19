class Solution:
    def check(self, nums: List[int], queries: List[List[int]]) -> bool:
        # O(N)
        n = len(nums)
        arr = [0] * (n + 1)
        for l, r, val in queries:
            arr[l] += val
            arr[r + 1] -= val
        for i in range(1, n):
            arr[i] += arr[i - 1]
        for i in range(n):
            if nums[i] - arr[i] > 0:
                return False
        return True


    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(queries)
        lo, hi = -1, n + 1
        while lo + 1 < hi:
            md = (lo + hi) // 2
            if self.check(nums, queries[:md]) is True:
                hi = md
            else:
                lo = md
        if hi == n + 1:
            hi = -1
        return hi