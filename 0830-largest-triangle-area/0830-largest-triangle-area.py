class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        
        def dist(i: int, j: int) -> int:
            x1, y1 = points[i]
            x2, y2 = points[j]
            x = abs(x1 - x2)
            y = abs(y1 - y2)
            return sqrt(x * x + y * y)

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a = dist(i, j)
                    b = dist(j, k)
                    c = dist(i, k)
                    if a + b <= c or a + c <= b or b + c <= a:
                        continue
                    s = float(a + b + c) / 2.0
                    area = sqrt(s * (s - a) * (s - b) * (s - c))
                    res = max(res, area)
        return res
