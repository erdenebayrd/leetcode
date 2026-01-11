class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # time: O(N ^ 2 * LogN)
        # space: O(N ^ 2)
        n = len(matrix)
        m = len(matrix[0])
        arr = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                arr[i][j] = int(matrix[i][j])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    arr[i][j] += arr[i][j - 1]
                elif j == 0:
                    arr[i][j] += arr[i - 1][j]
                else:
                    arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]
        
        def subSum(rowStart: int, colStart: int, rowEnd: int, colEnd: int) -> int:
            assert rowStart >= 0 and colStart >= 0 and rowEnd < n and colEnd < m
            if rowStart == 0 and colStart == 0:
                return arr[rowEnd][colEnd]
            if rowStart == 0:
                return arr[rowEnd][colEnd] - arr[rowEnd][colStart - 1]
            if colStart == 0:
                return arr[rowEnd][colEnd] - arr[rowStart - 1][colEnd]
            return arr[rowEnd][colEnd] - arr[rowEnd][colStart - 1] - arr[rowStart - 1][colEnd] + arr[rowStart - 1][colStart - 1]
        
        res = 0
        for rowEnd in range(n):
            for curCol in range(m):
                # 1. find rowStart O(Log N)
                lo, hi = -1, rowEnd + 1
                while lo + 1 < hi:
                    md = (lo + hi) // 2
                    if subSum(md, curCol, rowEnd, curCol) == rowEnd - md + 1:
                        hi = md
                    else:
                        lo = md
                if hi == rowEnd + 1:
                    continue
                rowStart = hi
                # 2. find colStart O(Log N)
                lo, hi = -1, curCol + 1
                while lo + 1 < hi:
                    md = (lo + hi) // 2
                    if subSum(rowStart, md, rowEnd, curCol) == (rowEnd - rowStart + 1) * (curCol - md + 1):
                        hi = md
                    else:
                        lo = md
                colStart = hi
                # 3. find colEnd O(Log N)
                lo, hi = curCol, m
                while lo + 1 < hi:
                    md = (lo + hi) // 2
                    if subSum(rowStart, curCol, rowEnd, md) == (rowEnd - rowStart + 1) * (md - curCol + 1):
                        lo = md
                    else:
                        hi = md
                colEnd = lo
                area = (colEnd - colStart + 1) * (rowEnd - rowStart + 1)
                assert area == subSum(rowStart, colStart, rowEnd, colEnd)
                res = max(res, area)
        return res