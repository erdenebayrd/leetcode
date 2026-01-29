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
            row, column, cost = queue.popleft()
            cost += 1 # added 1 to go to neighbor nodes
            for deltaRow, deltaColumn in directions:
                destinationRow = row + deltaRow
                destinationColumn = column + deltaColumn
                if destinationRow < 0 or destinationRow >= len(rooms) or destinationColumn < 0 or destinationColumn >= len(rooms[0]) or rooms[destinationRow][destinationColumn] == -1 or rooms[destinationRow][destinationColumn] <= cost:
                    continue
                queue.append((destinationRow, destinationColumn, cost))
                rooms[destinationRow][destinationColumn] = cost