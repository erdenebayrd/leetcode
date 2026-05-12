from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # time: O(n ^ 3)
        # space: O(n ^ 2)
        # method: memo dp

        n = len(piles)
        prefix = [0] * n
        prefix[0] = piles[0]
        for i in range(1, n):
            prefix[i] += prefix[i - 1] + piles[i]
        
        def get_range_sum(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == 0:
                return prefix[right]
            return prefix[right] - prefix[left - 1]

        @cache
        def solve(index: int, current_m: int) -> int:
            if index >= n:
                return 0
            
            cumulative_sum = 0
            result = 0
            for i in range(index, min(n, index + 2 * current_m)):
                cumulative_sum += piles[i]
                result = max(result, cumulative_sum + get_range_sum(i + 1, n - 1) - solve(i + 1, max(current_m, i - index + 1)))
            return result
        
        return solve(0, 1)