from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: BFS
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = deque()

        def dfs(row: int, col: int, queue_ref: deque, visited_ref: set, grid_ref: list) -> None:
            queue_ref.append((row, col, 0))
            visited_ref.add((row, col))
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or (next_row, next_col) in visited_ref or grid_ref[next_row][next_col] == 0:
                    continue
                dfs(next_row, next_col, queue_ref, visited_ref, grid_ref)

        for row in range(rows):
            found = False
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col, queue, visited, grid)
                    found = True
                    break
            if found:
                break
        
        while queue:
            row, col, dist = queue.popleft()
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or (next_row, next_col) in visited:
                    continue
                if grid[next_row][next_col] == 1:
                    return dist
                queue.append((next_row, next_col, dist + 1))
                visited.add((next_row, next_col))
        return 0