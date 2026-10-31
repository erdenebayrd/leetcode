from functools import cache

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: DP
        mod = int(1e9 + 7)

        @cache
        def solve(row: int, col: int, direction: int) -> int:
            if row < 0 or col < 0:
                return 0
            
            if row == 0 and col == 0:
                return 1
            
            if grid[row][col] == 1:
                if direction == 0:
                    return solve(row, col - 1, direction ^ 1)
                if direction == 1:
                    return solve(row - 1, col, direction ^ 1)

            total = solve(row - 1, col, 0) + solve(row, col - 1, 1)

            return total % mod
        
        rows = len(grid)
        cols = len(grid[0])

        return solve(rows - 1, cols - 1, -1)