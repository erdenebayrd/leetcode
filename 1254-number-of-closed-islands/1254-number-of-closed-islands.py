class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: DFS/BFS/DSU

        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def is_closed_island(row: int, col: int) -> bool:
            visited.add((row, col))
            result = True
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row + delta_row, col + delta_col
                if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                    result = False
                elif (next_row, next_col) not in visited and grid[next_row][next_col] == 0:
                    result &= is_closed_island(next_row, next_col)
            return result
        
        result = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited or grid[row][col] == 1: # already visited or water
                    continue
                if is_closed_island(row, col):
                    result += 1
        return result