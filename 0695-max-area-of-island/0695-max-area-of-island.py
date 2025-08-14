class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        currentCompNum = 2
        d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        n = len(grid)
        m = len(grid[0])

        def dfs(i: int, j: int, cur) -> None:
            grid[i][j] = cur
            for k in range(len(d)):
                x = i + d[k][0]
                y = j + d[k][1]
                if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] != 1:
                    continue
                dfs(x, y, cur)

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                dfs(i, j, currentCompNum)
                currentCompNum += 1
        cnt = Counter([])
        for row in grid:
            cnt += Counter(row)
        res = 0
        for key in cnt:
            if key == 0:
                continue
            res = max(cnt[key], res)
        return res