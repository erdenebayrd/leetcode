from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0: # which means this cell is gate
                    queue.append((i, j, 0))
        
        while queue:
            row, col, cost = queue.popleft()
            for x, y in directions:
                newRow = row + x
                newCol = col + y
                newCost = cost + 1
                if newRow < 0 or newRow >= len(rooms) or newCol < 0 or newCol >= len(rooms[0]) or rooms[newRow][newCol] == -1 or rooms[newRow][newCol] <= newCost:
                    continue
                queue.append((newRow, newCol, newCost))
                rooms[newRow][newCol] = newCost