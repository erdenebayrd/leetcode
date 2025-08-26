class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        arr = []
        for x, y in dimensions:
            arr.append((x * x + y * y, x * y))
        arr.sort()
        return arr[-1][-1]