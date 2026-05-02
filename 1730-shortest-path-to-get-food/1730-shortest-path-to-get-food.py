from collections import deque, defaultdict

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: BFS
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        row, col = -1, -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    row, col = i, j

        queue = deque()
        queue.append((row, col, 0))
        visited.add((row, col))
        while queue:
            row, col, distance = queue.popleft()
            if grid[row][col] == "#":
                return distance
            for deltaRow, deltaCol in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nextRow, nextCol = row + deltaRow, col + deltaCol
                if nextRow < 0 or nextRow >= rows or nextCol < 0 or nextCol >= cols or (nextRow, nextCol) in visited or grid[nextRow][nextCol] == 'X':
                    continue
                if grid[nextRow][nextCol] == "#":
                    return distance + 1
                visited.add((nextRow, nextCol))
                queue.append((nextRow, nextCol, distance + 1))
        return -1