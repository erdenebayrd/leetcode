class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        le = 0
        curSumBits = 0 # count of every bit
        for ri, num in enumerate(nums):
            while num & curSumBits:
                curSumBits ^= nums[le] # remove
                le += 1
            res = max(ri - le + 1, res)
            curSumBits |= num # add
        
        return res