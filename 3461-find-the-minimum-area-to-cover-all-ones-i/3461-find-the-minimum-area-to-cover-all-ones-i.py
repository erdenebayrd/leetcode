class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        le, ri, up, bo = 1000, 0, 1000, 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                le = min(le, j)
                ri = max(ri, j)
                up = min(up, i)
                bo = max(bo, i)
        return (ri - le + 1) * (bo - up + 1)