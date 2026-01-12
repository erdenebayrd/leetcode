class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def calc(a: List[int], b: List[int]) -> int:
            assert len(a) == len(b) == 2
            diffX = abs(a[0] - b[0])
            diffY = abs(a[1] - b[1])
            return max(diffX, diffY)

        res = 0
        for i in range(1, len(points)):
            res += calc(points[i - 1], points[i])
        return res