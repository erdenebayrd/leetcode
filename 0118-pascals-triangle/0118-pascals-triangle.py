class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 1
        # 1 1
        # 1 2 1
        # 1 3 3 1
        # 1 4 6 4 1
        res = [[1]]
        for i in range(2, numRows + 1):
            res.append([0] * i)
            for j in range(len(res[-1])):
                x, y = 0, 0
                if j - 1 >= 0:
                    x = res[-2][j - 1]
                if j < len(res[-2]):
                    y = res[-2][j]
                res[-1][j] = x + y
        return res
