class SegmentTree: # we only need total covered area NOT the covered area within given [L, R] range on a query
    def __init__(self, xs: List[int]) -> None:
        self.xs = xs
        self.count = [0] * 8 * len(xs)
        self.covered = [0] * 8 * len(xs)
    
    def query(self) -> int:
        return self.covered[1]
    
    def update(self, p: int, l: int, r: int, xl: int, xr: int, val: int) -> None:
        if l > r or self.xs[l] >= xr or self.xs[r + 1] <= xl:
            return
        if self.xs[l] >= xl and self.xs[r + 1] <= xr:
            self.count[p] += val
        else:
            self.update(2 * p, l, (l + r) // 2, xl, xr, val)
            self.update(2 * p + 1, (l + r) // 2 + 1, r, xl, xr, val)
        if self.count[p] > 0: # [l, r] -> 1
            self.covered[p] = self.xs[r + 1] - self.xs[l]
        else: # what if the current node is leaf? => 4 * n -> 8 * n for enough node accesses on the segment tree
            self.covered[p] = self.covered[2 * p] + self.covered[2 * p + 1]

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = set()
        for x, _, l in squares:
            xs.update([x, x + l])
        xs = sorted(list(xs))
        # print(xs)
        n = len(xs)
        st = SegmentTree(xs)
        events = []
        for x, y, l in squares:
            events.append([y, x, x + l, 1])
            events.append([y + l, x, x + l, -1])
        totalArea = 0
        events.sort()
        prevY = events[0][0]
        areas = []
        # print(events)
        for y, xl, xr, val in events:
            width = st.query()
            height = y - prevY
            totalArea += height * width
            # print(y, xl, xr, val, width, height)
            st.update(1, 0, n - 2, xl, xr, val)
            #              width,     y, currArea
            areas.append([st.query(), y, totalArea])
            prevY = y
        # print(totalArea)
        area, width, y = 0, 0, 0
        for i in range(len(areas)):
            if areas[i][-1] * 2.0 >= totalArea:
                break
            width, y, area = areas[i]
        # print(width, y, area)
        # print(areas)
        return (totalArea - 2.0 * area) / (2.0 * width) + y