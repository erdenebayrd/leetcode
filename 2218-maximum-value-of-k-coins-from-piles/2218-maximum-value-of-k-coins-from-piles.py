from functools import cache

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # time: O(sum(piles[i].length) * K) -> O(N ^ 2)
        # space: O(sum(piles[i].length) * K) -> O(N ^ 2)
        # method: DP
        
        n = len(piles)
        for i in range(n):
            for j in range(1, len(piles[i])):
                piles[i][j] += piles[i][j - 1]

        @cache
        def solve(index: int, currentK: int) -> float:
            if currentK == 0:
                return 0
            if currentK < 0 or index >= n:
                return float('-inf')
            
            result = solve(index + 1, currentK) # no pick from current piles (index)
            for i in range(min(currentK, len(piles[index]))):
                result = max(result, piles[index][i] + solve(index + 1, currentK - i - 1))
            return result

        return solve(0, k)