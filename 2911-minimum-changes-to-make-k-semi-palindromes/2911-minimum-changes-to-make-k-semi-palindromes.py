from functools import cache

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        # time: O(n^2 * k * sqrt(n))
        # space: O(n * k)
        # method: DP
        n = len(s)
        divisors = {}
        for size in range(2, n + 1):
            divisors[size] = [1]
            for divisor in range(2, size):
                if size % divisor == 0:
                    divisors[size].append(divisor)
        @cache
        def cost(left: int, right: int, divisor: int) -> int: # O(n)
            result = 0
            size = right - left + 1
            for start in range(divisor):
                current_left = left + start
                current_right = current_left + size - divisor
                while current_left < current_right:
                    result += int(s[current_left] != s[current_right])
                    current_left += divisor
                    current_right -= divisor
            return result
            
        inf = float('inf')

        @cache
        def solve(left: int, k: int) -> float:
            if left == n and k == 0:
                return 0
            if left >= n or k <= 0:
                return inf

            result = inf
            for right in range(left + 1, n):
                for divisor in divisors[right - left + 1]:
                    result = min(result, cost(left, right, divisor) + solve(right + 1, k - 1))
            return result
        
        # print(cost(0, n - 1, 1))
        # print(cost(0, n - 1, 2))
        # print(cost(0, n - 1, 5)) 

        return solve(0, k)