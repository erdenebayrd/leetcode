class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for _ in range(n)]
        
        def dfs(curx, cury):
            vis[curx][cury] = True
            for i in range(4):
                x = curx + dx[i]
                y = cury + dy[i]
                if x >= 0 and x < n and y >= 0 and y < m and vis[x][y] is False and grid[x][y] == '1':
                    dfs(x, y)

        res = 0
        for i in range(n):
            for j in range(m):
                if vis[i][j] is False and grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res