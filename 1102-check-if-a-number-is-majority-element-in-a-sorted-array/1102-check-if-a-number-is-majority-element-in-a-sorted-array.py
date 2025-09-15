class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        cnt = 0
        for x in nums:
            if x == target:
                cnt += 1
        return len(nums) / 2 < cnt