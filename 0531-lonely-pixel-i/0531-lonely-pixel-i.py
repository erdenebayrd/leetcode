class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # time: O(rows * cols)
        # space: O(rows + cols)
        # method: simulation

        rows = len(picture)
        cols = len(picture[0])

        count_row = [0] * rows
        count_col = [0] * cols
        for row in range(rows):
            for col in range(cols):
                if picture[row][col] == 'B':
                    count_row[row] += 1
                    count_col[col] += 1
        count = 0
        for row in range(rows):
            for col in range(cols):
                if picture[row][col] == 'B':
                    if count_row[row] == count_col[col] == 1:
                        count += 1
        return count