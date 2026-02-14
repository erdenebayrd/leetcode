class Solution:
    def champagneTower(self, poured: int, queryRow: int, queryGlass: int) -> float:
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
        # time: O(N * N) # N is queryRow
        # space: O(N * N) -> O(N) by using only previous row of glasses
        glasses = [poured]
        for row in range(1, queryRow + 1):
            currentRowGlasses = [0] * (row + 1)
            for column in range(len(currentRowGlasses)):
                # glasses[column]
                # glasses[column - 1]
                if column < len(glasses):
                    currentRowGlasses[column] += max(0, glasses[column] - 1) / 2
                if column - 1 >= 0:
                    currentRowGlasses[column] += max(0, glasses[column - 1] - 1) / 2
            glasses = currentRowGlasses[:]
            
        return min(glasses[queryGlass], 1)

        # iteration 0
        # 0
        # 0 0

        # iteration 1
        # 0 0
        # 0 0 0

        # iteration 2
        # 0 0 0
        # 0 0 0 0

        # iteration 3
        # 0 0 0 0
        # 0 0 0 0 0


