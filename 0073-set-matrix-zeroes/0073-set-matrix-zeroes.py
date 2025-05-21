class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        inf = int(3e9)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != 0:
                    continue
                for k in range(n): # j'th col
                    if matrix[k][j] == 0:
                        continue
                    matrix[k][j] = inf
                for k in range(m): # i'th row
                    if matrix[i][k] == 0:
                        continue
                    matrix[i][k] = inf
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != inf:
                    continue
                matrix[i][j] = 0