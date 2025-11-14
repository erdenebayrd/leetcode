class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        arr = [[0] * n for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            for row in range(row1, row2 + 1):
                arr[row][col1] += 1
                if col2 + 1 < n:
                    arr[row][col2 + 1] -= 1
        for row in range(n):
            for col in range(1, n):
                arr[row][col] += arr[row][col - 1]
        return arr