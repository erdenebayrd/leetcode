from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: BFS
        rows = len(grid)
        cols = len(grid[0])
        
        inf = float('inf')
        queue = deque()
        dist = [[inf] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    queue.append((i, j))
                    dist[i][j] = 0
        
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            row, col = queue.popleft()
            for delta_row, delta_col in delta:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or dist[next_row][next_col] != inf or grid[next_row][next_col] == 'X':
                    continue
                dist[next_row][next_col] = dist[row][col] + 1
                queue.append((next_row, next_col))
                if grid[next_row][next_col] == '#':
                    return dist[row][col] + 1
        return -1