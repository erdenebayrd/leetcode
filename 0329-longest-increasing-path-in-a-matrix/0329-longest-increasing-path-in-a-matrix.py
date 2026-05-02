from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # time: O(rows * cols)
        # space: O(rows * cols)
        # method: DP
        rows = len(matrix)
        cols = len(matrix[0])

        @cache
        def lis(row: int, col: int) -> int:
            result = 0
            for deltaRow, deltaCol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nextRow, nextCol = row + deltaRow, col + deltaCol
                if nextRow < 0 or nextRow >= rows or nextCol < 0 or nextCol >= cols or matrix[row][col] >= matrix[nextRow][nextCol]:
                    continue
                result = max(result, lis(nextRow, nextCol))
            result += 1
            return result

        result = 0
        for row in range(rows):
            for col in range(cols):
                result = max(result, lis(row, col))
        return result