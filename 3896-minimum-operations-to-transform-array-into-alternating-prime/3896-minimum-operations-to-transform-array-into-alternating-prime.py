import bisect
from collections import defaultdict

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        # time: O(N log N) N is the maximum prime number
        # space: O(N)
        # method sieve
        
        def sieve(N: int) -> int: # O(N)
            isPrime = [True] * (N + 1)
            isPrime[0] = isPrime[1] = False
            primes = [2]
            for i in range(3, N + 1, 2):
                if isPrime[i] is False:
                    continue
                primes.append(i)
                for j in range(i * i, N + 1, i):
                    isPrime[j] = False
            return primes
        
        primes = sieve(max(nums) * 2)
        isPrime = set(primes)
        
        def nextPrime(number: int) -> int:
            while number not in isPrime:
                number += 1
            return number
        
        result = 0
        n = len(nums)
        for i in range(n):
            if i & 1: # odd index (non-prime)
                if nums[i] in isPrime:
                    result += 1
                    if nums[i] == 2:
                        result += 1
            else: # even index (prime)
                if nums[i] not in isPrime:
                    prime = nextPrime(nums[i])
                    result += prime - nums[i]
        return result