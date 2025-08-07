class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        res = 0
        n = len(fruits)
        for i in range(n):
            res += fruits[i][i]
            fruits[i][i] = 0
        for i in range(n):
            for j in range(n - i - 1):
                fruits[i][j] = 0
        # for i in range(n):
        #     print(fruits[i])
        second = [[0] * n for _ in range(n)]
        third = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                second[i][j] = fruits[i][j]
                third[i][j] = fruits[i][j]
        d = [1, 0, -1]
        for i in range(n): # row
            for j in range(n): # col
                cur = 0
                for k in range(3):
                    x = i - 1
                    y = j + d[k]
                    if x < 0 or x >= n or y < 0 or y >= n:
                        continue
                    cur = max(cur, second[x][y])
                second[i][j] += cur
        res += second[n - 1][n - 1]
        for i in range(n): # col
            for j in range(n): # row
                cur = 0
                for k in range(3):
                    x = i - 1 # col
                    y = j + d[k] # row
                    if x < 0 or x >= n or y < 0 or y >= n:
                        continue
                    cur = max(cur, third[y][x])
                third[j][i] += cur
        res += third[n - 1][n - 1]
        return res