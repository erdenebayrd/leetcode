class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def rangeSum(row: int, col: int, k: int) -> int:
            res = mat[row + k - 1][col + k - 1]
            if row > 0:
                res -= mat[row - 1][col + k - 1]
            if col > 0:
                res -= mat[row + k - 1][col - 1]
            if row > 0 and col > 0:
                res += mat[row - 1][col - 1]
            return res
        
        n = len(mat)
        m = len(mat[0])
        for i in range(1, m):
            mat[0][i] += mat[0][i - 1]
        for i in range(1, n):
            mat[i][0] += mat[i - 1][0]
        for i in range(1, n):
            for j in range(1, m):
                mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]

        # for row in range(n):
        #     print(mat[row])

        def can(k: int) -> bool:
            for i in range(n):
                for j in range(m):
                    if i + k - 1 < n and j + k - 1 < m and rangeSum(i, j, k) <= threshold:
                        return True
            return False

        for k in range(1, min(n, m) + 1):
            if can(k) is False:
                return k - 1
        return min(n, m)