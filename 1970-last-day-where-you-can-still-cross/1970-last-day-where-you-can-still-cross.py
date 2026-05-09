class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def check(idx: int) -> bool:
            visit = [[0] * col for _ in range(row)]
            for i in range(idx + 1):
                r, c = cells[i]
                visit[r - 1][c - 1] = 1
            
            def dfs(r: int, c: int) -> None:
                if visit[r][c] != 0:
                    return
                visit[r][c] = -1
                d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                for i in range(len(d)):
                    xx, yy = d[i]
                    x = r + xx
                    y = c + yy
                    if x < 0 or y < 0 or x >= row or y >= col:
                        continue
                    dfs(x, y)

            for i in range(col):
                dfs(0, i)
            for i in range(col):
                if visit[row - 1][i] == -1:
                    return True
            return False

        lo, hi = -1, len(cells)
        while lo + 1 < hi:
            md = (lo + hi) // 2
            if check(md) is True:
                lo = md
            else:
                hi = md

        return lo + 1