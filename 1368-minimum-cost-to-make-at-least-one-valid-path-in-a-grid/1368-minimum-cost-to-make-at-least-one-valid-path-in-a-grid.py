from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: O-1 BFS (instead of dijkstra)

        rows = len(grid)
        cols = len(grid[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        queue.append((0, 0)) # source node
        while queue:
            row, col = queue.popleft()
            for i in range(len(directions)):
                delta_row, delta_col = directions[i]
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    continue
                cost = 1
                if grid[row][col] - 1 == i:
                    cost = 0
                if dist[next_row][next_col] > dist[row][col] + cost:
                    dist[next_row][next_col] = dist[row][col] + cost
                    if cost == 0:
                        queue.appendleft((next_row, next_col))
                    else:
                        queue.append((next_row, next_col))
        return dist[rows - 1][cols - 1]