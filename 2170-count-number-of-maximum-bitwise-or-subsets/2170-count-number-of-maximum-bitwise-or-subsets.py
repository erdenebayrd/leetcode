class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
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