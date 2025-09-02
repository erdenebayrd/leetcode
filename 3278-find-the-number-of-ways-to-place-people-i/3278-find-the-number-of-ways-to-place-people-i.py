class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0

        def check(i: int, j: int) -> bool:
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 > x2 or y1 < y2:
                return False
            for k in range(n):
                if k == i or k == j:
                    continue
                x3, y3 = points[k]
                if x1 <= x3 and y1 >= y3 and x3 <= x2 and y3 >= y2:
                    return False
            return True

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if check(i, j) is True:
                    res += 1
        return res