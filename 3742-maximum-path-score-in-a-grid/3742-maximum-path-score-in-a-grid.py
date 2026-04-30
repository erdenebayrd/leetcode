from functools import cache

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # time: O(n * m * min(n + m, k)) -> O(N ^ 3)
        # space: O(n * m * min(n + m, k)) -> O(N ^ 3)
        # method: DP

        n = len(grid)
        m = len(grid[0])
        k = min(k, n + m)

        @cache
        def solve(row: int, col: int, cost: int) -> float:
            if row >= n or col >= m:
                return float('-inf')
            cost += int(grid[row][col] > 0)
            if cost > k:
                return float('-inf')
            benefit = grid[row][col]
            if row == n - 1 and col == m - 1:
                return benefit
            benefit += max(solve(row + 1, col, cost), solve(row, col + 1, cost))
            return benefit
        
        result = solve(0, 0, 0)
        solve.cache_clear()
        if result == float('-inf'):
            result = -1
        return result