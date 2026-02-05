class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # time: O(factorial(8))
        # space: O(N) N is number of cells which basically is 9 auxiliary 
        
        def minimumCostMatch(left: List[Tuple[int, int]], right: List[Tuple[int, int]]) -> int:
            if len(left) != len(right):
                raise "invalid input"
            if len(left) == 0:
                return 0
            cost = float('inf')
            nextLeft = []
            for i in range(1, len(left)):
                nextLeft.append(left[i])
            for i in range(len(right)):
                leftRow, leftColumn = left[0]
                rightRow, rightColumn = right[i]
                currentCost = abs(leftRow - rightRow) + abs(leftColumn - rightColumn)
                nextRight = []
                for j in range(len(right)):
                    if i == j:
                        continue
                    nextRight.append(right[j])
                cost = min(cost, currentCost + minimumCostMatch(nextLeft, nextRight))
            return cost

        left = []
        right = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    right.append([i, j])
                elif grid[i][j] > 1:
                    for _ in range(grid[i][j] - 1):
                        left.append([i, j])

        return minimumCostMatch(left, right)