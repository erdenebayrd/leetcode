class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def isMagic(topLeftX: int, topLeftY: int, k: int) -> bool:
            sums = set()
            # row sums
            for row in range(topLeftX, topLeftX + k + 1):
                cur = 0
                for col in range(topLeftY, topLeftY + k + 1):
                    cur += grid[row][col]
                sums.add(cur)
            # col sums
            for col in range(topLeftY, topLeftY + k + 1):
                cur = 0
                for row in range(topLeftX, topLeftX + k + 1):
                    cur += grid[row][col]
                sums.add(cur)
            # Diagonals
            diagonal1, diagonal2 = 0, 0
            for i in range(k + 1):
                diagonal1 += grid[i + topLeftX][i + topLeftY]
                diagonal2 += grid[topLeftX + k - i][topLeftY + i]
            sums.add(diagonal1)
            sums.add(diagonal2)
            return len(sums) == 1
        
        n = len(grid)
        m = len(grid[0])
        res = 1
        for i in range(n):
            for j in range(m):
                k = 0
                while i + k < n and j + k < m:
                    if isMagic(i, j, k) is True:
                        res = max(res, k + 1)
                    k += 1
        return res