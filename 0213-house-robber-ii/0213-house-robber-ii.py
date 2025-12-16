class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def subrob(nums: List[int]) -> int:
            pre1 = [0, 0]
            pre2 = [0, 0]
            res = 0
            for x in nums:
                cur = [max(pre1), max(pre2) + x]
                pre2 = pre1
                pre1 = cur
                res = max(res, max(cur))
            return res
        return max(subrob(nums[1:]), subrob(nums[:-1]))