class Solution:
    def minimumTotal(self, arr: List[List[int]]) -> int:
        n = len(arr)
        for i in range(1, n):
            for j in range(len(arr[i])):
                cur = int(1e9)
                if j - 1 >= 0:
                    cur = min(cur, arr[i - 1][j - 1])
                if j < len(arr[i - 1]):
                    cur = min(cur, arr[i - 1][j])
                arr[i][j] += cur
        return min(arr[n - 1])