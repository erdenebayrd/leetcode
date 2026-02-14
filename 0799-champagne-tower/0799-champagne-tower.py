class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # at 1st row 1 glass
        # 1 or more poured 1st row glasses be full

        # at 2nd row 2 glasses
        # 3 or more poured 2nd row glasses be full

        # at 3rd row 3 glasses
        # 3 or more poured 2nd row glasses be full
       
        # 6
        #                     1                                                         1
        #                1           1                                                  2
        #         0.75        1          0.75                                           3
        #      0        0.25        0.25        0                                       4

        # N * N

        n = query_row + 1
        glasses = []
        for row in range(n):
            glasses.append([0] * (row + 1))
        glasses[0][0] = poured
        for row in range(1, n):
            for column in range(len(glasses[row])):
                # [row - 1][column - 1] if column - 1 >= 0
                # [row - 1][column]
                if column < len(glasses[row - 1]):
                    glasses[row][column] += max(glasses[row - 1][column] - 1, 0) / 2
                if column - 1 >= 0:
                    glasses[row][column] += max(glasses[row - 1][column - 1] - 1, 0) / 2
        
        return min(glasses[query_row][query_glass], 1)

        # 0 0 0 0 0 0
        # 0 0 0 0 0 0
        # 0 0 0 0 0 0
        # 0 0 0 0 0 0
        # 0 0 0 0 0 0
        # 0 0 0 0 0 0