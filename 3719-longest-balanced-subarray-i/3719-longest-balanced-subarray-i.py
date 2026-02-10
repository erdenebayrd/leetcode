from collections import defaultdict

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            balanced = 0
            counter = defaultdict(int)
            for j in range(i, n):
                counter[nums[j]] += 1
                if counter[nums[j]] == 1:
                    balanced += int(nums[j] % 2 == 1) - int(nums[j] % 2 == 0)
                if balanced == 0:
                    res = max(res, j - i + 1)
        return res