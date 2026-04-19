class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        they never go on a path the other robot passed past.
        they only can collide at the same cell at same moment
        and they are always be on a same row
        """
        # time: O(row * col * col)
        # space: O(row * col * col)
        # method: DP
        rows = len(grid)
        cols = len(grid[0])
        
        @cache
        def solve(row: int, col1: int, col2: int) -> float:
            if col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return float('-inf')
            if row >= rows:
                return 0
            cherries = grid[row][col1]
            if col1 != col2:
                cherries += grid[row][col2]
            result = float("-inf")
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
            for deltaCol in directions:
                nextCol1, nextCol2 = col1 + deltaCol[0], col2 + deltaCol[1]
                result = max(result, solve(row + 1, nextCol1, nextCol2))
            result += cherries
            return result

        result = solve(0, 0, cols - 1)
        return result