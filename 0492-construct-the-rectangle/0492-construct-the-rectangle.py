class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # time: O(sqrt(n))
        # space: O(1)
        # method: brute force
        W = int(sqrt(area))
        for width in range(W, 0, -1):
            if area % width == 0:
                return [area // width, width]