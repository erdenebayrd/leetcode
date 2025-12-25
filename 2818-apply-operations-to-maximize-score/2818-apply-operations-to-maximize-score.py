class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def sieve(N: int) -> List[int]:
            primes = [2]
            arr = [True] * (N + 1)
            for i in range(3, N + 1, 2):
                if arr[i] is False:
                    continue
                primes.append(i)
                for j in range(i * i, N + 1, i):
                    arr[j] = False
            return primes
        
        primes = sieve(int(1e5 ** 0.5) + 1)
        # print(len(primes))

        n = len(nums)
        # n = int(1e5)
        # nums = [i + 1 for i in range(n)]
        primeScores = [0] * n # count of distinct primes
        for i, x in enumerate(nums):
            for prime in primes:
                if x % prime == 0:
                    primeScores[i] += 1
                while x % prime == 0:
                    x //= prime
            primeScores[i] += int(x > 1)
        # print(max(primeScores))
        # m = 1
        # for i in range(max(primeScores) + 1):
        #     m *= primes[i]
        # print(m)

        xl, xr = [], []
        for i in range(n):
            xl.append(i)
            xr.append(i)
        
        maxPrimeScore = max(primeScores)
        positionPrimeScores = [deque() for i in range(maxPrimeScore + 1)]
        for i in range(n):
            positionPrimeScores[primeScores[i]].append(i)
        # print(primeScores)
        for i in range(n - 1, -1, -1):
            positionPrimeScores[primeScores[i]].pop() # pop right most index
            rightMostIdx = -1
            for j in range(primeScores[i], maxPrimeScore + 1, 1):
                if len(positionPrimeScores[j]) > 0:
                    rightMostIdx = max(rightMostIdx, positionPrimeScores[j][-1])
            xl[i] = rightMostIdx + 1
        # print(xl)
        for i in range(i):
            assert xl[i] <= i
        
        positionPrimeScores = [deque() for i in range(maxPrimeScore + 1)]
        for i in range(n):
            positionPrimeScores[primeScores[i]].append(i)
        for i in range(n):
            positionPrimeScores[primeScores[i]].popleft()
            leftMostIndex = n
            for j in range(primeScores[i] + 1, maxPrimeScore + 1, 1):
                if len(positionPrimeScores[j]) > 0:
                    leftMostIndex = min(leftMostIndex, positionPrimeScores[j][0])
            xr[i] = leftMostIndex - 1
        # print(xr)
        for i in range(i):
            assert i <= xr[i]
        
        mod = int(1e9 + 7)
        x = [0] * n
        for i in range(n):
            le = i - xl[i] + 1
            ri = xr[i] - i + 1
            # x[i] = (le * ri) % (mod - 1) # fermat's little theorem
            x[i] = le * ri
        # print(x)
        # print(max(x))

        def powerLog(a: int, x: int) -> int:
            res = 1
            while x > 0:
                if x & 1:
                    res = (res * a) % mod
                    x -= 1
                else:
                    x //= 2
                    a = (a * a) % mod
            return res

        arr = [(nums[i], x[i]) for i in range(n)]
        arr.sort(reverse=True)
        res = 1
        for i in range(n):
            num, xx = arr[i]
            power = min(xx, k)
            res = (res * powerLog(num, power)) % mod
            k -= power
            if k <= 0:
                break
        # print(set(primeScores))
        return res