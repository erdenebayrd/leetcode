class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def nonZero(x: int) -> bool:
            if x == 0:
                return False
            while x > 0:
                if x % 10 == 0:
                    return False
                x //= 10
            return True
        for x in range(1, n):
            if nonZero(x) is True and nonZero(n - x) is True:
                return [x, n - x]
        assert False