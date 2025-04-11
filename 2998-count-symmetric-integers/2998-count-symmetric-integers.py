class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def check(x: int) -> bool:
            n = int(log(x, 10)) + 1
            s = 0
            for i in range(n // 2):
                s += (x % 10)
                x //= 10
            for i in range(n // 2):
                s -= (x % 10)
                x //= 10
            return s == 0

        res = 0
        for x in range(low, high + 1):
            if (int(log(x, 10)) + 1) & 1:
                continue
            if check(x) is True:
                res += 1
        return res