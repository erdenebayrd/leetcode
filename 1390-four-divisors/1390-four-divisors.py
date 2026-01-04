class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            divisors = []
            for i in range(2, int(x ** 0.5)):
                if x % i == 0:
                    divisors.append(x // i)
                    divisors.append(i)
                if len(divisors) > 2:
                    break
            if len(divisors) == 2:
                res += sum(divisors) + 1 + x
        return res