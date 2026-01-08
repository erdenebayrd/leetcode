class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.res = False
        n = len(maze) + 2
        m = len(maze[0]) + 2
        vis = [[[0] * 4 for _ in range(m)] for _ in range(n)]
        # 0: space
        # 1: visited
        # 2: wall
        for i in range(m):
            for k in range(4):
                vis[0][i][k] = 2 
                vis[n - 1][i][k] = 2
        for i in range(n):
            for k in range(4):
                vis[i][0][k] = 2 
                vis[i][m - 1][k] = 2
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 1:
                    for k in range(4):
                        vis[i + 1][j + 1][k] = 2
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(row: int, col: int, direction: int) -> bool:
            if vis[row][col][direction] != 0: # 0 means not visited yet, 1 visited, 2 hit the wall
                return vis[row][col][direction] == 2
            vis[row][col][direction] = 1
            if dfs(row + d[direction][0], col + d[direction][1], direction) is True:
                if row == destination[0] + 1 and col == destination[1] + 1:
                    self.res = True
                for k in range(4):
                    dfs(row + d[k][0], col + d[k][1], k)
        for k in range(4):
            dfs(start[0] + 1 + d[k][0], start[1] + 1 + d[k][1], k)
        return self.res