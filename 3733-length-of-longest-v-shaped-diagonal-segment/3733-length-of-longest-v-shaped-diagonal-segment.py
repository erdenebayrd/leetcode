class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        arr = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]
        d = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

        @cache
        def calc(x: int, y: int, dirIdx: int) -> int:
            xx, yy = x + d[dirIdx][0], y + d[dirIdx][1]
            if xx < 0 or yy < 0 or xx >= n or yy >= m:
                return 0
            if grid[x][y] ^ grid[xx][yy] == 2:
                 arr[x][y][dirIdx] = 1 + calc(xx, yy, dirIdx)
            return arr[x][y][dirIdx]

        for i in range(n):
            for j in range(m):
                for k in range(len(d)):
                    calc(i, j, k)
        
        # for row in arr:
        #     print(row)
        # for row in grid:
        #     print(row)

        def solve(x: int, y: int, dirIdx: int, distance: int) -> int:
            cur = 0
            # if dirIdx <= 1:
            #     cur = max(arr[x][y][2], arr[x][y][3])
            # else:
            #     cur = max(arr[x][y][0], arr[x][y][1])
            
            #  === ONLY CLOCKWISE ===
            if dirIdx == 0:
                cur = arr[x][y][2]
            elif dirIdx == 1:
                cur = arr[x][y][3]
            elif dirIdx == 2:
                cur = arr[x][y][1]
            elif dirIdx == 3:
                cur = arr[x][y][0]
            # if x == 1 and y == 4 and dirIdx == 3:
            #     print(cur, distance)
            cur += distance
            xx, yy = x + d[dirIdx][0], y + d[dirIdx][1]
            # print(cur, "cur")
            if xx < 0 or yy < 0 or xx >= n or yy >= m or (grid[x][y] + grid[xx][yy]) != 2:
                return cur
            # print(x, y, " ->:: ", xx, yy, ":", dirIdx, d[dirIdx])
            return max(cur, solve(xx, yy, dirIdx, distance + 1))
        
        # for row in arr:
        #     print(row)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                res = max(res, 1)
                for k in range(len(d)):
                    # if k == 1 and i == 0 and j == 2:
                    #     print(solve(i + d[k][0], j + d[k][1], k, 1))
                    xx, yy = i + d[k][0], j + d[k][1]
                    if xx < 0 or yy < 0 or xx >= n or yy >= m or grid[xx][yy] != 2:
                        continue
                    # print(1 + solve(xx, yy, k, 1), i, j, " -> ", xx, yy, k)
                    res = max(res, 1 + solve(xx, yy, k, 1))
        return res