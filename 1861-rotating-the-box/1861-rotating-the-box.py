from typing import Tuple

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: simulation + prefix sum

        # rotating clockwise 90 degree
        def rotate(row: int, col: int) -> Tuple[int, int]:
            return (col, len(boxGrid) - 1 - row)
        
        cols = len(boxGrid)
        rows = len(boxGrid[0])

        # initializing result
        result = [[""] * cols for _ in range(rows)]
        gravity = [[1] * cols for _ in range(rows)]

        # rotating and copying
        for i in range(len(boxGrid)):
            for j in range(len(boxGrid[i])):
                row, col = rotate(i, j)
                result[row][col] = boxGrid[i][j]
                if boxGrid[i][j] == '*' or boxGrid[i][j] == '#':
                    gravity[row][col] = 0

        for row in range(rows - 2, -1, -1):
            for col in range(cols):
                if gravity[row + 1][col] > 0 and result[row][col] != "*":
                    gravity[row][col] += gravity[row + 1][col]

        # apply gravity
        for row in range(rows - 2, -1, -1):
            for col in range(cols):
                if result[row][col] == "#" and gravity[row][col] > 0:
                    result[row][col] = '.'
                    result[row + gravity[row][col]][col] = '#'

        return result