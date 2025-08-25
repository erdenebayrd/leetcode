class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        def getDiagonal(x: int, y: int) -> List[int]:
            res = []
            while x >= 0 and x < n and y >= 0 and y < m:
                res.append(mat[x][y])
                x -= 1
                y += 1
            return res
        res = []
        lastReversed = True
        for i in range(n): # row
            arr = getDiagonal(i, 0)
            if lastReversed is False:
                arr = arr[::-1]
            lastReversed = not lastReversed
            res.extend(arr)
        
        for i in range(1, m): # col
            arr = getDiagonal(n - 1, i)
            if lastReversed is False:
                arr = arr[::-1]
            lastReversed = not lastReversed
            res.extend(arr)

        return res