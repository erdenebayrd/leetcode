class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        cur = nums[0]
        for x in nums:
            if x - cur <= k:
                continue
            res += 1
            cur = x
        return res