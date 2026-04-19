class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
            since we are going from 0,0 -> n -1, n -1 position and go back to 0, 0,
            its about find a 2 different paths (can be same if there is only one possible path)
            starting from 0, 0 -> n - 1, n - 1.
            okay now lets start to think about to find 2 different paths from 0, 0 -> n - 1, n - 1
            they only can down or right at a time
            meaning, 2 people never go a cell other person passed in a past.
            at the same time, 2 people can collide at the same cell.
            meaning we don't need to store STATE of the board (cherry board)
            lets say 3 steps passed
            meaning r1 + c1 == 3 and r2 + c2 == 3 as well
            r1 + c1 == r2 + c2 all the time
            meaning we can say r1 = r2 + c2 - c1
            meaning we only store r2, c2, c1 at DP state 
            it gives me a chance to solve this DP by N ^ 3
            N is the side length of perfect square
        """
        # time: O(N ^ 3)
        # space: O(N ^ 3)
        # method: DP
        n = len(grid)
        @cache
        def solve(r2: int, c2: int, c1: int) -> float:
            r1 = r2 + c2 - c1
            if r1 < 0 or r1 >= n or c1 < 0 or c1 >= n or r2 < 0 or r2 >= n or c2 < 0 or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")
            if r1 == n - 1 and c1 == n - 1 and r2 == n - 1 and c2 == n - 1:
                return grid[n - 1][n - 1]
            result = float('-inf')
            cherry = grid[r1][c1]
            if r1 != r2 or c1 != c2:
                cherry += grid[r2][c2]
            # second person go right and first go right as well
            result = max(result, solve(r2, c2 + 1, c1 + 1))
            # second person go right and first go down
            result = max(result, solve(r2, c2 + 1, c1))
            # second person go down and first go right
            result = max(result, solve(r2 + 1, c2, c1 + 1))
            # second person go down adn first go down 
            result = max(result, solve(r2 + 1, c2, c1))
            result += cherry
            return result
        
        result = solve(0, 0, 0)
        if result == float('-inf'):
            result = 0
        return result
