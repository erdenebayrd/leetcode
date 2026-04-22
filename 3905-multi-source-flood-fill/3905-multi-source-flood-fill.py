class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        # time: O(n * m * log (n * m))
        # space: O(n * m)
        # method: bfs
        grid = [[0] * m for _ in range(n)]
        queue = deque()
        sources.sort(key=lambda x: x[2], reverse=True)

        for r, c, color in sources:
            queue.append((r, c, color))
            grid[r][c] = color
        while queue:
            r, c, color = queue.popleft()
            for deltaRow, deltaCol in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nextRow, nextCol = r + deltaRow, c + deltaCol
                if nextRow < 0 or nextRow >= n or nextCol < 0 or nextCol >= m or grid[nextRow][nextCol] != 0:
                    continue
                grid[nextRow][nextCol] = color
                queue.append((nextRow, nextCol, color))
        return grid