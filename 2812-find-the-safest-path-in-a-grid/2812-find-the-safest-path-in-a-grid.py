import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: 0-1 BFS
        rows = len(grid)
        cols = len(grid[0])
        cost = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    cost[row][col] = 0
        
        while queue:
            row, col = queue.popleft()
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    continue
                if cost[next_row][next_col] > cost[row][col] + 1:
                    cost[next_row][next_col] = cost[row][col] + 1
                    queue.append((next_row, next_col))
        
        queue = deque()
        queue.append((0, 0, 0))
        visited = set()
        visited.add((0, 0))
        while queue:
            row, col, level = queue.popleft()
            if row == rows - 1 and col == cols - 1:
                return cost[0][0] - level
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + delta_row, col + delta_col
                next_node = (next_row, next_col)
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or next_node in visited:
                    continue
                visited.add(next_node)
                if cost[next_row][next_col] >= cost[row][col]: # edge weight is 0
                    cost[next_row][next_col] = cost[row][col]
                    queue.appendleft((next_row, next_col, level))
                else: # cost[next_row][next_col] < cost[row][col]: # edge weight is 1
                    queue.append((next_row, next_col, level + 1))