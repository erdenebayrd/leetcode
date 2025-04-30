class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            y = int(log(x, 10) + 1e-6) + 1
            if y & 1:
                continue
            res += 1
        return res