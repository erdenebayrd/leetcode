class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        arr = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                arr[i + 1][j + 1] = matrix[i][j] + arr[i][j + 1] + arr[i + 1][j] - arr[i][j]
        
        def get(bx: int, by: int, dx: int, dy: int) -> int:
            return arr[dx][dy] - arr[bx - 1][dy] - arr[dx][by - 1] + arr[bx - 1][by - 1]
        # for x in arr:
        #     print(x)
        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                lo, hi = 0, min(n - i, m - j) + 2
                while lo + 1 < hi:
                    md = (lo + hi) // 2
                    if get(i, j, i + md - 1, j + md - 1) == md * md:
                        lo = md
                    else:
                        hi = md
                res += lo
        return res