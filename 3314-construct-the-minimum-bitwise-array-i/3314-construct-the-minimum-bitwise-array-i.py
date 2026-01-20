class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            cur = -1
            for x in range(1, 1001):
                if (x | (x + 1)) == num:
                    cur = x
                    break
            res.append(cur)
        return res
        # | & ^