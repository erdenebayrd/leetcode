import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # time: O(rows * cols * log (rows * cols))
        # space: O(rows * cols)
        # method: Dijkstra
        rows = len(grid)
        cols = len(grid[0])
        cost = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    queue.append((row, col, 0))
                    cost[row][col] = 0
        
        while queue:
            row, col, _ = queue.popleft()
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    continue
                if cost[next_row][next_col] > cost[row][col] + 1:
                    cost[next_row][next_col] = cost[row][col] + 1
                    queue.append((next_row, next_col, cost[row][col] + 1))
        
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = -cost[0][0]
        min_heap = []
        heapq.heappush(min_heap, (dist[0][0], 0, 0))
        while min_heap:
            _, row, col = heapq.heappop(min_heap)
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    continue
                if dist[next_row][next_col] > max(dist[row][col], -cost[next_row][next_col]):
                    dist[next_row][next_col] = max(dist[row][col], -cost[next_row][next_col])
                    heapq.heappush(min_heap, (dist[next_row][next_col], next_row, next_col))
        
        
        return abs(dist[rows - 1][cols - 1])