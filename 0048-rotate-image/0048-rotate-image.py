class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # time: O(N ^ 2)
        # space: O(1)
        # method: math + memory trick (bit manipulation)

        delta = 1000
        bit = 11
        n = len(matrix)

        def newPosition(row: int, col: int) -> Tuple[int, int]: # new row, new col
            # row = 0 -> col = n - 1
            # newCol = n - 1 - row
            # newRow = col
            return (col, n - 1 - row)
        
        # tmp = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         row, col = newPosition(i, j)
        #         tmp[row][col] = matrix[i][j]
        # for i in range(n):
        #     print(tmp[i])
        
        def add(row: int, col: int, value: int) -> None:
            lastBits = (1 << bit) - 1
            value &= lastBits
            value <<= bit
            matrix[row][col] &= lastBits
            matrix[row][col] |= value

        for i in range(n):
            for j in range(n):
                matrix[i][j] += delta
        
        for i in range(n):
            for j in range(n):
                row, col = newPosition(i, j)
                add(row, col, matrix[i][j])
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] >>= bit
                matrix[i][j] -= delta