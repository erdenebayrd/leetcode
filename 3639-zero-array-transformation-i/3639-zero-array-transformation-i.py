class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # time: O(N)
        # space: O(N)
        # method: linear loop
        n = len(nums)
        arr = [0] * (n + 1)
        for l, r in queries:
            arr[l] -= 1
            arr[r + 1] += 1
        for i in range(1, n + 1):
            arr[i] += arr[i - 1]

        for i in range(n):
            if nums[i] + arr[i] > 0:
                return False
        return True