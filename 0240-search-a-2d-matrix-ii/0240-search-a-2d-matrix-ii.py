import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # time: O(rows * log (cols))
        # space: O(1)
        # method: binary search

        for row in matrix:
            index = bisect.bisect_left(row, target)
            if index < len(row) and row[index] == target:
                return True
        return False