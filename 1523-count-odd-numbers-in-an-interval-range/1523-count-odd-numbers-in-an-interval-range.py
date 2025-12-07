class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        if low & 1:
            res += 1
            low += 1
        if high & 1:
            res += 1
            high -= 1
        # print(res, high, low)
        return (high - low) // 2 + res