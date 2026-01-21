from collections import deque

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        inf = n * m + 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distances = [[[inf] * 4 for _ in range(m)] for _ in range(n)]
        queue = deque()
        for i in range(4):
            row, col = start
            distances[row][col][i] = 0
            queue.append([row, col, i, 0])

        while queue:
            row, col, direction, cost = queue.popleft()
            while row < n and col < m and maze[row][col] == 0:
                nextRow = row + directions[direction][0]
                nextCol = col + directions[direction][1]
                if nextRow < 0 or nextRow >= n or nextCol < 0 or nextCol >= m or maze[nextRow][nextCol] == 1: # hit a wall
                    if distances[row][col][direction] > cost:
                        distances[row][col][direction] = cost
                        for i in range(4):
                            queue.append([row, col, i, cost])
                    else:
                        break
                else:
                    row = nextRow
                    col = nextCol
                    cost += 1
        res = inf
        row, col = destination
        for i in range(4):
            res = min(res, distances[row][col][i])
        if res == inf:
            res = -1
        return res