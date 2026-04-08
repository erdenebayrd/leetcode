class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # time: O(N * Q)
        # space: O(1)
        # method: brute force, simulation

        mod = int(1e9) + 7
        for left, right, step, value in queries:
            while left <= right:
                nums[left] = (nums[left] * value) % mod
                left += step
        result = 0
        for number in nums:
            result ^= number
        return result