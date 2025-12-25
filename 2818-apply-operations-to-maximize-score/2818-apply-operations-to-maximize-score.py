# Gemini pro
from collections import deque
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        
        # --- 1. Sieve of Eratosthenes ---
        # Only need primes up to sqrt(10^5) approx 316
        upper_bound = int(100000**0.5) + 5
        primes = []
        is_prime = [True] * (upper_bound + 1)
        for i in range(2, upper_bound + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, upper_bound + 1, i):
                    is_prime[j] = False
        
        # --- 2. Calculate Prime Scores ---
        n = len(nums)
        primeScores = [0] * n
        for i, val in enumerate(nums):
            temp = val
            count = 0
            for p in primes:
                if p * p > temp:
                    break
                if temp % p == 0:
                    count += 1
                    while temp % p == 0:
                        temp //= p
            if temp > 1:
                count += 1
            primeScores[i] = count

        # --- 3. Find Previous Greater/Equal and Next Greater Element ---
        # Note: Your bucket/deque approach is O(N) because max score is small (~6).
        # This effectively replaces the Monotonic Stack.
        
        # Left boundary (Previous Greater or Equal Element)
        xl = [0] * n
        maxPrimeScore = max(primeScores) if primeScores else 0
        
        # Store indices by score
        positionPrimeScores = [deque() for _ in range(maxPrimeScore + 1)]
        
        # Fill strictly left-to-right to prep for 'pop' logic (simulating backward scan)
        # Actually, simpler to just iterate and maintain state.
        # Let's stick to your logic but clean:
        for i in range(n):
            positionPrimeScores[primeScores[i]].append(i)
            
        for i in range(n - 1, -1, -1):
            positionPrimeScores[primeScores[i]].pop() # Remove self
            
            # We need index of Nearest Element to the LEFT with score >= current
            # Since we populated queues with 0..n-1, and popped current, 
            # the queues now contain only indices < i (if we popped correctly in a forward pass?)
            # Wait, your original logic populated ALL, then popped from right.
            # That leaves indices < i in the deque. The largest among them is the neighbor.
            
            rightMostIdx = -1
            for score in range(primeScores[i], maxPrimeScore + 1):
                if positionPrimeScores[score]:
                    rightMostIdx = max(rightMostIdx, positionPrimeScores[score][-1])
            xl[i] = rightMostIdx + 1

        # Right boundary (Next Strictly Greater Element)
        xr = [0] * n
        positionPrimeScores = [deque() for _ in range(maxPrimeScore + 1)]
        for i in range(n):
            positionPrimeScores[primeScores[i]].append(i)
            
        for i in range(n):
            positionPrimeScores[primeScores[i]].popleft() # Remove self
            
            # We need index of Nearest Element to the RIGHT with score > current
            # Queues contain indices > i. We want the smallest index.
            leftMostIndex = n
            for score in range(primeScores[i] + 1, maxPrimeScore + 1):
                if positionPrimeScores[score]:
                    leftMostIndex = min(leftMostIndex, positionPrimeScores[score][0])
            xr[i] = leftMostIndex - 1

        # --- 4. Calculate Contribution and Greedy Selection ---
        # Create pairs of (num_value, available_operations)
        pairs = []
        for i in range(n):
            # Total subarrays where nums[i] is the pivot
            # No modulo here!
            count = (i - xl[i] + 1) * (xr[i] - i + 1)
            pairs.append((nums[i], count))
        
        # Sort by number value descending to maximize score
        pairs.sort(key=lambda x: x[0], reverse=True)
        
        res = 1
        for num, limit in pairs:
            if k <= 0:
                break
            
            take = min(k, limit)
            # Power calculation with modulo
            res = (res * pow(num, take, mod)) % mod
            k -= take
            
        return res