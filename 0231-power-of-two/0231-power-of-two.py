class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            if (1 << i) == n:
                return True
        return False