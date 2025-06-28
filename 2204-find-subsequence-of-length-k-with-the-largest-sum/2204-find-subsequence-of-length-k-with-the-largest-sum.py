class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [val for idx, val in sorted([(idx, val) for val, idx in sorted([(val, idx) for idx, val in enumerate(nums)], reverse=True)[:k]])]