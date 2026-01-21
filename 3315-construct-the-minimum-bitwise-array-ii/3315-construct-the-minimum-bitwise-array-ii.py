class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        for idx, num in enumerate(nums):
            for i in range(31, -1, -1):
                if (num >> i) & 1:
                    cur = num ^ (1 << i)
                    if cur | (cur + 1) == num:
                        res[idx] = cur
                        break
        return res