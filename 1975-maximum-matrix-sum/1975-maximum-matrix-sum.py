class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        mnAbs = float('inf')
        total = 0
        cntNegative = 0
        for row in matrix:
            for val in row:
                x = abs(val)
                mnAbs = min(mnAbs, x)
                total += x
                cntNegative += int(val < 0)
        if cntNegative & 1:
            total -= 2 * mnAbs
        return total