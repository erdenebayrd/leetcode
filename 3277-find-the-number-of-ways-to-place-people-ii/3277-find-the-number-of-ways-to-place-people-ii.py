from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)
        res = 0
        for i in range(n):
            y = int(-2e9)
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if y1 >= y2 and y2 > y:
                    res += 1
                    y = y2

        return res