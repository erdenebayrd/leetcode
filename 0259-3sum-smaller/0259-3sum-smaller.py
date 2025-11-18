class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for le in range(n):
            md = le + 1
            ri = n - 1
            while md < ri:
                if nums[le] + nums[md] + nums[ri] < target:
                    res += ri - md # (le, md, ri), (le, md, ri - 1), (le, md, ri - 2), ... , (le, md, md + 1) # all these triplets could be okay
                    md += 1
                else:
                    ri -= 1
        return res