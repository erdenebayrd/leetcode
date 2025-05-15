class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n = len(grid)
        m = len(grid[0])

        @cache
        def calc(row, col, d) -> int:
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == "W":
                return 0
            res = calc(row + d[0], col + d[1], d)
            if grid[row][col] == "E":
                res += 1
            return res
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    cur = 0
                    for d in dirs:
                        cur += calc(i + d[0], j + d[1], d)
                    res = max(res, cur)
        return res