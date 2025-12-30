class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def check(row, col) -> bool:
            cnt = defaultdict(int)
            cntSum = defaultdict(int)
            diagnalSum0 = 0
            diagnalSum1 = 0
            for r in range(row - 2, row + 1):
                rowSum = 0
                for c in range(col - 2, col + 1):
                    x = grid[r][c]
                    cnt[x] += 1
                    rowSum += x
                    if r - c == row - col:
                        diagnalSum0 += x
                    if r + c - row - col == -2:
                        diagnalSum1 += x
                cntSum[rowSum] += 1
            for c in range(col - 2, col + 1):
                colSum = 0
                for r in range(row - 2, row + 1):
                    x = grid[r][c]
                    colSum += x
                cntSum[colSum] += 1
            # print("-" * 100)
            # print(cnt)
            # print(diagnalSum0, diagnalSum1)
            # print(cntSum)
            # print("-" * 100)
            for i in range(1, 10):
                if cnt[i] != 1:
                    return False
            if diagnalSum0 != diagnalSum1:
                return False
            if len(cntSum) != 1:
                return False
            
            return True


        res = 0
        for row in range(2, n):
            for col in range(2, m):
                res += int(check(row, col))
        return res