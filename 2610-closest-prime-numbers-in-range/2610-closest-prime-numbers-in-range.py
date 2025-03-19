class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve algorithm O(N)
        primes = [2]
        N = int(1e6) + 1
        visited = [False] * N
        for i in range(3, N, 2):
            if visited[i] is True:
                continue
            for j in range(i, N, i):
                visited[j] = True
            primes.append(i)
        
        begIdx, endIdx = -1, -1
        for idx, prime in enumerate(primes):
            if begIdx == -1 and prime >= left:
                begIdx = idx
            if prime <= right:
                endIdx = idx
        
        res = [-1, -1]
        if endIdx - begIdx < 1 or begIdx == -1:
            return res
        
        minDiff = int(1e6)
        for i in range(begIdx + 1, endIdx + 1):
            curDiff = primes[i] - primes[i - 1]
            if curDiff < minDiff:
                minDiff = curDiff
                res = [primes[i - 1], primes[i]]
        return res