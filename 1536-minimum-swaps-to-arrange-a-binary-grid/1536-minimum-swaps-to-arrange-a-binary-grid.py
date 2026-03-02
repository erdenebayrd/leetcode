class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid) # number of rows and cols
        rightMostOnePosition = [-1] * n # right most 1 bit position for each rows
        for row in range(n):
            for col in range(n - 1, -1, -1):
                if grid[row][col] == 1:
                    rightMostOnePosition[row] = col
                    break
        
        print(rightMostOnePosition)
        result = 0
        for row in range(n):
            # n - row - 1 number of trailing zeros required for this row
            if rightMostOnePosition[row] <= row: # no swap required
                continue
            
            swapRow = -1
            for nextRow in range(row + 1, n):
                if rightMostOnePosition[nextRow] <= row:
                    swapRow = nextRow
                    break
                    
            if swapRow == -1:
                return -1
            # place this "swapRow" into current row
            result += swapRow - row
            print(row, swapRow)
            while row < swapRow:
                rightMostOnePosition[swapRow - 1], rightMostOnePosition[swapRow] = rightMostOnePosition[swapRow], rightMostOnePosition[swapRow - 1]
                swapRow -= 1
        return result