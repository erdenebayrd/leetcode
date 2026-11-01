class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # time: O(N)
        # space: O(1)
        # method: greedy
        return sum(nums) - min(nums) * len(nums)