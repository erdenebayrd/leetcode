class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        return max(nums) * n - sum(nums)