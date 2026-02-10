from functools import cache

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        columns = len(strs[0])

        def isLexographicOrdered(previousIndex: int, currentIndex: int) -> bool: # O(rows)
            if previousIndex < 0: # currentIndex column characters always be greater than nothing
                return True
            for row in range(rows):
                if strs[row][previousIndex] > strs[row][currentIndex]:
                    return False
            return True

        @cache
        def solve(fromIndex: int, currentIndex: int) -> int:
            if currentIndex >= columns:
                return 0
            res = 1 + solve(fromIndex, currentIndex + 1) # deleting currentIndex column
            if isLexographicOrdered(fromIndex, currentIndex) is True:
                res = min(res, solve(currentIndex, currentIndex + 1))
            return res
        

        # time: O(N ^ 3) N is number of rows/columns
        # space: O(N ^ 2) we store every possible "pairs" of column indices
        return solve(-1, 0)