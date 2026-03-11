from collections import defaultdict, deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # time: O(N) N is the distance (number of moves) between [0, 0] -> [x, y] position
        # space: O(N)
        # method: BFS
        if x == 0 and y == 0:
            return 0
        visited = defaultdict(bool)
        queue = deque()
        queue.append([0, 0, 0])
        visited[(0, 0)] = True

        while queue:
            currentX, currentY, currentCost = queue.popleft()
            for deltaX, deltaY in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
                nextX, nextY = currentX + deltaX, currentY + deltaY
                if visited[(nextX, nextY)] is False:
                    visited[(nextX, nextY)] = True
                    queue.append([nextX, nextY, currentCost + 1])
                    if nextX == x and nextY == y:
                        return currentCost + 1