class FenwickTree:
    def __init__(self, sz: int) -> None:
        self.ft = [0] * (sz + 1)
    
    def update(self, idx: int, value: int) -> None:
        while idx > 0 and idx < len(self.ft):
            self.ft[idx] += value
            idx += idx & -idx
    
    def get(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.ft[idx]
            idx -= idx & -idx
        return res
    
    def rangeSum(self, l: int, r: int) -> int:
        return self.get(r) - self.get(l - 1)

class Leaderboard:

    def __init__(self):
        self.cnt = FenwickTree(100000)
        self.sum = FenwickTree(100000)
        self.score = defaultdict(int)

    def __update(self, score: int, value: int) -> None:
        self.cnt.update(score, value) # O(Log(1e5))
        self.sum.update(score, value * score) # O(Log(1e5))

    def addScore(self, playerId: int, score: int) -> None:
        # remove
        self.__update(self.score[playerId], -1)
        # update
        self.score[playerId] += score
        # add
        self.__update(self.score[playerId], 1)

    def top(self, K: int) -> int:
        n = int(1e5)
        lo, hi = 0, n + 1
        while lo + 1 < hi:
            md = (lo + hi) // 2
            if self.cnt.rangeSum(md, n) >= K: # O(Log(1e5) ^ 2)
                lo = md
            else:
                hi = md
        extra = self.cnt.rangeSum(lo, n) - K
        return self.sum.rangeSum(lo, n) - extra * lo

    def reset(self, playerId: int) -> None:
        # remove
        self.__update(self.score[playerId], -1)
        self.score[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)