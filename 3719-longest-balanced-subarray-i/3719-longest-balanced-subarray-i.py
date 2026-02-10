from collections import defaultdict

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            odd = set()
            even = set()
            for j in range(i, n):
                if nums[j] & 1:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
                if len(even) == len(odd):
                    res = max(res, j - i + 1)
        return res