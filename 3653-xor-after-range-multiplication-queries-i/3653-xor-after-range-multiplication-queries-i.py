class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # time: O(N * Q)
        # space: O(1)
        # method: brute force, simulation

        mod = int(1e9) + 7
        for left, right, step, value in queries:
            for index in range(left, right + 1, step):
                nums[index] = (nums[index] * value) % mod
        result = 0
        for number in nums:
            result ^= number
        return result