class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        le = 0
        cur = 0 # count of every bit
        for ri, num in enumerate(nums):
            while num & cur:
                cur ^= nums[le] # remove
                le += 1
            res = max(ri - le + 1, res)
            cur |= num # add
        
        return res