from functools import cache

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        # # time: O(N ^ 4)
        # # space: O(N ^ 3)
        # # method: DP
        # n = len(grid)
        # for col in range(n):
        #     for row in range(1, n):
        #         grid[row][col] += grid[row - 1][col]
        
        # def isOut(rowOrCol: int) -> bool:
        #     if rowOrCol < 0 or rowOrCol >= n:
        #         return True
        #     return False

        # def getColumnRangeSum(startRow: int, endRow: int, column: int) -> int:
        #     if isOut(startRow) or isOut(endRow) or isOut(column) or endRow < startRow:
        #         return 0
        #     if startRow == 0:
        #         return grid[endRow][column]
        #     return grid[endRow][column] - grid[startRow - 1][column]
        
        # @cache
        # def solve(prevPrevHeight: int, prevHeight: int, currentColumn: int) -> int:
        #     if currentColumn > n:
        #         return 0
        #     # no paint at all (currentColumn)
        #     score = getColumnRangeSum(prevHeight, prevPrevHeight - 1, currentColumn - 1)
        #     result = score + solve(prevHeight, 0, currentColumn + 1)
        #     if currentColumn == n:
        #         return result
            
        #     # started painting
        #     for currentColumnPaintedHeight in range(1, n + 1):
        #         startRow = prevHeight
        #         endRow = max(prevPrevHeight, currentColumnPaintedHeight) - 1
        #         score = getColumnRangeSum(startRow, endRow, currentColumn - 1)
        #         result = max(result, score + solve(prevHeight, currentColumnPaintedHeight, currentColumn + 1))
        #     return result
        
        # return solve(0, 0, 0)

        # # ----------------------------- O(N ^ 3) DP splitting left and right half -----------------------------
        # # time: O(N ^ 3)
        # # space: O(N ^ 2)
        # # method: DP
        # n = len(grid)
        # for col in range(n):
        #     for row in range(1, n):
        #         grid[row][col] += grid[row - 1][col]
        
        # def isOut(rowOrColumn: int) -> bool:
        #     if rowOrColumn < 0 or rowOrColumn >= n:
        #         return True
        #     return False
        
        # def getColumnRangeSum(startRow: int, endRow: int, column: int) -> int:
        #     if isOut(startRow) or isOut(endRow) or isOut(column) or endRow < startRow:
        #         return 0
        #     if startRow == 0:
        #         return grid[endRow][column]
        #     return grid[endRow][column] - grid[startRow - 1][column]
        
        # @cache
        # def solve(prevHeight: int, currentColumn: int, prevColumnAlreadyScored: bool) -> int:
        #     if currentColumn == n: # at the end of row (current column hits at the end)
        #         return 0
        #     result = 0
        #     for rowsPaintedOnCurrentColumn in range(n + 1): # 0 means no paint, at max n rows at current columns be painted
        #         # left shadow is already calculated
        #         if prevColumnAlreadyScored is True:
        #             # meaning we have only one choice left which is current column (current column is getting scored)
        #             # 1. current column's left shadow
        #             # 2. current column's right shadow
        #             # getting max of [1] and [2]
                    
        #             # [1] left shadow of current column
        #             score = getColumnRangeSum(rowsPaintedOnCurrentColumn, prevHeight - 1, currentColumn)
        #             result = max(result, score + solve(rowsPaintedOnCurrentColumn, currentColumn + 1, True))
        #             # [2] right shadow of current column (which actually will be calculated in the future /next steps/ )
        #             score = 0
        #             result = max(result, score + solve(rowsPaintedOnCurrentColumn, currentColumn + 1, False))
        #         else:
        #             # [1] left shadow of current column
        #             score = getColumnRangeSum(rowsPaintedOnCurrentColumn, prevHeight - 1, currentColumn) # can be zero
        #             # need to add right shadow of currentColumn - 1 ( prev column's right shadow comes from current column )
        #             score += getColumnRangeSum(prevHeight, rowsPaintedOnCurrentColumn - 1, currentColumn - 1) # can be zero as well
        #             result = max(result, score + solve(rowsPaintedOnCurrentColumn, currentColumn + 1, True))

        #             # [2] right shadow of current column (which actually will be calculated in the future /next steps/ )
        #             # below is just prev column's right shadow
        #             score = getColumnRangeSum(prevHeight, rowsPaintedOnCurrentColumn - 1, currentColumn - 1) # can be zero as well
        #             result = max(result, score + solve(rowsPaintedOnCurrentColumn, currentColumn + 1, False))

        #     return result

        # result = solve(0, 0, True)
        # solve.cache_clear()
        # return result



        from functools import cache
import sys
from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        sys.setrecursionlimit(1 << 25)
        n = len(grid)
        # padded column prefix sums: colP[c][r] = grid[0][c] + ... + grid[r-1][c]
        # range [a, b] sum on column c becomes colP[c][b+1] - colP[c][a]; no special case.
        colP = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            s = 0
            for r in range(n):
                s += grid[r][c]
                colP[c][r + 1] = s

        @cache
        def solve(prevHeight, currentColumn, prevColumnAlreadyScored):
            if currentColumn == n:
                return 0
            ph = prevHeight
            c  = currentColumn
            cur_col_p  = colP[c]
            prev_col_p = colP[c - 1] if c >= 1 else None

            best = 0
            for h in range(n + 1):
                # right-shadow of col c-1 if not yet scored: rows [ph, h-1]
                if (not prevColumnAlreadyScored) and prev_col_p is not None and ph < h:
                    r_prev = prev_col_p[h] - prev_col_p[ph]
                else:
                    r_prev = 0
                # left-shadow of col c: rows [h, ph-1]
                if h < ph:
                    l_cur = cur_col_p[ph] - cur_col_p[h]
                else:
                    l_cur = 0

                # option A: score col c via left shadow now
                v = r_prev + l_cur + solve(h, c + 1, True)
                if v > best: best = v
                # option B: defer col c, will be scored via right shadow next step
                v = r_prev + solve(h, c + 1, False)
                if v > best: best = v
            return best

        return solve(0, 0, True)