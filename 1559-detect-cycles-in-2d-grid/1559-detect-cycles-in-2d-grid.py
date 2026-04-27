class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: DFS
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        state = [[0] * cols for _ in range(rows)]

        def hasCycle(row: int, col: int, parentRow: int, parentCol: int) -> bool:
            if state[row][col] == 2: # already visited
                return False
            if state[row][col] == 1: # 1 means visiting
                return True
            state[row][col] = 1 # stated visiting
            result = False
            for deltaRow, deltaCol in directions:
                nextRow, nextCol = row + deltaRow, col + deltaCol
                if nextRow == parentRow and nextCol == parentCol:
                    continue
                if nextRow < 0 or nextRow >= rows or nextCol < 0 or nextCol >= cols:
                    continue
                if grid[nextRow][nextCol] == grid[row][col]:
                    result |= hasCycle(nextRow, nextCol, row, col)
            state[row][col] = 2 # done visiting
            return result
        
        result = False
        for row in range(rows):
            for col in range(cols):
                result |= hasCycle(row, col, -1, -1)
        return result