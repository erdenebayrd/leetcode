class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # time: O(N * Log N)
        # space: O(N)
        # method: ternary search
        arr = []
        for row in grid:
            for col in row:
                arr.append(col)
        if len(arr) == 1:
            return 0
        arr.sort()
        n = len(arr)
        for i in range(1, n):
            if (arr[i] - arr[0]) % x != 0:
                return -1
        
        res = 0
        for el in arr:
            res += abs(el - arr[n // 2]) // x
        return res
