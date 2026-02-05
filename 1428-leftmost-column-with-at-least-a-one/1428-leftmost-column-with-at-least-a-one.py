# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, columns = binaryMatrix.dimensions()
        if rows <= 0 or columns <= 0:
            return -1
        
        def check(column: int) -> bool:
            for row in range(rows):
                if binaryMatrix.get(row, column) == 1:
                    return True
            return False

        low, high = -1, columns
        while low + 1 < high:
            middle = (low + high) // 2
            if check(middle):
                high = middle
            else:
                low = middle
        if high == columns:
            high = -1
        return high