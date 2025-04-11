class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # brute force
        def check(x: int, n: int) -> bool:
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
            n = int(log(x, 10)) + 1
            if n & 1:
                continue
            if check(x, n) is True:
                res += 1
        return res