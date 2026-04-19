class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # time: O(rows * cols)
        # space: O(1)
        # method: DP
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                left = grid[i][j - 1] if j - 1 >= 0 else float('inf')
                upper = grid[i - 1][j] if i - 1 >= 0 else float('inf')
                if i == 0 and j == 0:
                    continue
                grid[i][j] += min(left, upper)
        return grid[rows - 1][cols - 1]