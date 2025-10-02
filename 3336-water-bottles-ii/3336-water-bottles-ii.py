class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            numBottles += 1
            numExchange += 1
            res += 1
        return res