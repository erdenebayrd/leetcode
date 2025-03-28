class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # time: O(N + M)
        # space: O(N + M)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for _ in range(n)]
        queriesOrdered = sorted([(val, idx) for idx, val in enumerate(queries)])
        # print(queriesOrdered)
        curIdxQuery = 0
        queue = SortedList()
        queue.add((grid[0][0], 0, 0)) # starting point
        vis[0][0] = True
        queryRes = [0] * len(queries)
        while len(queue) > 0:
            curVal, curX, curY = queue.pop(0)
            # print(curVal, curX, curY)
            while curIdxQuery < len(queries) and curVal >= queriesOrdered[curIdxQuery][0]:
                curIdxQuery += 1
            if curIdxQuery >= len(queries):
                break
            queryRes[curIdxQuery] += 1
            for i in range(4):
                nx, ny = dx[i] + curX, dy[i] + curY
                if nx < 0 or nx >= n or ny < 0 or ny >= m or vis[nx][ny] is True:
                    continue
                queue.add((grid[nx][ny], nx, ny))
                vis[nx][ny] = True
        # print(queryRes)
        for i in range(1, len(queries)):
            queryRes[i] += queryRes[i - 1]
        
        res = [0] * len(queries)
        for i in range(len(queries)):
            idx = queriesOrdered[i][1]
            res[idx] = queryRes[i]
        return res