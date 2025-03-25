class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            val = -1
            diff[l] += val
            diff[r + 1] -= val
        for i in range(1, n + 1):
            diff[i] += diff[i - 1]
        for i in range(n):
            if nums[i] + diff[i] > 0:
                return False
        return True