def longestVShapedDiagonal(grid):
    n, m = len(grid), len(grid[0])
    
    # Define the expected sequence values
    def get_expected_value(index):
        if index == 0:
            return 1
        return 2 if index % 2 == 1 else 0
    
    # 4 diagonal directions
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    
    # Define clockwise 90-degree turn for each direction
    clockwise_turn = {
        (1, 1): (1, -1),    # SE → SW
        (1, -1): (-1, -1),  # SW → NW
        (-1, -1): (-1, 1),  # NW → NE
        (-1, 1): (1, 1)     # NE → SE
    }
    
    max_length = 0
    
    # Try each cell with value 1 as starting point
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 1:
                continue
                
            # Try each diagonal direction
            for dr, dc in directions:
                # First, build the path going straight (no turn)
                first_path = [(i, j)]
                r, c = i, j
                
                while True:
                    r, c = r + dr, c + dc
                    if not (0 <= r < n and 0 <= c < m):
                        break
                    expected = get_expected_value(len(first_path))
                    if grid[r][c] != expected:
                        break
                    first_path.append((r, c))
                
                # Update max with straight path
                max_length = max(max_length, len(first_path))
                
                # Try making a turn at each position along the path
                new_dr, new_dc = clockwise_turn[(dr, dc)]
                
                for turn_idx in range(len(first_path)):
                    # Start with length up to turn point
                    length = turn_idx + 1
                    r, c = first_path[turn_idx]
                    
                    # Continue in the new direction after turn
                    while True:
                        r, c = r + new_dr, c + new_dc
                        if not (0 <= r < n and 0 <= c < m):
                            break
                        expected = get_expected_value(length)
                        if grid[r][c] != expected:
                            break
                        length += 1
                    
                    max_length = max(max_length, length)
    
    return max_length

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # return longestVShapedDiagonal(grid)
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