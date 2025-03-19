class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        n = len(nums)
        res = 0
        for i in range(n - 2):
            if nums[i] == 0:
                for j in range(i, i + 3):
                    nums[j] ^= 1
                res += 1
        if sum(nums) != n:
            res = -1
        return res