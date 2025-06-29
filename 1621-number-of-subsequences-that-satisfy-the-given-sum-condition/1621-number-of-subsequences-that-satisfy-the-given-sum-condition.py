class Solution:
    def __init__(self) -> None:
        self.__mod = 10 ** 9 + 7
    
    def power(self, base: int, n: int) -> int:
        assert n >= 0
        res = 1
        while n > 0:
            if n & 1:
                res = (res * base) % self.__mod
            n //= 2
            base = (base * base) % self.__mod
        return res


    def prefixSum(self, n: int) -> int:
        # return sum of power of 2 -> 2 ^ 0 + 2 ^ 1 + ... + 2 ^ n
        return (self.power(2, n + 1) - 1 + self.__mod) % self.__mod
    
    def rangeSum(self, l: int, r: int) -> int:
        if l == 0:
            return self.prefixSum(r)
        return (self.prefixSum(r) - self.prefixSum(l - 1) + self.__mod) % self.__mod

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            lo, hi = -1, i + 1
            while lo + 1 < hi:
                md = (lo + hi) // 2
                if nums[md] + nums[i] <= target:
                    lo = md
                else:
                    hi = md
            if lo == i:
                res = (res + 1) % self.__mod
                lo -= 1
            if lo == -1:
                continue
            res = (res + self.rangeSum(i - lo - 1, i - 1)) % self.__mod
            
        return res