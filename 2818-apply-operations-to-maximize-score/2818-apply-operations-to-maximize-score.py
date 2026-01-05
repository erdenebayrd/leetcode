# My solution
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        primeScores = [0] * n
        cnt = [0] * n # how many times i'th element could be chosen by highest prime score
        mod = 1_000_000_007
        m = max(nums) + 1
        primes = [2]
        def sieve():
            isPrime = [True] * m
            isPrime[0] = isPrime[1] = False
            for i in range(3, m, 2):
                if isPrime[i] is False:
                    continue
                primes.append(i)
                for j in range(i * i, m, i):
                    isPrime[j] = False
        sieve()
        
        for i in range(n):
            x = nums[i]
            for prime in primes:
                if prime * prime > x:
                    break
                if x % prime != 0:
                    continue
                primeScores[i] += 1
                while x % prime == 0:
                    x /= prime
            primeScores[i] += int(x > 1)
        # print(primeScores)
        # left to right for leftMostIndex
        decreasingMonotonicStack = deque()
        leftMostIndex = [-1] * n
        for i in range(n):
            while decreasingMonotonicStack and primeScores[decreasingMonotonicStack[-1]] < primeScores[i]:
                decreasingMonotonicStack.pop()
            if decreasingMonotonicStack:
                leftMostIndex[i] = decreasingMonotonicStack[-1]
            decreasingMonotonicStack.append(i)
        
        # right to left for rightMostIndex
        decreasingMonotonicStack = deque()
        rightMostIndex = [n] * n
        for i in range(n - 1, -1, -1):
            while decreasingMonotonicStack and primeScores[decreasingMonotonicStack[-1]] <= primeScores[i]:
                decreasingMonotonicStack.pop()
            if decreasingMonotonicStack:
                rightMostIndex[i] = decreasingMonotonicStack[-1]
            decreasingMonotonicStack.append(i)
        
        for i in range(n):
            cnt[i] = (i - leftMostIndex[i]) * (rightMostIndex[i] - i)
        del rightMostIndex
        del leftMostIndex
        del decreasingMonotonicStack
        del primes
        del m
        del primeScores
        arr = []
        for i in range(n):
            arr.append((nums[i], cnt[i]))
        arr.sort(reverse=True)
        # print(arr)

        def powLog(x: int, y: int) -> int:
            cur = 1
            while y > 0:
                if y & 1:
                    cur = (cur * x) % mod
                    y -= 1
                else:
                    x = (x * x) % mod
                    y //= 2
            return cur
        
        res = 1
        for i in range(n):
            if k == 0:
                break
            y = min(k, arr[i][1])
            x = arr[i][0]
            res = (res * powLog(x, y)) % mod
            k -= y
        return res