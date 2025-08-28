class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        def getSortedArr(x: int, y: int) -> List[int]:
            cur = []
            while x < n and y < n:
                cur.append(grid[x][y])
                x += 1
                y += 1
            return sorted(cur)
        
        def replaceGrid(x: int, y: int, arr: List[int]) -> None:
            curIdx = 0
            while x < n and y < n and curIdx < len(arr):
                grid[x][y] = arr[curIdx]
                curIdx += 1
                x += 1
                y += 1

        for i in range(n):
            cur = getSortedArr(0, i)
            replaceGrid(0, i, cur)
            cur = getSortedArr(i, 0)
            replaceGrid(i, 0, cur[::-1])
            
        return grid