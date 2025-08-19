class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur += 1
            else:
                res += (cur + 1) * cur // 2
                cur = 0
        res += (cur + 1) * cur // 2
        return res