class Solution:
    def minJumps(self, nums: List[int]) -> int:
        # time: O(M + N * log M) M is max number in nums
        # space: O(N + N * log M)
        # method: sieve + bfs

        def sieve(limit: int):
            isPrime = [True] * (limit + 1)
            isPrime[0] = isPrime[1] = False
            primes = defaultdict(list)
            for number in range(limit + 1):
                if isPrime[number] is False:
                    continue
                for factor in range(number, limit + 1, number):
                    primes[number].append(factor)
                    isPrime[factor] = False
            return primes
        
        primes = sieve(max(nums))
        seen = set()
        n = len(nums)
        queue = deque()
        dist = [float('inf')] * n
        dist[0] = 0
        queue.append(0)
        positions = defaultdict(list)
        for i in range(n):
            positions[nums[i]].append(i)

        visited = set()
        visited.add(0)

        while queue:
            index = queue.popleft()
            value = nums[index]
            if value in primes and value not in seen: # prime number
                for factor in primes[value]:
                    if factor not in seen and factor in positions:
                        for idx in positions[factor]:
                            if idx not in visited:
                                queue.append(idx)
                                visited.add(idx)
                                dist[idx] = min(dist[idx], dist[index] + 1)
                        seen.add(factor)
            if index + 1 < n and dist[index + 1] > dist[index] + 1 and index + 1 not in visited:
                dist[index + 1] = dist[index] + 1
                queue.append(index + 1)
                visited.add(index + 1)
            if index - 1 >= 0 and dist[index - 1] > dist[index] + 1 and index - 1 not in visited:
                dist[index - 1] = dist[index] + 1
                queue.append(index - 1)
                visited.add(index - 1)

        return dist[n - 1]