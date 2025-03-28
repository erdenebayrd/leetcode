class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # time: O(N * Log N)
        # space: O(N)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for _ in range(n)]
        queriesOrdered = sorted([(val, idx) for idx, val in enumerate(queries)])
        vis[0][0] = True
        queue = [(grid[0][0], 0, 0)]
        heapq.heapify(queue)
        points = 0
        res = [0] * len(queries)
        for queryVal, originalIdx in queriesOrdered:
            while queue and queue[0][0] < queryVal:
                _, x, y = heapq.heappop(queue)
                points += 1
                for i in range(4):
                    nx, ny = dx[i] + x, dy[i] + y
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and vis[nx][ny] is False:
                        vis[nx][ny] = True
                        heapq.heappush(queue, (grid[nx][ny], nx, ny))
            res[originalIdx] = points
        return res