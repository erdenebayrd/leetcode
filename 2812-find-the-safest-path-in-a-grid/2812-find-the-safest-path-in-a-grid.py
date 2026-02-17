from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # tc: O(N ^ 2) N is length of grid
        # sc: O(N ^ 2) store, distances

        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def nextCells(row, col):
            cells = []
            for direction in directions:
                deltaRow, deltaCol = direction
                nextRow = deltaRow + row
                nextCol = deltaCol + col
                if 0 <= nextRow < n and 0 <= nextCol < n:
                    cells.append([nextRow, nextCol])
            return cells

        distances = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    distances[i][j] = 0
                    queue.append([i, j, 0])

        while queue:
            row, col, dist = queue.popleft()
            cells = nextCells(row, col)
            for nextRow, nextCol in cells:   
                if distances[nextRow][nextCol] > dist + 1:
                    distances[nextRow][nextCol] = dist + 1
                    queue.append([nextRow, nextCol, dist + 1])
        
        for i in range(n):
            print(distances[i])

        # dijkstra for max(min) path
        maxHeap = []
        heapq.heappush(maxHeap, [-distances[0][0], 0, 0])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while maxHeap:
            negativeSafe, row, col = heapq.heappop(maxHeap)
            safe = -negativeSafe
            if row == n - 1 and col == n - 1:
                return safe
            cells = nextCells(row, col)
            for nextRow, nextCol in cells:
                if visited[nextRow][nextCol] is False:
                    visited[nextRow][nextCol] = True
                    newSafe = min(safe, distances[nextRow][nextCol])
                    heapq.heappush(maxHeap, [-newSafe, nextRow, nextCol])
        
        return -1