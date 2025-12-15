class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        cur = 1
        res = 1
        for i in range(1, len(prices)):
            if prices[i - 1] - 1 == prices[i]:
                cur += 1
            else:
                cur = 1
            res += cur
        return res