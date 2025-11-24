class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur = 0
        res = []
        for x in nums:
            cur = ((cur << 1) | x) % 5
            res.append(cur == 0)
        return res