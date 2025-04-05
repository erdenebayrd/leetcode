class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # time: O(N * 2^N)
        # space: O(1)
        n = len(nums)
        res = 0
        for i in range(1 << n):
            cur = 0
            for j in range(n):
                if (i >> j) & 1:
                    cur ^= nums[j]
            res += cur
        return res