class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # time: O(N)
        # space: O(N)
        pos = {}
        pre = 0
        pos[0] = 0 # init
        res = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre not in pos:
                pos[pre] = i + 1
            if pre - k in pos:
                res = max(res, i - pos[pre - k] + 1)
        return res