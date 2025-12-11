class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xd = {}
        buildings.sort(key=lambda x: x[1])
        for x, y in buildings:
            if x not in xd:
                xd[x] = []
            xd[x].append(y)

        yd = {}
        buildings.sort(key=lambda x: x[0])
        for x, y in buildings:
            if y not in yd:
                yd[y] = []
            yd[y].append(x)
        
        res = 0
        for x, y in buildings:
            idx = bisect_left(xd[x], y)
            if idx == 0 or idx == len(xd[x]) - 1:
                continue

            idx = bisect_left(yd[y], x)
            if idx == 0 or idx == len(yd[y]) - 1:
                continue

            res += 1
            
        return res