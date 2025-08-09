class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in range(31):
            if (1 << i) == n:
                return True
        return False