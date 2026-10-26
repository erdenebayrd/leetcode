from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: BFS    
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def visit(row: int, col: int) -> int:
            queue = deque()
            queue.append((row, col))
            total = grid[row][col]
            visited[row][col] = True
            while queue:
                row, col = queue.popleft()
                for delta_row, delta_col in directions:
                    next_row, next_col = row + delta_row, col + delta_col
                    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or visited[next_row][next_col] or grid[next_row][next_col] <= 0:
                        continue
                    queue.append((next_row, next_col))
                    visited[next_row][next_col] = True
                    total += grid[next_row][next_col]
            return total

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0 and not visited[row][col]:
                    total = visit(row, col)
                    if total % k == 0:
                        count += 1
        
        return count