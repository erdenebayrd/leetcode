from typing import Tuple

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: simulation

        # rotating clockwise 90 degree
        def rotate(row: int, col: int) -> Tuple[int, int]:
            return (col, len(boxGrid) - 1 - row)
        
        cols = len(boxGrid)
        rows = len(boxGrid[0])

        # initializing result
        result = [[""] * cols for _ in range(rows)]

        # rotating and copying
        for i in range(len(boxGrid)):
            for j in range(len(boxGrid[i])):
                row, col = rotate(i, j)
                result[row][col] = boxGrid[i][j]
        
        # apply gravity
        for col in range(cols):
            lastRow = rows - 1
            for row in range(rows - 1, -1, -1):
                if result[row][col] == "#":
                    if row == lastRow:
                        lastRow -= 1
                        continue
                    result[row][col] = "."
                    result[lastRow][col] = "#"
                    lastRow -= 1
                if result[row][col] == "*":
                    lastRow = row - 1
        
        return result