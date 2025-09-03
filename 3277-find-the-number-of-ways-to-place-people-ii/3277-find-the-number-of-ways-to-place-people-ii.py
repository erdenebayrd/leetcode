from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        # print(points)
        n = len(points)
        res = 0
        for i in range(n):
            sl = SortedList([])
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 <= x2 and y1 >= y2:
                    idx = sl.bisect_left(y2)
                    # if idx == len(sl) or (idx < len(sl) and y1 < sl[idx]):
                    if idx == len(sl):
                        # print(sl[idx])
                        res += 1
                    # if sl.bisect_left(y1) - sl.bisect_left(y2) == 0:
                    #     res += 1
                    #     print(i, j)
                if y1 >= y2:
                    sl.add(y2)
        return res