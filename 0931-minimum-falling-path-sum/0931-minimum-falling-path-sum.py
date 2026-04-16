class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # time: O(N ^ 2)
        # space: O(1)
        # method: DP
        n = len(matrix)
        for row in range(1, n):
            for col in range(n):
                parent = matrix[row - 1][col]
                if col - 1 >= 0:
                    parent = min(parent, matrix[row - 1][col - 1])
                if col + 1 < n:
                    parent = min(parent, matrix[row - 1][col + 1])
                matrix[row][col] += parent
        return min(matrix[n - 1])