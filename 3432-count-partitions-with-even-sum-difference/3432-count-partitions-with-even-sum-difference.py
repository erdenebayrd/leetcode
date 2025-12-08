class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        suf = sum(nums)
        pre = 0
        res = 0
        for x in nums:
            suf -= x
            pre += x
            res += int((pre - suf) % 2 == 0 and suf > 0)
        return res