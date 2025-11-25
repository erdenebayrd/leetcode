class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for i in range(k):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return i + 1
        return -1