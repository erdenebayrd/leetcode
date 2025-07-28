class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # time: O(N * 2 ^ N)
        # space: O(1)
        # method: brute force
        s = 0
        for x in nums:
            s |= x
        n = len(nums)
        res = 0
        for i in range(1, 1 << n):
            cur = 0
            for j in range(n):
                if (i >> j) & 1:
                    cur |= nums[j]
            if cur == s:
                res += 1
        return res