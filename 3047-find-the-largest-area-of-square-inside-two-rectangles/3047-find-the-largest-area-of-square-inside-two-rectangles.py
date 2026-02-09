from typing import List, Tuple

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        #                                       start X, end X, sy,  ey                start X, end X, sy,  ey
        def areaSquareIntersection(rectangle1: Tuple[int, int, int, int], rectangle2: Tuple[int, int, int, int]) -> int:
            sx1, ex1, sy1, ey1 = rectangle1
            sx2, ex2, sy2, ey2 = rectangle2
            sx = max(sx1, sx2)
            ex = min(ex1, ex2)
            width = ex - sx
            sy = max(sy1, sy2)
            ey = min(ey1, ey2)
            height = ey - sy
            if width <= 0 or height <= 0:
                return 0
            return min(height, width) ** 2
        
        res = 0
        n = len(bottomLeft)
        for i in range(n):
            sx1, sy1 = bottomLeft[i]
            ex1, ey1 = topRight[i]
            for j in range(i + 1, n):
                sx2, sy2 = bottomLeft[j]
                ex2, ey2 = topRight[j]
                res = max(res, areaSquareIntersection([sx1, ex1, sy1, ey1], [sx2, ex2, sy2, ey2]))
        return res