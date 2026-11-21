class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # time: O(n ^ 2)
        # space: O(1)
        # method: simulation

        n = len(matrix)
        def next_coordinate(row: int, col: int) -> list:
            next_col = n - 1 - row
            next_row = col
            return [next_row, next_col]
        
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                points = []
                row, col = i, j
                for _ in range(4):
                    points.append(row)
                    points.append(col)
                    row, col = next_coordinate(row, col)
                
                # rotate
                p1r, p1c, p2r, p2c, p3r, p3c, p4r, p4c = points
                matrix[p1r][p1c], matrix[p2r][p2c], matrix[p3r][p3c], matrix[p4r][p4c] = matrix[p4r][p4c], matrix[p1r][p1c], matrix[p2r][p2c], matrix[p3r][p3c]
        
        