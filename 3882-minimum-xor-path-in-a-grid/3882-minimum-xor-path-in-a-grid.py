class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        # time: O(rows * cols * max(grid))
        # space: O(cols * max(grid))
        # method: DP
        rows = len(grid)
        cols = len(grid[0])
        values = [set() for _ in range(cols)]
        values[0].add(grid[0][0])

        for i in range(1, cols):
            for value in values[i - 1]:
                values[i].add(value ^ grid[0][i])

        for i in range(1, rows):
            prev = set()
            for j in range(0, cols):
                current = set()
                
                for value in values[j]:
                    current.add(value ^ grid[i][j])
                
                for value in prev:
                    current.add(value ^ grid[i][j])
                
                values[j] = current
                prev = current
        
        return min(values[-1])