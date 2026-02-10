class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        left, right = [], []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    right.append([i, j])
                while grid[i][j] > 1:
                    left.append([i, j])
                    grid[i][j] -= 1
        n = len(left)
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                currentCost = 0
                for k in range(2):
                    currentCost += abs(left[i][k] - right[j][k])
                cost[i][j] = currentCost
        
        @cache
        def solve(leftBit: int, rightBit: int) -> int:
            if leftBit == (1 << n) - 1:
                return 0
            res = float('inf')
            for i in range(n):
                if (leftBit >> i) ^ 1:
                    for j in range(n):
                        if (rightBit >> j) ^ 1 == 1:
                            res = min(res, cost[i][j] + solve(leftBit | (1 << i), rightBit | (1 << j)))
            return res
        
        return solve(0, 0)