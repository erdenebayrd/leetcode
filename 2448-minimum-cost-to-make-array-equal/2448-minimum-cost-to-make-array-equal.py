class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calculateCost(equal: int) -> int:
            totalCost = 0
            for i in range(len(nums)):
                difference = abs(nums[i] - equal)
                currentCost = difference * cost[i]
                totalCost += currentCost
            return totalCost

        lo, hi = 0, 10 ** 18
        while lo + 1 < hi:
            md = (lo + hi) // 2
            if calculateCost(md) <= calculateCost(md + 1):
                hi = md
            else:
                lo = md
        return calculateCost(hi)