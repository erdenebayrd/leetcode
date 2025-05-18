class Solution:

    @cache
    def solve(self, comb, idx):
        if idx >= self.n:
            return 1
        res = 0
        for row in self.combinations:
            flag = True
            for i in range(len(row)):
                if row[i] == comb[i]:
                    flag = False
            if flag is False:
                continue
            res = (res + self.solve(row, idx + 1)) % self.mod
        return res


    def colorTheGrid(self, m: int, n: int) -> int:
        # time: O((3 ^ M) * N)
        # space: O((3 ^ M) * N)
        # method: bitmask DP
        self.mod = int(1e9 + 7)
        self.n = n
        self.combinations = []
        for row in list(product([0, 1, 2], repeat=m)):
            flag = True
            for i in range(1, len(row)):
                if row[i] == row[i - 1]:
                    flag = False
            if flag is False:
                continue
            self.combinations.append(row)
        res = 0
        for row in self.combinations:
            res = (res + self.solve(row, 1)) % self.mod
        return res