class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # time: O(n ^ 4)
        # space: O(n ^ 4)
        # method: brute force + bfs

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        dist = [[0] * cols for _ in range(rows)]
        count = [[0] * cols for _ in range(rows)]
        count_buildings = 0
        inf = float('inf')

        def bfs(row: int, col: int) -> None:
            cost = {}
            queue = deque()
            queue.append((row, col, 0))
            while queue:
                row, col, current_cost = queue.popleft()
                for delta_row, delta_col in directions:
                    next_row, next_col = row + delta_row, col + delta_col
                    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or (next_row, next_col) in cost or grid[next_row][next_col] != 0:
                        continue
                    cost[(next_row, next_col)] = current_cost + 1
                    queue.append((next_row, next_col, current_cost + 1))
                    dist[next_row][next_col] += current_cost + 1
                    count[next_row][next_col] += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    bfs(row, col)
                    count_buildings += 1
        
        result = inf
        for row in range(rows):
            for col in range(cols):
                if count[row][col] == count_buildings:
                    result = min(result, dist[row][col])
        
        if result == inf:
            result = -1
        
        return result