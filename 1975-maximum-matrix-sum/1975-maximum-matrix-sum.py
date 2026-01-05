class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        mnAbs = float('inf')
        total = 0
        cntNegative = 0
        for row in matrix:
            for val in row:
                mnAbs = min(mnAbs, abs(val))
                total += abs(val)
                cntNegative += int(val < 0)
        if cntNegative & 1:
            total -= 2 * mnAbs
        return total